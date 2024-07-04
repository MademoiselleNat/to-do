from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.customLogin.as_view(), name = 'login'),
    path('signup/', views.SignupView.as_view(), name = 'signup'),
]

