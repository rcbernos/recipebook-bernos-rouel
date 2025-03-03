from django.urls import path
from .views import index, list

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', list, name='list'),
    path('recipe/1', list, name='list'),
    path('recipe/2', list, name='list'),
]
app_name = "ledger"