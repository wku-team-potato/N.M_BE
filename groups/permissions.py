from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import GroupMember

class IsGroupAdmin(BasePermission):
    """
    그룹 관리자 권한 클래스
    """
    def has_object_permission(self, request, view, obj):
        # obj는 Group 인스턴스
        try:
            group_member = GroupMember.objects.get(user_id=request.user, group_id=obj)
            return group_member.is_admin
        except GroupMember.DoesNotExist:
            return False