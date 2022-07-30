import random

lottery_number = ('1', '2', '3' ,'4', '5', '6', '7', '8', '9', '10')
lottery_letter = ('y', 'x', 'p', 'z', 'h')

class Lottery:
    def __init__(self, number, letter):
        self.number = number
        self.letter = letter
        self.output = []

    def make_lottery(self):
        for i in range(3):
            self.output.append(random.choice(self.number))
        for b in range(3):
            self.output.append(random.choice(self.letter))
        return self.output

my_tickets = Lottery(lottery_number, lottery_letter)
print(my_tickets.make_lottery())