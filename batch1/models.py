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





# from django.db import models

# # Function to get upload path (optional if not needed)
# def get_upload_to(instance, filename):
#     return f'uploads/{filename}'

# # Model for Uploaded Files
# class UploadedFile(models.Model):
#     file = models.FileField(upload_to=get_upload_to)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"File uploaded at {self.uploaded_at}"

# # Primary Model for CSV Data
# class CsvData(models.Model):
#     field1 = models.CharField(max_length=255, verbose_name="Field One")
#     field2 = models.CharField(max_length=255, verbose_name="Field Two")
#     field3 = models.CharField(max_length=255, verbose_name="Field Three")
#     field4 = models.CharField(max_length=255, verbose_name="Field four")
#     field5 = models.CharField(max_length=255, verbose_name="Field Five")
#     field6 = models.CharField(max_length=255, verbose_name="Field Six")
#     field7 = models.CharField(max_length=255, verbose_name="Field Seven")
#     field8 = models.CharField(max_length=255, verbose_name="Field eight")
#     field9 = models.CharField(max_length=255, verbose_name="Field Nine")
#     field10 = models.CharField(max_length=255, verbose_name="Field Ten")

#     def __str__(self):
#         return f"{self.field1} - {self.field2} - {self.field3} - {self.field4} - {self.field5} - {self.field6}- {self.field7} - {self.field8} - {self.field9} - {self.field10}"

# # Optional: Another Model with More Details
# class DetailedData(models.Model):  
#     field1 = models.CharField(max_length=255,default='')
#     field2 = models.CharField(max_length=255,default='')
#     field3 = models.CharField(max_length=255,default='')
#     field4 = models.CharField(max_length=255,default='')
#     field5 = models.CharField(max_length=255,default='')
#     field6 = models.CharField(max_length=255,default='')
#     field7 = models.CharField(max_length=255,default='')
#     field8 = models.CharField(max_length=255,default='')
#     field9 = models.CharField(max_length=255,default='')
#     field10 = models.CharField(max_length=255,default='')
#     name = models.CharField(max_length=255, verbose_name="Full Name")
#     description = models.TextField(verbose_name="Description")

#     def __str__(self):
#         return f"{self.name} - {self.field1}"





