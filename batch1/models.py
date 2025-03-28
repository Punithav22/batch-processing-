from django.db import models

# Function to get upload path (optional if not needed)
def get_upload_to(instance, filename):
    return f'uploads/{filename}'

# Model for Uploaded Files
class UploadedFile(models.Model):
    file = models.FileField(upload_to=get_upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File uploaded at {self.uploaded_at}"

# Primary Model for CSV Data
class CsvData(models.Model):
    field1 = models.CharField(max_length=255, verbose_name="Field One", default='')
    field2 = models.CharField(max_length=255, verbose_name="Field Two", default='')
    field3 = models.CharField(max_length=255, verbose_name="Field Three", default='')
  

    def __str__(self):
        return f"{self.field1} - {self.field2} - {self.field3} "

# Optional: Another Model with More Details
class DetailedData(models.Model):  
    field1 = models.CharField(max_length=255, default='')
    field2 = models.CharField(max_length=255, default='')
    field3 = models.CharField(max_length=255, default='')
   
    name = models.CharField(max_length=255, verbose_name="Full Name")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.name} - {self.field1}"





