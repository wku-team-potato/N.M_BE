from rest_framework import serializers
from .models import Foods

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['food_id', 'food_name', 'serving_size', 'energy', 
                    'carbohydrate', 'sugars', 'fat', 'protein', 'calcium', 
                    'phosphorus', 'sodium', 'potassium', 'magnesium', 'iron', 'zinc', 'cholesterol', 'trans_fat']