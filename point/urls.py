from django.urls import path, include
from . import views

urlpatterns = [
    path('transaction/', views.PointTransactionListView.as_view(), name='transaction-list'),
]
