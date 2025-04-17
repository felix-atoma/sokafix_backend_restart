from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.submit_contact),
    path('subscribe/', views.subscribe_newsletter),
    path('messages/', views.list_messages),
]
