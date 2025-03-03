from django.urls import path
from .views import index, list

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', list, name='list'),
    path('recipe/1', recipe1, name='recipe1'),
    path('recipe/2', recipe2, name='recipe2'),
]
app_name = "ledger"