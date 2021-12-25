from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('register/submit', views.submit_registration, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")

]