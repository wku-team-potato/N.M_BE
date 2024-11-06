from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
from profile.models import Profile
from .models import Item
from .models import PurchaseRecord
from .serializers import ItemSerializer
from .serializers import PurchaseRecordSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema

class ItemBuyView(generics.UpdateAPIView):
    """_summary_
        description:
        - Profile의 total_points를 확인하여 아이템 가격과 비교 후 구매 처리
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        item = self.get_object()
        user_id = request.user.id
        
        try:
            user_profile = Profile.objects.get(user_id=user_id)
            
            if user_profile.total_points < item.price:
                return Response(
                    {'message': '포인트가 부족하여 구매할 수 없습니다.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            with transaction.atomic():
                user_profile.total_points -= item.price
                user_profile.save()
                
                PurchaseRecord.objects.create(
                    user_id=request.user.id,
                    item_id=item.id,
                    created_at=timezone.now()
                )
            
            response_data = {
                "message": "아이템 구매가 완료되었습니다.",
                "remaining_points": user_profile.total_points,
                "item": ItemSerializer(item).data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        except Profile.DoesNotExist:
            return Response(
                {'message': '프로필 정보가 없습니다.'},
                status=status.HTTP_404_NOT_FOUND
            )

class ItemRetrieveView(generics.RetrieveAPIView):
    """_summary_
        description:
        - Item 모델의 id, name, description, price, img, created_at를 가져오는 APIView
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

class ItemListView(generics.ListCreateAPIView):
    """_summary_
        description:
        - Item 모델의 id, name, description, price, img, created_at를 가져오는 APIView
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PurchaseRecordListView(generics.ListCreateAPIView):
    """_summary_
        description:
        - PurchaseRecord 모델의 id, user_id, item_id, created_at를 가져오는 APIView
    """
    queryset = PurchaseRecord.objects.all()
    serializer_class = PurchaseRecordSerializer
    lookup_field = 'user_id'

# ############ Not Using ############

class ItemCreateView(generics.CreateAPIView):
    """_summary_
        description:
        - Item 모델의 id, name, description, price, img, created_at를 생성하는 APIView
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    @swagger_auto_schema(request_body=ItemSerializer)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class ItemUpdateView(generics.UpdateAPIView):
#     """_summary_
#         description:
#         - Item 모델의 id, name, description, price, img, created_at를 업데이트하는 APIView
#     """
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     lookup_field = 'id'

# class ItemDeleteView(generics.DestroyAPIView):
#     """_summary_
#         description:
#         - Item 모델의 id, name, description, price, img, created_at를 삭제하는 APIView
#     """
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     lookup_field = 'id'