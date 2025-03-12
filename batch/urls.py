from django.urls import path
from .views import upload_file, data_list, export_data

urlpatterns = [
    path('upload/', upload_file, name="upload_file"),
    path('data/', data_list, name="data_list"),
    path('export/', export_data, name="export_data"),
]

