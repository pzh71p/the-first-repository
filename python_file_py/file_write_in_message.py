file_name = '/red_alert_3y/python_work/file_txt_csv_json/write_in_guest.txt'

with open(file_name, 'a') as file:
    while True:
        inside = input("Enter your name to save in or just hit [Enter] to quit")
        if inside == '':
            break
        file.write(f"\n {inside.rstrip().title()}")