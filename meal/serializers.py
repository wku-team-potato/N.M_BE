from rest_framework import serializers
from .models import UserMeal
from nutrition.models import Foods

class UserMealSerializer(serializers.ModelSerializer):
    # food_id는 외래 키로 입력받기
    food_id = serializers.PrimaryKeyRelatedField(queryset=Foods.objects.all(), source='food')

    class Meta:
        model = UserMeal
        fields = ['id', 'user_id', 'food_id', 'serving_size', 'meal_type', 'date', 'created_at']
        read_only_fields = ['id',   'user_id', 'created_at']

    def create(self, validated_data):
        # user 필드를 현재 요청한 사용자로 설정
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
class StreakSerializer(serializers.Serializer):
    streak = serializers.IntegerField()
    
class MealSummarySerializer(serializers.Serializer):
    calorie = serializers.FloatField()
    carbohydrate = serializers.FloatField()
    protein = serializers.FloatField()
    fat = serializers.FloatField()

class MealFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ['food_name', 'serving_size', 'energy', 'carbohydrate', 'protein', 'fat']
        read_only_fields = []

class UserMealDetailSerializer(serializers.ModelSerializer):
    # food_id는 외래 키로 입력받기
    food_id = serializers.PrimaryKeyRelatedField(queryset=Foods.objects.all(), source='food')
    food = MealFoodSerializer(read_only=True)  # 조회 시 food 세부 정보 포함
    
    class Meta:
        model = UserMeal
        fields = ['id', 'user_id', 'food_id', 'food', 'serving_size', 'meal_type', 'date', 'created_at']
        read_only_fields = ['id', 'user_id', 'created_at']

