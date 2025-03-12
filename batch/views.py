
import logging
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import ProcessedData
from .utils import process_uploaded_file

logger = logging.getLogger(__name__)

import pandas as pd
from .models import ProcessedData

def process_uploaded_file(file):
    try:
        df = pd.read_csv(file)  # Read CSV file

        required_columns = {"name", "email", "age"}
        if not required_columns.issubset(df.columns):
            return False  # Stop processing if required columns are missing

        df.dropna(inplace=True)  # Remove empty rows
        df.drop_duplicates(subset=["email"], inplace=True)  # Remove duplicates in file

        # Get existing emails from database
        existing_emails = set(ProcessedData.objects.values_list("email", flat=True))

        new_records = []
        for _, row in df.iterrows():
            if row["email"] in existing_emails:
                # Update existing record
                ProcessedData.objects.filter(email=row["email"]).update(
                    name=row["name"], age=row["age"]
                )
            else:
                # Add new record for bulk insert
                new_records.append(ProcessedData(
                    name=row["name"], email=row["email"], age=row["age"]
                ))

        # Bulk insert new records
        if new_records:
            ProcessedData.objects.bulk_create(new_records, ignore_conflicts=True)

        return True
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            if process_uploaded_file(file):
                messages.success(request, "File processed successfully!")
            else:
                messages.error(request, "File format error!")
            return redirect("data_list")
    else:
        form = FileUploadForm()
    return render(request, "batch_upload.html", {"form": form})

def data_list(request):
    data = ProcessedData.objects.all()
    return render(request, "batch_status.html", {"data": data})

def export_data(request):
    data = list(ProcessedData.objects.values("name", "email", "age"))
    df = pd.DataFrame(data)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="processed_data.csv"'
    df.to_csv(response, index=False)
    
    return response


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import ProcessedData
# import pandas as pd
# from django.http import HttpResponse
# from .forms import FileUploadForm  # Ensure you have a form for file upload

# # 🚀 File Upload and Processing
# def upload_file(request):
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES["file"]  # Get the uploaded file
#             df = pd.read_csv(file)  # Read CSV into Pandas DataFrame

#             # Ensure column names match Django model fields
#             df.columns = [
#                 "pregnancies", "glucose", "blood_pressure", "skin_thickness", 
#                 "insulin", "bmi", "diabetes_pedigree_function", "age", "outcome"
#             ]

#             # Convert DataFrame rows into Django model instances
#             ProcessedData.objects.all().delete()  # Optional: Clear previous data
#             records = [
#                 ProcessedData(**row.to_dict()) for _, row in df.iterrows()
#             ]
#             ProcessedData.objects.bulk_create(records)  # Efficient batch insert

#             messages.success(request, "File uploaded and processed successfully!")
#             return redirect("data_list")
#     else:
#         form = FileUploadForm()

#     return render(request, "batch_upload.html", {"form": form})

# # 📊 Display Processed Data
# def data_list(request):
#     data = ProcessedData.objects.all()
#     return render(request, "batch_status.html", {"data": data})

# # 📤 Export Data as CSV
# def export_data(request):
#     data = list(ProcessedData.objects.all().values())
    
#     if not data:
#         return HttpResponse("No data available to export.", content_type="text/plain")

#     df = pd.DataFrame(data)

#     response = HttpResponse(content_type="text/csv")
#     response["Content-Disposition"] = 'attachment; filename="processed_diabetes.csv"'
    
#     df.to_csv(response, index=False)
#     return response
