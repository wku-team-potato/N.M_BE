from rest_framework import serializers
from .models import Group, GroupMember, GroupRanking

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ['id', 'creator', 'created_at', 'updated_at']
    
class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = '__all__'
        read_only_fields = ['id', 'user_id', 'is_admin', 'created_at', 'updated_at']
        
class GroupRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupRanking
        fields = '__all__'
        read_only_fields = ['id', 'group_id', 'updated_at']

class PublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = ['is_public']

class GroupDetailSerializer(serializers.ModelSerializer):
    """
    그룹의 상세 정보를 직렬화하는 Serializer
    """
    members = GroupMemberSerializer(source='groupmember_set', many=True)  # 그룹 멤버 정보 포함

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'creator', 'created_at', 'updated_at', 'members']