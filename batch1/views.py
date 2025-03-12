from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
import csv
from .forms import FileUploadForm, CsvDataForm
from .models import CsvData
from django.http import HttpResponse


def bulk_delete(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        CsvData.objects.filter(id__in=selected_ids).delete()
    return redirect('upload_success')







# File Upload View
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']

        # Check if the uploaded file is CSV
        if not file.name.endswith('.csv'):
            return render(request, 'upload.html', {'error': 'Only CSV files are allowed.'})

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_path = fs.path(filename)  # Get the actual file system path

        # Parse the CSV file
        data = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:  # Ensure UTF-8 encoding
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)

        # Store the data into session
        request.session['uploaded_data'] = data
        return redirect('upload_success')

    return render(request, 'upload.html')

# Upload Success View
def upload_success(request):
    data = request.session.get('uploaded_data', None)
    if not data:
        return redirect('upload_file')

    # Skip header row if needed
    for row in data[1:]:
        if len(row) >= 10:  # Ensure row has at least 10 columns
            CsvData.objects.update_or_create(
                field1=row[0],
                 field2=row[1],
                  field3=row[2] 
                
            )

    csv_data = CsvData.objects.all()

    # Clear session data after successfully saving
    request.session.pop('uploaded_data', None)

    return render(request, 'upload_success.html', {'data': csv_data})

# Insert Row View
def insert_row(request):
    if request.method == 'POST':
        form = CsvDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = CsvDataForm()

    return render(request, 'insert_row.html', {'form': form})

# Edit Row View
def edit_row(request, id):
    row = get_object_or_404(CsvData, id=id)

    if request.method == 'POST':
        form = CsvDataForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = CsvDataForm(instance=row)

    return render(request, 'edit_row.html', {'form': form, 'row': row})
from django.http import JsonResponse
import json
from .models import CsvData



# Delete Row View
def delete_row(request, id):
    row = get_object_or_404(CsvData, id=id)
    row.delete()
    return redirect('upload_success')




# CSV Download View (Export all 10 fields)
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Field1', 'Field2', 'Field3'])  # CSV headers

    for row in CsvData.objects.all():
        writer.writerow([row.field1, row.field2, row.field3])

    return response

