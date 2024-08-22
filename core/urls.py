from django.urls import path
from .views import index, redirect_url

urlpatterns = [
    path('', index, name='index'),
    path('<slug_parameter>/', redirect_url, name='redirect_url'),
]