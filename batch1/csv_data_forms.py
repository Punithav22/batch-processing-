# # csv_data_forms.py
# from django import forms
# from myapp.models import CsvData  # Import model here

# class CsvDataForm(forms.ModelForm):
#     class Meta:
#         model = CsvData  # Link form to model
#         fields = ['field1', 'field2', 'field3']  # Add model fields



from django import forms
from batch1.models import CsvData  # Replace 'batch1' with your actual app name

class CsvDataForm(forms.ModelForm):
    class Meta:
        model = CsvData  # Link form to model
        fields = ['field1', 'field2', 'field3']  # Add model fields
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter field1'}),
            'field2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter field2'}),
            'field3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter field3'}),
            
            
        }
