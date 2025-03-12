# # from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from .forms import FileUploadForm
# from .models import UploadedFile
# import pandas as pd
# from django.core.files.storage import default_storage

# def upload_file(request):
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('process_files')  # Redirect to processing function
#     else:
#         form = FileUploadForm()
    
#     return render(request, 'upload.html', {'form': form})

    

# def process_files(request):
#     unprocessed_files = UploadedFile.objects.filter(processed=False)

#     for file_obj in unprocessed_files:
#         file_path = file_obj.file.path  # Get file path
#         if file_path.endswith('.csv'):  # Process only CSV files
#             df = pd.read_csv(file_path)  # Read CSV file
#             # Perform your processing logic here
#             print(df.head())  # Example: Print first few rows

#         file_obj.processed = True  # Mark file as processed
#         file_obj.save()
    
#     return render(request, 'process_complete.html')
#     def process_csv(file_path):
#     # Load the CSV
#     df = pd.read_csv(file_path)

#     # Find Missing Values
#     print("Missing Values:\n", df.isnull().sum())

#     # Remove Rows with Missing Values
#     df_cleaned = df.dropna()

#     # Filter: Select Age > 25
#     selected_data = df_cleaned[df_cleaned['age'] > 25]
    
#     print("Filtered Data:\n", selected_data)

# # Example Usage
# process_csv('uploads/sample_data.csv')
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .forms import FileUploadForm
# from .models import UploadedFile
# import pandas as pd
# import os

# def upload_file(request):
#     """Handles file upload and saves to the database"""
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('process_files')  # Redirect to processing
#     else:
#         form = FileUploadForm()
    
#     return render(request, 'upload.html', {'form': form})

# def process_files(request):
#     """Processes uploaded CSV files and prevents reprocessing"""
    
#     unprocessed_files = UploadedFile.objects.filter(processed=False)
#     results = []  # Store messages for UI display

#     for file_obj in unprocessed_files:
#         file_path = file_obj.file.path  

#         if file_path.endswith('.csv'):  
#             try:
#                 df = pd.read_csv(file_path)  # Read CSV file
                
#                 # 🚨 Skip Empty Files
#                 if df.empty:
#                     results.append(f"🚨 {file_obj.file.name} is empty! Skipping...")
#                     file_obj.processed = True  # Mark as processed to avoid repeat
#                     file_obj.save(update_fields=['processed'])
#                     continue

#                 # 🚀 Find Missing Values
#                 missing_values = df.isnull().sum()
#                 if missing_values.sum() == 0:
#                     results.append(f"✅ {file_obj.file.name}: No missing values found!")
#                 else:
#                     df.fillna(method='ffill', inplace=True)  
#                     results.append(f"⚠️ {file_obj.file.name}: Missing values filled.")

#                 # 🚀 Filter Data Only if `age` and `salary` Exist
#                 if 'age' in df.columns and 'salary' in df.columns:
#                     filtered_data = df[(df['age'] > 25) & (df['salary'] > 50000)]
#                     results.append(f"📊 {file_obj.file.name}: {len(filtered_data)} records filtered.")
#                 else:
#                     results.append(f"⚠️ {file_obj.file.name}: 'age' or 'salary' column not found. Skipping filter.")

#                 # 🚀 Save Cleaned File
#                 cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')
#                 df.to_csv(cleaned_file_path, index=False)
#                 results.append(f"✅ Cleaned file saved: {cleaned_file_path}")

#                 # ✅ Mark as Processed to Avoid Reprocessing
#                 file_obj.processed = True  
#                 file_obj.save(update_fields=['processed'])  # Force saving this field only

#             except Exception as e:
#                 results.append(f"❌ Error processing {file_obj.file.name}: {str(e)}")

#     return render(request, 'process_complete.html', {"results": results})

# def export_processed_data(request, file_id):
#     """Exports the processed CSV file for download"""
#     try:
#         file_obj = UploadedFile.objects.get(id=file_id, processed=True)  # Get only processed files
#         cleaned_file_path = file_obj.file.path.replace('.csv', '_cleaned.csv')

#         if not os.path.exists(cleaned_file_path):
#             return HttpResponse("Processed file not found!", status=404)

#         # Read processed CSV
#         df = pd.read_csv(cleaned_file_path)

#         # Create HTTP response for CSV download
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(cleaned_file_path)}"'
#         df.to_csv(response, index=False)
#         return response

#     except UploadedFile.DoesNotExist:
#         return HttpResponse("File not found or not processed yet.", status=404)

# from django.shortcuts import render, redirect
# from .forms import FileUploadForm
# from .models import UploadedFile
# import pandas as pd
# import os
# import csv
# from django.http import HttpResponse
# from .models import ProcessedData

# def upload_file(request):
#     """Handles file upload and saves to the database"""
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('process_files')  # Redirect to processing
#     else:
#         form = FileUploadForm()
    
#     return render(request, 'upload.html', {'form': form})

# def process_files(request):
#     """Processes uploaded CSV files and prevents reprocessing"""
#     processed_files = UploadedFile.objects.filter(processed=True)  # Get processed files
#     return render(request, 'process_complete.html', {"processed_files": processed_files})

# def export_processed_data(request, file_id):
#     """Exports the processed CSV file for download"""
#     try:
#         file_obj = UploadedFile.objects.get(id=file_id, processed=True)
#         cleaned_file_path = file_obj.file.path.replace('.csv', '_cleaned.csv')

#         if not os.path.exists(cleaned_file_path):
#             return HttpResponse("Processed file not found!", status=404)

#         df = pd.read_csv(cleaned_file_path)

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = f'attachment; filename="{os.path.basename(cleaned_file_path)}"'
#         df.to_csv(response, index=False)
#         return response

#     except UploadedFile.DoesNotExist:
#         return HttpResponse("File not found or not processed yet.", status=404)

#         def export_to_csv(request):
#     # Define the HTTP response with CSV content type
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="processed_data.csv"'

#     # Create a CSV writer
#     writer = csv.writer(response)
    
#     # Write the header row
#     writer.writerow(['Name', 'Gender', 'Age'])

#     # Fetch data from the database and write to CSV
#     for record in ProcessedData.objects.all():
#         writer.writerow([record.name, record.gender, record.age])

#     return response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import UploadedFile, ProcessedData
import pandas as pd
import os
import csv

def upload_file(request):
    """Handles file upload and saves to the database"""
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('process_files')  # Redirect to processing
    else:
        form = FileUploadForm()
    
    return render(request, 'upload.html', {'form': form})

def process_files(request):
    """Processes uploaded CSV files and prevents reprocessing"""
    processed_files = UploadedFile.objects.filter(processed=True)  # Get processed files
    return render(request, 'process_complete.html', {"processed_files": processed_files})

def export_processed_data(request, file_id):
    """Exports the processed CSV file for download"""
    try:
        file_obj = UploadedFile.objects.get(id=file_id, processed=True)
        cleaned_file_path = file_obj.file.path.replace('.csv', '_cleaned.csv')

        if not os.path.exists(cleaned_file_path):
            return HttpResponse("Processed file not found!", status=404)

        df = pd.read_csv(cleaned_file_path)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(cleaned_file_path)}"'
        df.to_csv(response, index=False)
        return response

    except UploadedFile.DoesNotExist:
        return HttpResponse("File not found or not processed yet.", status=404)

def export_to_csv(request):
    """Exports all processed data from the database to a CSV file"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="processed_data.csv"'

    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['Name', 'Gender', 'Age'])

    # Fetch data from the database and write to CSV
    for record in ProcessedData.objects.all():
        writer.writerow([record.name, record.gender, record.age])

    return response
