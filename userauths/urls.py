from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
]