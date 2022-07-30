import json

def get_stored_name():
    file_name = '/red_alert_3y/python_work/file_txt_csv_json/username.json'
    try:
        with open(file_name) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user_name():
    username = input("What is your name~")
    file_name = '/red_alert_3y/python_work/file_txt_csv_json/username.json'
    with open(file_name, 'w') as file:
        json.dump(username, file)
    return username


def greet_user():
    username = get_stored_name()
    test = input("Enter your name to test if you are the user!")
    if test == username:
        if username:
            print(f"Welcome back {username.title()}!")
        else:
            username = get_new_user_name()
            print(f"We'll remember you when you come back {username.title()}")
    else:
        print("You are not the user")


greet_user()