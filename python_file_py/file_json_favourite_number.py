import json


def remember_your_favourite_numbers():
    favourite_number = input("Enter your favourite number and I'll remember")
    file_name = '/red_alert_3y/python_work/file_txt_csv_json/favourite_number.json'
    with open(file_name, 'w') as file:
        json.dump(favourite_number, file)


def read_favourite_number():
    file_name = '/red_alert_3y/python_work/file_txt_csv_json/favourite_number.json'
    try:
        with open(file_name) as file:
            number = json.load(file)
            print(f"I know your favourite number it is {int(number)}")
    except FileNotFoundError:
        remember_your_favourite_numbers()

read_favourite_number()