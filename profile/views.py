from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .models import HeightWeightRecord
from .serializers import UserNameSerializer
from .serializers import UserProfileSerializer
from .serializers import UserHeightWeightSerializer
from .serializers import UserTotalPointsSerializer
from .serializers import HeightWeightRecordSerializer
from .serializers import UserNameHeightWeightSerializer

from rest_framework.response import Response

"""
폐기 : UserNameUpdateView
사유 : url로 user_id를 받는 방식 사용하지 않음
"""
# class UserNameUpdateView(generics.UpdateAPIView):
#     """_summary_
#         description:
#         - Profile 모델의 username을 업데이트하는 APIView
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserNameSerializer
#     lookup_field = 'user_id'

"""
폐기 : UserNameUpdateView
사유 : api 문서 단순화로 인한 삭제
"""
# class UserNameUpdateView(generics.UpdateAPIView):
#     """_summary_
#         description:
#         - Profile 모델의 username을 업데이트하는 APIView
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserNameSerializer
#     permission_classes = [IsAuthenticated]
#     # lookup_field = 'user_id'
    
#     def get_object(self):
#         return Profile.objects.get(user=self.request.user)
    
#     def update(self, request, *args, **kwargs):
#         profile = self.get_object()
        
#         serializer = self.get_serializer(profile, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         response = Response(serializer.data, status=status.HTTP_200_OK)
#         response.data['message'] = 'username이 업데이트 되었습니다.'

#         return response

"""
폐기 : HeightWeightUpdateView
사유 : url로 user_id를 받는 방식 사용하지 않음
"""
# class HeightWeightUpdateView(generics.UpdateAPIView):
#     """_summary_
#         description:
#         - Profile 모델의 height, weight를 업데이트하는 APIView
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserHeightWeightSerializer
#     lookup_field = 'user_id'

class HeightWeightUpdateView(generics.UpdateAPIView):
    """_summary_
        description:
        - Profile 모델의 height, weight를 업데이트하는 APIView
    """
    queryset = Profile.objects.all()
    serializer_class = UserHeightWeightSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.data['message'] = 'height, weight가 업데이트 되었습니다.'

        return response

class UserNameHeightWeightUpdateView(generics.UpdateAPIView):
    """_summary_
        description:
        - Profile 모델의 username, height, weight를 업데이트하는 APIView
    """
    queryset = Profile.objects.all()
    serializer_class = UserNameHeightWeightSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.data['message'] = 'username, height, weight가 업데이트 되었습니다.'

        return response
    
"""
폐기 : UserNameRetrieveView
사유 : api 문서 단순화로 인한 삭제, url로 user_id를 받는 방식 사용하지 않음
"""
# class UserNameRetrieveView(generics.RetrieveAPIView):
#     """_summary_
#         description:
#         - Profile 모델의 user_id, username을 가져오는 APIView
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserNameSerializer
#     lookup_field = 'user_id'

"""
폐기 : UserHeightWeightRetrieveView
사유 : api 문서 단순화로 인한 삭제, url로 user_id를 받는 방식 사용하지 않음
"""
# class UserHeightWeightRetrieveView(generics.RetrieveAPIView):
#     """_summary_
#         description:
#         - Profile 모델의 user_id, height, weight를 가져오는 APIView
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserHeightWeightSerializer
#     lookup_field = 'user_id'

"""
폐기 : UserTotalPointsRetrieveView
사유 : url로 user_id를 받는 방식 사용하지 않음
"""
# class UserTotalPointsRetrieveView(generics.RetrieveAPIView):
#     """_summary_
#         description:
#         - Profile 모델의 user_id, total_points를 가져오는 APIView
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserTotalPointsSerializer
#     lookup_field = 'user_id'

class UserTotalPointsRetrieveView(generics.RetrieveAPIView):
    """_summary_
        description:
        - Profile 모델의 user_id, total_points를 가져오는 APIView
    """
    queryset = Profile.objects.all()
    serializer_class = UserTotalPointsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.data['message'] = 'total_points가 조회되었습니다.'
        
        return response
    
"""
폐기 : UserProfileRetrieveView
사유 : api 문서 단순화로 인한 삭제, url로 user_id를 받는 방식 사용하지 않음
"""
# class UserProfileRetrieveView(generics.RetrieveAPIView):
#     """_summary_
#         description:
#         - Profile 모델의 user_id, username, total_points, height, weight를 가져오는 APIView
#     """
#     queryset = Profile.objects.all()
#     serializer_class = UserProfileSerializer
#     lookup_field = 'user_id'
    
class HeightWeightRecordListView(generics.ListAPIView):
    """_summary_
        description:
        - HeightWeightRecord 모델의 user_id, height, weight, created_at를 가져오는 APIView
    """
    queryset = HeightWeightRecord.objects.all()
    serializer_class = HeightWeightRecordSerializer
    # lookup_field = 'user_id'
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def get_queryset(self):
        user = self.get_object()
        return HeightWeightRecord.objects.filter(user=user).order_by('-created_at')
    
    # def get_queryset(self):
    #     user_id = self.kwargs.get(self.lookup_field)
    #     return HeightWeightRecord.objects.filter(user_id=user_id).order_by('-created_at')

# class ProfileRetrieveView(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'user_id'
    
# class ProfileUpdateView(generics.UpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'user_id'
    
# class ProfileRecordListVIew(generics.ListAPIView):
#     serializer_class = ProfileRecordSerializer
#     lookup_field = 'user_id'
    
#     def get_queryset(self):
#         user_id = self.kwargs.get(self.lookup_field)  # URL에서 user_id를 가져옴
#         return ProfileRecord.objects.filter(user_id=user_id).order_by('-recorded_at')

# class WeightRecordChanges(APIView):
#     def post(self, request):
#         try:
#             user_profile_id = request.data.get('user_profile_id')
#             days = int(request.query_params.get('days', 5))
            
#             records = WeightRecord.get_weight_changes(user_profile_id, days)
            
#             weight_data = []
#             for record in records:
#                 weight_info = {
#                     'date': record.recorded_at.date(),
#                     'height': record.height,
#                     'weight': record.weight,
#                     'difference': record.get_weight_difference()
#                 }
#                 weight_data.append(weight_info)
            
#             total_change = 0
#             if len(weight_data) >= 2:
#                 total_change = weight_data[-1]['weight'] - weight_data[0]['weight']
            
#             response_data = {
#                 'weight_records': weight_data,
#                 'total_days': days,
#                 'total_change': round(total_change, 2),
#                 'average_weight': round(records.aggregate(Avg('weight'))['weight__avg'], 2)
#             }
            
#             return Response(response_data, status=status.HTTP_200_OK)
            
#         except Exception as e:
#             return Response(
#                 {'error': str(e)},
#                 status=status.HTTP_400_BAD_REQUEST
#             )