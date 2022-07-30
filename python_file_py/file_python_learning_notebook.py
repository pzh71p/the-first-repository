file_path = '/red_alert_3y/python_work/file_txt_csv_json/python_learning_notebook.txt'

with open(file_path, encoding='UTF-8') as file:
    lines = file.readlines()
    print(lines)
for i in lines:
    i = i.rstrip()
    print(i.replace('python', 'c++').title())