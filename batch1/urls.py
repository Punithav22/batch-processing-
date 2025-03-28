
from django.urls import path
from . import views  # Import views
from .views import bulk_delete  # ✅ Import bulk delete function

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('insert/', views.insert_row, name='insert_row'),
    path('edit/<int:id>/', views.edit_row, name='edit_row'),
    path('delete/<int:id>/', views.delete_row, name='delete_row'),
    path('download/', views.download_csv, name='download_csv'),  # ✅ Added this line
    path('bulk_delete/', bulk_delete, name='bulk_delete'),  # ✅ Fixed the reference
]
