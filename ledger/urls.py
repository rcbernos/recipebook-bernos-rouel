from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeAddView, ImageAddView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeAddView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image', ImageAddView.as_view(), name='image-add'),
]
app_name = "ledger"
