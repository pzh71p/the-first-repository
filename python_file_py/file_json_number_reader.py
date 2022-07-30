import json

file_name = '/red_alert_3y/python_work/file_txt_csv_json/numbers.json'
with open(file_name) as file:
    numbers = json.load(file)
print(numbers)