from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user_id_id'

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