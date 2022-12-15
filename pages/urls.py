from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'pages'

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('faq/', views.FaqView.as_view(), name='faq'),
]