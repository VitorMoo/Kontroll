from django.urls import path
from .views import UserRegisterView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
