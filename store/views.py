from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
from profile.models import Profile
from .models import Item
from .models import PurchaseRecord
from .serializers import ItemSerializer
from .serializers import PurchaseRecordSerializer
from .serializers import ItemBuySerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from .services import purchase_item
from point.services import InsufficientPointsException
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ItemBuyView(APIView):
    """
    아이템 구매 API
    
    URL path parameter로 받은 id로 아이템을 구매합니다.
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        try:
            # get_object_or_404 사용하여 아이템 조회
            item = get_object_or_404(Item, id=id)
            user_profile = Profile.objects.get(user_id=request.user.id)
            
            # 아이템 구매 처리
            purchase_item(request.user, item)
            
            response_data = {
                "message": "아이템 구매가 완료되었습니다.",
                "remaining_points": user_profile.total_points,
                "item": ItemSerializer(item).data
            }
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Profile.DoesNotExist:
            return Response(
                {"message": "사용자 프로필을 찾을 수 없습니다."}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except InsufficientPointsException:
            return Response(
                {"message": "포인트가 부족합니다."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": f"구매 처리 중 오류가 발생했습니다: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
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