import json
import csv




# Read the raw json file you saved earlier
with open('data/IBM_daily.json') as f:
    data = json.load(f)

# Extract the actual "Time Series (Daily)" dictionary
series = data["Time Series (Daily)"]

# Open a new CSV file to write
with open('data/IBM_daily.csv', 'w', newline='') as csvfile:
    fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for date, values in series.items():
        row = {
            'date': date,
            'open': values['1. open'],
            'high': values['2. high'],
            'low': values['3. low'],
            'close': values['4. close'],
            'volume': values['5. volume']
        }
        writer.writerow(row)

print("CSV file created: data/IBM_daily.csv")
