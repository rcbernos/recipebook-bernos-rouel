from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>/add_image', RecipeDetailView.as_view(), name='recipe-detail'),
]
app_name = "ledger"
