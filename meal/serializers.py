from rest_framework import serializers
from .models import UserMeal

class UserMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMeal
        fields = ['user_meal_id', 'user_id', 'food_id', 'meal_type', 'date']