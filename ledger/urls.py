from django.urls import path
from .views import index, list, recipe1, recipe2

urlpatterns = [
    path('recipes/list', list, name='list'),
    path('recipe/1', recipe1, name='recipe1'),
    path('recipe/2', recipe2, name='recipe2'),
]
app_name = "ledger"