from rest_framework import routers
from ingredients import views as ingredients_views

router = routers.DefaultRouter()
router.register(r'category', ingredients_views.CategoryViewset)
router.register(r'ingredient', ingredients_views.IngredientViewset)