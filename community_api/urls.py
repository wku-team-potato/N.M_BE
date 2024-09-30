from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'post', views.PostAPI)
router.register(r'comment', views.CommentAPI)

urlpatterns = [
    path('', include(router.urls))
]