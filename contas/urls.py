# contas/urls.py
from django.urls import path
from .views import RegisterView, LoginView  # <-- Importa as novas classes

urlpatterns = [
    # Conecta a URL 'register/' à classe RegisterView
    path('register/', RegisterView.as_view(), name='register'), 

    # Conecta a URL 'login/' à classe LoginView
    path('login/', LoginView.as_view(), name='login'),
]