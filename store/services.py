from point.services import deduct_points
from .models import PurchaseRecord

def purchase_item(user, item, quantity=1):
    """
    상점에서 아이템을 구매하는 함수.
    
    :param user: 아이템을 구매할 사용자
    :param item: 구매할 아이템
    :param quantity: 구매할 수량 (기본값: 1)
    """
    total_price = item.price * quantity
    deduct_points(user, total_price, f"{item.name} 구매")
    # user.profile.items.add(item, through_defaults={"quantity": quantity})
    PurchaseRecord.objects.create(user=user, item=item)
    