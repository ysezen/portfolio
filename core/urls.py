from django.urls import path
from .views import index, redirect_url,submit_contact_form

urlpatterns = [
    path('', index, name='index'),
    path('submit_contact_form', submit_contact_form, name='submit_contact_form'),
    path('<slug_parameter>/', redirect_url, name='redirect_url'),
]