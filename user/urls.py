from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="SignUp"),
    path("login/", views.Login.as_view(), name="Login"),
    path("logout/", views.Logout.as_view(), name="Logout"),
]
