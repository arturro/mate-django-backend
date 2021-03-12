from rest_framework import routers
from ingredients import views as ingredients_views

router = routers.DefaultRouter()
router.register(r'category', ingredients_views.CategoryViewSet)
router.register(r'ingredient', ingredients_views.IngredientViewSet)
