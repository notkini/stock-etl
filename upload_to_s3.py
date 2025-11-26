import boto3

# === Change this to your S3 bucket name ===
BUCKET_NAME = "kini-stock-etl-bucket"  # <-- replace with your bucket name

# Path to your CSV file
FILE_NAME = "data/IBM_daily.csv"

# What you want to call it in the S3 bucket inside a folder (key)
S3_KEY = "stock_data/IBM_daily.csv"

# Set up the S3 client
s3 = boto3.client('s3')

# Upload the file
s3.upload_file(FILE_NAME, BUCKET_NAME, S3_KEY)

print(f"Uploaded {FILE_NAME} to s3://{BUCKET_NAME}/{S3_KEY}")
