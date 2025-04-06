from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.loginuser, name='login'),
    path('signout', views.signout, name='signout'),
    path('findfriends', views.findfriends, name='findfriends'),
    path('user2', views.user2, name='user2'),

    path('deletefriend/<str:username>', views.deletefriend, name='deletefriend'),
    path('user/<str:username>', views.user, name='user'),
    path('request/<str:username>', views.request, name='request'),
    path('accept/<str:sender>', views.accept, name='accept'),
    path('reject/<str:sender>', views.reject, name='reject'),
    path('message', views.message, name='message'),
]
