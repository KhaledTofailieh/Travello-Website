from . import views
from django.urls import path

app_name = 'dest-api'

urlpatterns = [
    path('', views.api_destinations_details, name="details"),
    path('<name>', views.api_destination_details, name="detail"),
    path('<name>', views.api_destination_edit, name="edit"),
    path('<name>', views.api_destination_delete, name="delete"),

]