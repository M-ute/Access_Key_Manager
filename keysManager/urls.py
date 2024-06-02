# keysManager/urls.py

from django.urls import path, include
from keysManager.views import register, user_login, user_logout, home

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    path('password_reset/', include('django.contrib.auth.urls')),
]
