from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name="Hello Page"),
    path('add', views.add_numbers, name="Result")
]
