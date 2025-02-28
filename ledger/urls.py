from django.urls import path
from .views import index, list

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', list, name='list'),
]
app_name = "ledger"