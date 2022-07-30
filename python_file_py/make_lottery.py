from random import choice as ch

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'y', 'x', 'p', 'z', 'h')


def make_lottery(number_letter):
    winning = []
    while len(winning) < 6:
        input_number = ch(number_letter)
        if input_number not in winning:
            winning.append(input_number)
    return winning


def test(winning_lottery, test_lottery):
    for i in test_lottery:
        if i not in winning_lottery:
            return False
    return True


lottery = make_lottery(numbers)
print(lottery)
play_times = 0
win = False
max_times = 1_0000_0000

while not win:
    new_lottery = make_lottery(numbers)
    win = test(lottery, new_lottery)
    play_times += 1
    if play_times >= max_times:
        break
if win:
    print(f"You win!")
    print(f"Before {play_times} times's try you win!")
else:
    print("You try 1_0000_0000 times but not win")