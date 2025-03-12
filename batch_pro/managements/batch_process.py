from django.core.management.base import BaseCommand
from myapp.models import UploadedFile
import pandas as pd

class Command(BaseCommand):
    help = "Process uploaded files in batches"

    def handle(self, *args, **kwargs):
        unprocessed_files = UploadedFile.objects.filter(processed=False)
        for file_obj in unprocessed_files:
            file_path = file_obj.file.path
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
                print(df.head())  # Example processing
            
            file_obj.processed = True
            file_obj.save()
        self.stdout.write(self.style.SUCCESS("Batch processing completed!"))
