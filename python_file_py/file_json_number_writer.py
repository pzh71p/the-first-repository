import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

file_name = '/red_alert_3y/python_work/file_txt_csv_json/numbers.json'
with open(file_name, 'w') as file:
    json.dump(numbers, file)
