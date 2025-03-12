# import pandas as pd
# from .models import ProcessedData

# def process_uploaded_file(file):
#     try:
#         df = pd.read_csv(file)  # Read CSV file

#         required_columns = {"name", "email", "age"}
#         if not required_columns.issubset(df.columns):
#             return False  # Stop processing if required columns are missing

#         df.dropna(inplace=True)  # Remove empty rows
#         df.drop_duplicates(subset=["email"], inplace=True)  # Remove duplicates in file

#         # Get existing emails from database
#         existing_emails = set(ProcessedData.objects.values_list("email", flat=True))

#         new_records = []
#         for _, row in df.iterrows():
#             if row["email"] in existing_emails:
#                 # Update existing record
#                 ProcessedData.objects.filter(email=row["email"]).update(
#                     name=row["name"], age=row["age"]
#                 )
#             else:
#                 # Add new record for bulk insert
#                 new_records.append(ProcessedData(
#                     name=row["name"], email=row["email"], age=row["age"]
#                 ))

#         # Bulk insert new records
#         if new_records:
#             ProcessedData.objects.bulk_create(new_records, ignore_conflicts=True)

#         return True
#     except Exception as e:
#         print(f"Error processing file: {e}")
#         return False


import pandas as pd
from django.db import transaction
from .models import ProcessedData

def process_uploaded_file(file):
    try:
        df = pd.read_csv(file)  # Read CSV file

        required_columns = {"name", "email", "age"}
        if not required_columns.issubset(df.columns):
            return False  # Stop processing if required columns are missing

        df.dropna(inplace=True)  # Remove empty rows
        df.drop_duplicates(subset=["email"], inplace=True)  # Remove duplicates in file

        emails = list(df["email"])  # Extract emails from the file

        # Fetch only emails that already exist in the database
        existing_data = {obj.email: obj for obj in ProcessedData.objects.filter(email__in=emails)}

        new_records = []
        updated_records = []

        for _, row in df.iterrows():
            email = row["email"]
            if email in existing_data:
                # Update existing record
                existing_obj = existing_data[email]
                existing_obj.name = row["name"]
                existing_obj.age = row["age"]
                updated_records.append(existing_obj)
            else:
                # Create new record
                new_records.append(ProcessedData(
                    name=row["name"], email=email, age=row["age"]
                ))

        # Perform bulk insert and bulk update inside a transaction
        with transaction.atomic():
            if new_records:
                ProcessedData.objects.bulk_create(new_records)
            if updated_records:
                ProcessedData.objects.bulk_update(updated_records, ["name", "age"])

        return True
    except Exception as e:
        print(f"Error processing file: {e}")
        return False
