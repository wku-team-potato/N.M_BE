from django.shortcuts import render

from .models import Foods
from .serializers import FoodSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

class FoodsAPI(APIView):
    def get(self, request):
        
        food_code = request.query_params.get('food_code', '')
        food_name = request.query_params.get('food_name', '')
        
        if food_code and food_name:
            return Response({'error': 'Please provide either food_code or food_name'}, status=400)
        
        queryset = Foods.objects.all()
        
        if food_name:
            queryset = queryset.filter(Q(food_name__icontains=food_name))
        elif food_code:
            queryset = queryset.filter(Q(food_code__icontains=food_code))
        else:
            return Response({'error': 'Please provide either food_code or food_name'}, status=400)
        
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)