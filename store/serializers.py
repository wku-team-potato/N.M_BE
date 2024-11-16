from rest_framework import serializers
from .models import Item
from .models import PurchaseRecord

class ItemSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - Item 모델의 id, name, description, price, img, created_at를 가져오는 serializer
    """
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'img', 'created_at']

class PurchaseRecordSerializer(serializers.ModelSerializer):
    """_summary_
        description:
        - PurchaseRecord 모델의 id, user_id, item_id, created_at를 가져오는 serializer
    """
    class Meta:
        model = PurchaseRecord
        fields = ['id', 'user_id', 'item_id', 'created_at']
        
class ItemBuySerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, default=1)

    class Meta:
        fields = []