| File/Folder       | Purpose                                                                              |
| ----------------- | ------------------------------------------------------------------------------------ |
| main.py           | Fetches daily IBM stock data from Alpha Vantage API and saves as JSON indata/folder. |
| convert_to_csv.py | Converts the raw JSON file into a clean CSV file for analysis.                       |
| upload_to_s3.py   | Uploads the generated CSV file to your AWS S3 bucket.                                |
| data/             | Stores data files (IBM_daily.json,IBM_daily.csv).                                    |
| .env              | Stores your (private!) Alpha Vantage API key.Not committed to GitHub.                |
| README.md         | Explains project setup, file purposes, and AWS integration steps.                    |

How to Run the Project
Set up your API key:

Create a .env file and add:
ALPHAVANTAGE_API_KEY=your_key_here

Install dependencies:

text
pip install requests python-dotenv boto3
Fetch IBM stock data (main.py):

text
python main.py
Saves IBM_daily.json in data/

Convert to CSV (convert_to_csv.py):

text
python convert_to_csv.py
Creates IBM_daily.csv in data/

Upload CSV to AWS S3 (upload_to_s3.py):

Make sure you’ve run aws configure and set up your IAM user.

text
python upload_to_s3.py
Uploads CSV to your S3 bucket in stock_data/ folder.

AWS Steps
Instructions for S3 bucket, IAM, Glue Crawler, Athena setup (see guide above).

Notes
Do not upload .env or credentials to GitHub.

AWS resources are described in this README for reference; not hosted in the code.

For more details, see AWS Setup Guide above.

Extra: Example File Descriptions
main.py

Downloads raw stock data from API.

convert_to_csv.py

Transforms API data (JSON) into CSV for data analysis or later processing.

upload_to_s3.py

Moves processed data to AWS cloud for team access and next steps.