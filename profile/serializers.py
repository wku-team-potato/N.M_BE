from rest_framework import serializers
from .models import Profile
from .models import HeightWeightRecord


class UserNameSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - Profile 모델의 user_id, username을 가져오는 serializer
    """
    class Meta:
        model = Profile
        fields = ['user_id', 'username']
        
class UserHeightWeightSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - Profile 모델의 user_id, height, weight를 가져오는 serializer
    """
    class Meta:
        model = Profile
        fields = ['user_id', 'height', 'weight']

class UserNameHeightWeightSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - Profile 모델의 user_id, username, height, weight를 가져오는 serializer
    """
    class Meta:
        model = Profile
        fields = ['user_id', 'username', 'height', 'weight']

class UserTotalPointsSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - Profile 모델의 user_id, total_points를 가져오는 serializer
    """
    class Meta:
        model = Profile
        fields = ['user_id', 'total_points']


class UserProfileSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - Profile 모델의 user_id, username, total_points, height, weight를 가져오는 serializer
    """
    class Meta:
        model = Profile
        fields = ['user_id', 'username', 'total_points', 'height', 'weight']


class HeightWeightRecordSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - HeightWeightRecord 모델의 user_id, height, weight, created_at를 가져오는 serializer
    """
    
    username = serializers.SerializerMethodField()
    
    class Meta:
        model = HeightWeightRecord
        fields = ['user_id', 'username', 'height', 'weight', 'created_at']
        
    def get_username(self, obj):
        return obj.user.username if obj.user else None

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'consecutive_attendance_days', 'cumulative_attendance_days',
                'consecutive_goals_achieved', 'cumulative_goals_achieved']

        


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['user_id', 'height', 'weight', 'created_at', 'updated_at']

# class ProfileRecordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProfileRecord
#         fields = ['user_profile_record_id', 'user_id', 'height', 'weight', 'recorded_at']


# class HeightWeightSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['height', 'weight']

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