file_path = ['/red_alert_3y/python_work/file_txt_csv_json/cats.txt',
             '/red_alert_3y/python_work/file_txt_csv_json/dogs.txt']

for i in file_path:
    try:
        with open(i, encoding='UTF-8') as file:
            line = file.readlines()
            for b in line:
                print(b.rstrip().title())
    except FileNotFoundError:
        print(f" ! Error : File {i.title()} was not found in this folder !")