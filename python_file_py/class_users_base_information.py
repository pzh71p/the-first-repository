class Users:

    def __init__(self, first_name, last_name, login_attempts=0, **more_things):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.more_things = more_things
        self.more_things['first_name'] = self.first_name
        self.more_things['last_name'] = self.last_name

    def describe_users(self):
        user_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"{user_name}'s basic information: ")
        for i in self.more_things.keys():
            print(f"{i.title()} : {self.more_things[i].title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


class Admin(Users):
    def __init__(self, first_name, last_name, login_attempts=0, **more_things):
        super().__init__(first_name, last_name, login_attempts=0, **more_things)
        self.privilege = Privilege()


class Privilege:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Here are your privileges : ")
        if self.privileges:
            for i in self.privileges:
                print(f"- {i.title()}")
        else:
            print("This user has no privileges!")


red_alert_3y = Users('red_alert', '3y', pet_name='sirius_pulse')
red_alert_3y.describe_users()
s = 0
for i in range(4):
    s = red_alert_3y.increment_login_attempts()
print(s)
s = red_alert_3y.reset_login_attempts()
print(s)

pri = ['can add post', 'can delete post', 'can ban user']
admin = Admin('sad sometimes', 'yxy', location='hubei')
admin.privilege.privileges = pri
admin.privilege.show_privileges()
