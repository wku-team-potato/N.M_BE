from django.shortcuts import render
from .models import Group, GroupMember, GroupRanking
from .serializers import GroupSerializer, GroupMemberSerializer, GroupRankingSerializer, PublicInfoSerializer, GroupDetailSerializer
from .permissions import IsGroupAdmin
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CreateGroup(generics.CreateAPIView):
    """
    그룹을 생성하는 API 뷰

    새로운 그룹을 생성합니다.
    
    
    그룹 이름은 중복될 수 없습니다.
    
    
    그룹 생성자는 요청을 보낸 사용자로 자동 설정됩니다.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        group_name = serializer.validated_data.get('name')
        if Group.objects.filter(name=group_name).exists():
            raise ValidationError({"name": "이미 존재하는 그룹 이름입니다."})
        
        group = serializer.save(creator=self.request.user)
        GroupMember.objects.create(
            user_id=self.request.user,
            group_id=group,
            is_admin=True
        )
        
        GroupRanking.objects.create(
            group_id=group,
            total_points=0
        )

    def create(self, request, *args, **kwargs):
        """
        그룹 생성 요청 처리 및 통일된 응답 반환
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            return Response({
                "success": True,
                "message": "그룹이 성공적으로 생성되었습니다.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({
                "success": False,
                "message": "그룹 생성에 실패했습니다.",
                "errors": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "success": False,
                "message": "서버에서 오류가 발생했습니다.",
                "errors": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GroupListView(generics.ListAPIView):
    """
    사용자가 속한 그룹 목록을 조회하는 API 뷰

    사용자가 GroupMember로 속한 모든 그룹 목록을 조회합니다.
    """
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # GroupMember를 통해 현재 사용자가 속한 그룹 조회
        user = self.request.user
        return Group.objects.filter(groupmember__user_id=user).distinct().order_by('-created_at')

class GroupAllListView(generics.ListAPIView):
    """
    모든 그룹 목록을 조회하는 API 뷰

    모든 그룹 목록을 조회합니다.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Group.objects.all().order_by('-created_at')

class GroupSearchListView(generics.ListAPIView):
    """
    그룹 검색 결과를 조회하는 API 뷰

    검색어에 매칭되는 그룹 목록을 조회합니다.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search = self.kwargs.get('search')
        return Group.objects.filter(name__icontains=search).order_by('-created_at')
    
class GroupUpdateView(generics.UpdateAPIView):
    """
    그룹 정보를 수정하는 API 뷰

    그룹 정보를 수정합니다.
    
    그룹 생성자만 수정할 수 있습니다.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsGroupAdmin]

    def perform_update(self, serializer):
        group = self.get_object()
        if group.creator != self.request.user:
            raise ValidationError({"detail": "그룹 생성자만 수정할 수 있습니다."})
        serializer.save()

    def update(self, request, *args, **kwargs):
        """
        그룹 정보 수정 처리 및 통일된 응답 반환
        """
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response({
                "success": True,
                "message": "그룹 정보가 성공적으로 수정되었습니다.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response({
                "success": False,
                "message": "그룹 정보 수정에 실패했습니다.",
                "errors": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "success": False,
                "message": "서버에서 오류가 발생했습니다.",
                "errors": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GroupDeleteView(generics.DestroyAPIView):
    """
    그룹을 삭제하는 API 뷰

    그룹을 삭제합니다.
    
    그룹 생성자만 삭제할 수 있습니다.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsGroupAdmin]

    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise ValidationError("그룹 생성자만 삭제할 수 있습니다.")
        instance.delete()

class GroupJoinView(generics.CreateAPIView):
    """
    그룹에 가입하는 API 뷰


    그룹에 가입합니다.
    """
    
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        group_id = self.request.data.get('group_id')
        if not group_id:
            raise ValidationError({"detail": "그룹 ID가 필요합니다."})
        
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            raise ValidationError({"detail": "그룹이 존재하지 않습니다."})
        
        if GroupMember.objects.filter(user_id=self.request.user, group_id=group).exists():
            raise ValidationError({"detail": "이미 가입한 그룹입니다."})
        
        serializer.save(user_id=self.request.user, group_id=group)

    def create(self, request, *args, **kwargs):
        """
        그룹 가입 요청 처리 및 통일된 응답 반환
        
        그룹 가입에 실패하면 ValidationError를 발생시킵니다.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                "success": True,
                "message": "그룹에 성공적으로 가입했습니다.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            # ValidationError를 클라이언트 친화적인 형식으로 변환
            return Response({
                "success": False,
                "message": "그룹 가입에 실패했습니다.",
                "errors": e.detail  # ValidationError 세부 내용
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 기타 서버 오류 처리
            return Response({
                "success": False,
                "message": "서버에서 오류가 발생했습니다.",
                "errors": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GroupLeaveView(generics.DestroyAPIView):
    """
    그룹에서 탈퇴하는 API 뷰

    그룹에서 탈퇴합니다.
    그룹 생성자도 탈퇴할 수 있습니다.
    탈퇴 후 그룹 인원이 0명이면 그룹을 삭제합니다.
    """
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'group_id'  # URL에서 group_id를 받음

    def get_object(self):
        """
        URL에서 전달된 group_id를 사용해 그룹 멤버 객체를 조회
        """
        group_id = self.kwargs.get(self.lookup_url_kwarg)
        if not group_id:
            return Response({
                "success": False,
                "message": "그룹 ID가 필요합니다.",
                "deleted": False
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({
                "success": False,
                "message": "해당 그룹이 존재하지 않습니다.",
                "deleted": False
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            group_member = GroupMember.objects.get(user_id=self.request.user, group_id=group)
        except GroupMember.DoesNotExist:
            return Response({
                "success": False,
                "message": "가입하지 않은 그룹입니다.",
                "deleted": False
            }, status=status.HTTP_400_BAD_REQUEST)

        return group_member
    
    def destroy(self, request, *args, **kwargs):
        """
        그룹 탈퇴 및 그룹 삭제 여부를 처리하고 통일된 응답 반환

        """
        instance = self.get_object()

        # get_object에서 예외 응답을 반환한 경우 바로 리턴
        if isinstance(instance, Response):
            return instance

        group = instance.group_id  # 해당 멤버가 속한 그룹 가져오기
        instance.delete()  # 그룹 멤버 삭제

        # 그룹 멤버 수 확인
        remaining_members_count = GroupMember.objects.filter(group_id=group).count()
        group_deleted = False
        if remaining_members_count == 0:
            group.delete()  # 그룹 삭제
            group_deleted = True

        # 통일된 응답 반환
        return Response({
            "success": True,
            "message": "그룹에서 성공적으로 탈퇴했습니다.",
            "deleted": group_deleted
        }, status=status.HTTP_200_OK)



class GroupTopRankingView(APIView):
    """
    상위 10개 그룹 랭킹을 조회하는 API 뷰

    total_points를 기준으로 상위 10개 그룹 랭킹을 조회합니다.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="상위 10개 그룹 랭킹을 조회",
        responses={
            200: openapi.Response(
                description="성공",
                examples={
                    "application/json": [
                        {
                            "rank": 1,
                            "group_name": "Health Enthusiasts",
                            "total_points": 10000,
                            "updated_at": "2024-12-09T12:34:56Z"
                        }
                    ]
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        # total_points 기준으로 내림차순 정렬 후 상위 10개 가져오기
        rankings = GroupRanking.objects.all().order_by('-total_points')[:10]

        # 순위를 계산하여 결과에 추가
        ranking_data = []
        for index, ranking in enumerate(rankings, start=1):
            data = {
                "rank": index,
                "group_name": ranking.group_id.name,
                "total_points": ranking.total_points,
                "updated_at": ranking.updated_at,
            }
            ranking_data.append(data)

        return Response(ranking_data, status=status.HTTP_200_OK)
    
class UpdatePublicInfoView(generics.UpdateAPIView):
    """
    그룹 멤버의 정보 공개 여부를 수정하는 API 뷰
    
    그룹 멤버의 정보 공개 여부를 수정합니다.
    """
    queryset = GroupMember.objects.all()
    serializer_class = PublicInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        그룹 멤버 객체를 가져옵니다.
        """
        group_id = self.kwargs.get('group_id')
        try:
            return GroupMember.objects.get(user_id=self.request.user, group_id=group_id)
        except GroupMember.DoesNotExist:
            raise ValidationError({"detail": "가입하지 않은 그룹입니다."})

    def update(self, request, *args, **kwargs):
        """
        정보 공개 여부를 수정하고 통일된 형식으로 응답합니다.
        """
        try:
            is_public = request.data.get('is_public')
            if is_public is None:
                raise ValidationError({"is_public": "필수 항목입니다."})

            # 멤버 객체 가져오기
            group_member = self.get_object()
            
            # 정보 공개 여부 업데이트
            group_member.is_public = is_public
            group_member.save()

            return Response({
                "success": True,
                "message": "정보 공개 여부가 성공적으로 수정되었습니다.",
                "data": {
                    "group_id": group_member.group_id.id,
                    "user_id": group_member.user_id.id,
                    "is_public": group_member.is_public
                }
            }, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({
                "success": False,
                "message": "정보 공개 여부 수정에 실패했습니다.",
                "errors": e.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "success": False,
                "message": "서버에서 오류가 발생했습니다.",
                "errors": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class GroupDetailView(generics.RetrieveAPIView):
    """
    그룹의 상세 정보를 조회하는 API 뷰

    그룹의 상세 정보와 그룹에 등록된 사용자 정보를 조회합니다.
    """
    
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        group_id = self.kwargs.get('pk')
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            raise ValidationError({"detail": "그룹이 존재하지 않습니다.}"})
        
        group_member = GroupMember.objects.filter(group_id=group)
        serializer = GroupMemberSerializer(group_member, many=True)
        
        group_serializer = self.get_serializer(group)
        return Response({
            "group": group_serializer.data
        })
