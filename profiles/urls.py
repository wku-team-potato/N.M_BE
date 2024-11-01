from django.urls import path, include
from . import views

urlpatterns = [
    path('update/<int:user_id_id>/', views.ProfileUpdateView.as_view(), name='update_profile'),
]
