from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse
import csv

from .forms import FileUploadForm, CsvDataForm
from .models import CsvData

# Bulk Delete View
def bulk_delete(request):
    if request.method == 'POST':
        # Convert comma-separated string to a list of integers
        selected_ids = request.POST.get('selected_ids', '').split(',')
        selected_ids = [int(id) for id in selected_ids if id.isdigit()]  # Ensure only integers are passed

        if selected_ids:
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
        file_path = fs.path(filename)

        # Parse the CSV file
        data = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)

        # Store the data into session
        request.session['uploaded_data'] = data
        return redirect('upload_success')

    return render(request, 'upload.html')





# Upload Success View with Pagination
def upload_success(request):
    # Load data from session or DB
    data = request.session.get('uploaded_data', None)
    if data:
        # Skip header row and save data
        for row in data[1:]:
            if len(row) >= 3:
                CsvData.objects.update_or_create(
                    field1=row[0],
                    field2=row[1],
                    field3=row[2]
                )
        # Clear session after saving
        request.session.pop('uploaded_data', None)

    # Paginate saved CSV data
    csv_data = CsvData.objects.all()
    paginator = Paginator(csv_data, 10)  # 10 rows per page
    page = request.GET.get('page')
    csv_data = paginator.get_page(page)

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


# Edit Row View — keeps the current page
def edit_row(request, id):
    row = get_object_or_404(CsvData, id=id)

    if request.method == 'POST':
        form = CsvDataForm(request.POST, instance=row)
        if form.is_valid():
            form.save()
            page = request.GET.get('page', 1)
            return redirect(f'{reverse("upload_success")}?page={page}')
    else:
        form = CsvDataForm(instance=row)

    return render(request, 'edit_row.html', {'form': form, 'row': row})


# Delete Row View — keeps the current page
def delete_row(request, id):
    row = get_object_or_404(CsvData, id=id)
    row.delete()
    page = request.GET.get('page', 1)
    return redirect(f'{reverse("upload_success")}?page={page}')


# CSV Download View
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Field1', 'Field2', 'Field3'])  # CSV headers

    for row in CsvData.objects.all():
        writer.writerow([row.field1, row.field2, row.field3])

    return response