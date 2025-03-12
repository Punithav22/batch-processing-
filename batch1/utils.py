# # utils.py
# import pandas as pd
# from .models import ProcessedData

# def process_uploaded_file(file):
#     try:
#         df = pd.read_csv(file)  # Assuming CSV format

#         required_columns = {"name", "email", "age"}
#         if not required_columns.issubset(df.columns):
#             return False  # Missing required columns

#         df.dropna(inplace=True)  # Remove empty rows
#         df.drop_duplicates(subset=["email"], inplace=True)  # Remove duplicate emails

#         for _, row in df.iterrows():
#             ProcessedData.objects.update_or_create(
#                 email=row["email"],
#                 defaults={"name": row["name"], "age": row["age"]}
#             )
#         return True
#     except Exception as e:
#         print(f"Error processing file: {e}")
#         return False
  


import pandas as pd
from .models import ProcessedData

def process_uploaded_file(file):
    try:
        # Read CSV file (ensure correct encoding)
        df = pd.read_csv(file, encoding='utf-8')

        # Normalize column names to avoid issues with spaces or case differences
        df.columns = df.columns.str.strip().str.lower()

        required_columns = {"name", "email", "age"}
        if not required_columns.issubset(df.columns):
            return False  # Missing required columns

        # Clean data
        df.dropna(inplace=True)  # Remove empty rows
        df.drop_duplicates(subset=["email"], inplace=True)  # Remove duplicate emails

        # Insert or update database records
        for _, row in df.iterrows():
            ProcessedData.objects.update_or_create(
                email=row["email"].strip(),
                defaults={"name": row["name"].strip(), "age": int(row["age"])}
            )

        return True
    except Exception as e:
        print(f"Error processing file: {e}")
        return False
