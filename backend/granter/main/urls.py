from django.urls import path
from . import views

urlpatterns = [
    path('startups/', views.startups_view, name='startups'),
]
