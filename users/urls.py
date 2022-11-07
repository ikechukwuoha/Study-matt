
from django.urls import path
from . import views


app_name = 'users'


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('login/', views.loginPage, name='login'),
    
    
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
]