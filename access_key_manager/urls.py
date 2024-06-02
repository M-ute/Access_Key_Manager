
from django.contrib import admin
from django.urls import path, include
from keysManager.views import register, user_login, user_logout, home
from keysManager import views




urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('keysManager/', include('keysManager.urls')), 
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'), # Include key_manager app URLs
    #path('', views.root_view, name='root'),

]


