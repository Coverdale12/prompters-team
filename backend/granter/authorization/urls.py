from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.auth_view, name='login'),
]