from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
from profile.models import Profile
from .models import Item
from .models import PurchaseRecord
from .serializers import ItemSerializer
from .serializers import PurchaseRecordSerializer
from .serializers import ItemBuySerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .services import purchase_item
from point.services import InsufficientPointsException
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ItemBuyView(APIView):
    """
    아이템 구매 API
    
    URL path parameter로 받은 id로 아이템을 구매합니다.
    """
    permission_classes = [IsAuthenticated]
    
    
    @swagger_auto_schema(
        operation_summary="아이템 구매",
        operation_description="URL path parameter로 아이템 ID를 받아 구매를 진행합니다.",
        responses={
            200: openapi.Response(
                description="구매 성공",
                examples={
                    "application/json": {
                        "message": "아이템 구매가 완료되었습니다.",
                        "remaining_points": 500,
                        "item": {
                            "id": 1,
                            "name": "Sword of Power",
                            "price": 1000
                        }
                    }
                },
            ),
            400: openapi.Response(
                description="포인트 부족",
                examples={
                    "application/json": {
                        "message": "포인트가 부족합니다."
                    }
                },
            ),
            404: openapi.Response(
                description="사용자 프로필 또는 아이템을 찾을 수 없음",
                examples={
                    "application/json": {
                        "message": "사용자 프로필을 찾을 수 없습니다."
                    }
                },
            ),
            500: openapi.Response(
                description="구매 처리 중 오류 발생",
                examples={
                    "application/json": {
                        "message": "구매 처리 중 오류가 발생했습니다: 오류 메시지"
                    }
                },
            ),
        },
    )
    def post(self, request, id):
        try:
            # get_object_or_404 사용하여 아이템 조회
            item = get_object_or_404(Item, id=id)
            user_profile = Profile.objects.get(user_id=request.user.id)
            
            # 아이템 구매 처리
            purchase_item(request.user, item)
            
            response_data = {
                "message": "아이템 구매가 완료되었습니다.",
                "remaining_points": user_profile.total_points,
                "item": ItemSerializer(item).data
            }
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Profile.DoesNotExist:
            return Response(
                {"message": "사용자 프로필을 찾을 수 없습니다."}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except InsufficientPointsException:
            return Response(
                {"message": "포인트가 부족합니다."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": f"구매 처리 중 오류가 발생했습니다: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ItemRetrieveView(generics.RetrieveAPIView):
    """
    아이템 조회 API
    
    URL path parameter로 받은 id로 Item을 조회합니다.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

class ItemListView(generics.ListCreateAPIView):
    """
    아이템 목록 조회 API
    
    Item 모델의 전체 목록을 조회합니다.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PurchaseRecordListView(generics.ListCreateAPIView):
    """
    # 구매 기록 조회 API
    
    # PurchaseRecord 모델의 전체 목록을 조회합니다.
    """
    
    queryset = PurchaseRecord.objects.all()
    serializer_class = PurchaseRecordSerializer
    lookup_field = 'user_id'
    
class PurchaseRecord_ListView(generics.ListCreateAPIView):
    """
    구매 기록 조회 API
    
    PurchaseRecord 모델의 전체 목록을 조회합니다.
    """
    permission_classes = [IsAuthenticated]
    queryset = PurchaseRecord.objects.all()
    serializer_class = PurchaseRecordSerializer
    
    def get_queryset(self):
        return PurchaseRecord.objects.filter(user=self.request.user).order_by('-created_at')
# ############ Not Using ############

class ItemCreateView(generics.CreateAPIView):
    """
    아이템 생성 API
    
    Item 모델의 id, name, description, price, img, created_at를 생성합니다.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    @swagger_auto_schema(request_body=ItemSerializer)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class ItemUpdateView(generics.UpdateAPIView):
#     """_summary_
#         description:
#         - Item 모델의 id, name, description, price, img, created_at를 업데이트하는 APIView
#     """
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     lookup_field = 'id'

# class ItemDeleteView(generics.DestroyAPIView):
#     """_summary_
#         description:
#         - Item 모델의 id, name, description, price, img, created_at를 삭제하는 APIView
#     """
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     lookup_field = 'id'