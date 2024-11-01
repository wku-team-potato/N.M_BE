from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import UserMeal
from .serializers import UserMealSerializer

@api_view(['GET', 'POST'])
def user_meal_list(request):
    if request.method == 'GET':
        meals = UserMeal.objects.all()
        serializer = UserMealSerializer(meals, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserMealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)