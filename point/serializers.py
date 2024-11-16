from rest_framework import serializers
from .models import PointTransaction

class PointTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointTransaction
        fields = ['id', 'user_id', 'points_changed', 'transaction_type', 'description', 'created_at']
        read_only_fields = ['id', 'user_id', 'created_at']