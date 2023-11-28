from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_text, name='submit_text'),
]
