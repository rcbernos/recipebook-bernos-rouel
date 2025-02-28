from django.urls import path
from .views import index
urlpatterns = [
    path('', index, name='index'),
    path('/recipes/list', index, name='list'),
]
app_name = "ledger"