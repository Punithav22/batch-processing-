from django.urls import path
from .views import upload_file, process_files, export_processed_data

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('process/', process_files, name='process_files'),
    path('export/<int:file_id>/', export_processed_data, name='export_processed_data'),
     path('export/csv/', export_to_csv, name='export_csv'), 
]
