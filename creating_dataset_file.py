import csv
import json
# Path to your CSV file
csv_file_path = '"C:\\Users\\hasee\\Desktop\\NCAI internship\\ML Chatbot\Dataset\\Related_dataset.csv"'

# Path to the JSON file you want to create
json_file_path = 'dataset.json'

# Initialize the list to hold dictionary objects
data = []

# Read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile, fieldnames=['prompt', 'completion'])
    next(csvreader)  # Skip the header row if your CSV has one
    for row in csvreader:
        # Append each row as a dictionary to the list
        data.append({
            "prompt": row['prompt'],
            "completion": row['completion']
        })

# Write the JSON output file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print("JSON file has been created.")
