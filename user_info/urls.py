from django.urls import path
from .views import home, register, user_login

urlpatterns = [
    path('', home, name='home'),
    path('accounts/register/', register, name='register'),
    path('accounts/login/', user_login, name='login'),
]
