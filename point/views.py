from django.shortcuts import render
from .models import PointTransaction
from .serializers import PointTransactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.

class PointTransactionListView(generics.ListAPIView):
    """__summary__
    description:
        사용자의 포인트 트랜잭션 목록을 조회하는 API 뷰
    """
    queryset = PointTransaction.objects.all()
    serializer_class = PointTransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PointTransaction.objects.filter(user=user).order_by('-created_at')