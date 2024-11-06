from django.urls import path, include
from . import views

urlpatterns = [
    # food_id로 검색할 때
    path('foods/search/id/<int:food_id>/', views.FoodsAPI.as_view(), name='food_search_by_id'),
    # food_name으로 검색할 때
    path('foods/search/name/<str:food_name>/', views.FoodsAPI.as_view(), name='food_search_by_name'),
]
