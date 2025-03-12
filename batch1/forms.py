# from django import forms
# from .models import CsvData, UploadedFile

# # Form for uploading files
# class FileUploadForm(forms.ModelForm):
#     class Meta:
#         model = UploadedFile
#         fields = ['file']

# # Form for CSV data model
# class CsvDataForm(forms.ModelForm):
#     class Meta:
#         model = CsvData
#         fields = ['field1', 'field2', 'field3']




from django import forms
from .models import CsvData, UploadedFile

# Form for uploading files
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

# Form for CSV data model
class CsvDataForm(forms.ModelForm):
    class Meta:
        model = CsvData
        fields = ['field1', 'field2', 'field3']
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter field1'}),
            'field2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter field2'}),
            'field3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter field3'}),
             
        }
