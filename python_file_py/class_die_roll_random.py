import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        choose = random.randint(1, self.sides)
        return choose

my_choose = Die(20)
for i in range(10):
    print(my_choose.roll_die())