from django.urls import path, include
from . import views

urlpatterns = [
    # 아이템 구매
    path("items/<int:id>/buy/", views.ItemBuyView.as_view(), name="item-buy"),
    # 아이템 조회
    path("items/<int:id>/", views.ItemRetrieveView.as_view(), name="item-retrieve"),
    # 아이템 목록 조회
    path("items/list/", views.ItemListView.as_view(), name="item-list"),
    # 구매 기록 조회
    # path("purchase-records/<int:id>/", views.PurchaseRecordListView.as_view(), name="purchase-record-list"),
    path("purchaserecords/", views.PurchaseRecord_ListView.as_view(), name="purchase-record-list"),

    # ############ Not Using ############
    # 아이템 생성
    path("items/create/", views.ItemCreateView.as_view(), name="item-create"),
]