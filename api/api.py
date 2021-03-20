from django.urls import (
    include,
    path,
)
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from ingredients import views as ingredients_views

router = routers.DefaultRouter()
router.register(r'category', ingredients_views.CategoryViewSet)
router.register(r'ingredient', ingredients_views.IngredientViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/', include(router.urls)),
    path('swagger/', schema_view, name='swagger'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),


]
