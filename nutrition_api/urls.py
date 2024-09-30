from django.urls import path, include
from . import views

urlpatterns = [
    path('search', views.FoodsAPI.as_view(), name='food_search_api'),
]