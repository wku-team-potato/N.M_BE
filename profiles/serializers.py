from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['height', 'weight']

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['user_profile_id', 'user_id', 'birthday', 'created_at', 'updated_at']

# class WeightRecordSerializer(serializers.ModelSerializer):
#     weight_difference = serializers.SerializerMethodField()
#     date = serializers.DateField(source='recorded_at', format='%Y-%m-%d')
    
#     class Meta:
#         model = WeightRecord
#         fields = ['date', 'height', 'weight', 'created_at']
    
#     def get_weight_difference(self, obj):
#         return obj.get_weight_difference()