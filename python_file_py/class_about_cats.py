class Cats:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now sitting")

    def running_around_the_room(self):
        print(f"{self.name.title()} is now running around the room")

