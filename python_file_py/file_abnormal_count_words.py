def count_words(file_name):
    try:
        with open(file_name, encoding='UTF-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, this file {file_name.title()} is not found in this folder!!!")
    else:
        contents = contents.split()
        output = len(contents)
        print(f"{file_name.title()} has {output} words in it!")


files = ['/red_alert_3y/python_work/file_txt_csv_json/alice.txt',
         '/red_alert_3y/python_work/file_txt_csv_json/moby_dick.txt',
         '/red_alert_3y/python_work/file_txt_csv_json/little_women.txt',
         '/red_alert_3y/python_work/file_txt_csv_json/siddhartha.txt']
for i in files:
    count_words(i)
