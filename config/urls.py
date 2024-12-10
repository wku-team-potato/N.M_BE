from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="API Doument",
        default_version="v1",
        description="API Document for the project",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/v1/auth/", include("user.urls")),
    path("api/v1/profile/", include("profile.urls")),
    # path("api/v1/community/", include("community_api.urls")),
    path("api/v1/nutrition/", include("nutrition.urls")),
    path('api/v1/store/', include('store.urls')),
    path("api/v1/meal/", include("meal.urls")),
    path("api/v1/point/", include("point.urls")),
    path("api/v1/groups/", include("groups.urls")),
    path("api/v1/swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("api/v1/redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
