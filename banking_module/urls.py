from django.urls import path
from .views import register, home, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', home, name='home'),
]
