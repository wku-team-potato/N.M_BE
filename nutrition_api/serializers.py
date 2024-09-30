from rest_framework import serializers
from .models import Foods

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['food_name', 'representative_food_name', 'serving_size', 'energy', 'moisture', 
                    'protein', 'fat', 'ash', 'carbohydrate', 'sugars', 'dietary_fiber', 'calcium', 
                    'iron', 'phosphorus', 'potassium', 'sodium', 'vitamin_a', 'retinol', 'beta_carotene', 
                    'thiamin', 'riboflavin', 'niacin', 'vitamin_c', 'vitamin_d', 'cholesterol', 'saturated_fat', 
                    'trans_fat']