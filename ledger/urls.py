from django.urls import path
from .views import index, list, recipe1, recipe2

urlpatterns = [
    path('recipes/list', list, name='list'),
    path('recipe/<int:pk>', recipe1, name='recipe<int:pk>'),
]
app_name = "ledger"