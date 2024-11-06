from django.forms import ValidationError
from rest_framework import generics

from .models import Foods
from .serializers import FoodSerializer
from django.db.models import Q
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class FoodsAPI(generics.ListAPIView):
    """
    음식 검색을 위한 API 뷰
    """
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # queryset을 초기화
        queryset = Foods.objects.all()
        
        # URL 경로 파라미터에서 food_id와 food_name을 가져옴
        food_id = self.kwargs.get('food_id')
        food_name = self.kwargs.get('food_name')

        # food_id로 검색할 때
        if food_id:
            queryset = queryset.filter(food_id=food_id)

        # food_name으로 검색할 때
        elif food_name:
            queryset = queryset.filter(Q(food_name__icontains=food_name))

        # 둘 다 없으면 ValidationError 반환
        else:
            raise ValidationError('Please provide either food_id or food_name')

        return queryset
        
# class FoodsAPI(APIView):
#     def get(self, request):
        
#         food_code = request.query_params.get('food_code', '')
#         food_name = request.query_params.get('food_name', '')
        
#         if food_code and food_name:
#             return Response({'error': 'Please provide either food_code or food_name'}, status=400)
        
#         queryset = Foods.objects.all()
        
#         if food_name:
#             queryset = queryset.filter(Q(food_name__icontains=food_name))
#         elif food_code:
#             queryset = queryset.filter(Q(food_code__icontains=food_code))
#         else:
#             return Response({'error': 'Please provide either food_code or food_name'}, status=400)
        
#         serializer = FoodSerializer(queryset, many=True)
#         return Response(serializer.data)