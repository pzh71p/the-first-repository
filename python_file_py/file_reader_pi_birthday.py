file_path = '/red_alert_3y/python_work/file_txt_csv_json/pi_digits.txt'

with open(file_path, 'r', encoding='UTF-8') as file_object:
    file = file_object.readlines()

pi_string = ""
for i in file:
    pi_string += i.strip()

birthday = input("Enter your birthday, in from pi~")
if birthday in pi_string:
    print("We find your birthday in pi")
else:
    print("We haven't find your birthday in pi")
