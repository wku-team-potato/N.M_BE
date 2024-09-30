from django.shortcuts import render

from .models import Foods
from .serializers import FoodSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class FoodsAPI(APIView):
    def get(self, request):
        query = request.query_params.get('food_name', '')
        if query:
            foods = Foods.objects.filter(
                Q(food_name__icontains=query) |
                Q(representative_food_name__icontains=query)
            ).distinct()
            serializer = FoodSerializer(foods, many=True)
            return Response(serializer.data)
        
        return Response([], status=200)