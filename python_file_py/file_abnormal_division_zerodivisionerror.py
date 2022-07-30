while True:
    print("Give me two numbers and I'll divide them!")
    print("Or just hit [Enter] to quit!")
    first_number = input("First number?")
    if first_number == '':
        break
    second_number = input("Second number?")
    if second_number == '':
        break
    try:
        answer = int(float(first_number)) / int(float(second_number))
    except ZeroDivisionError:
        print("You can't divide a number by zero!")
    else:
        print(answer)
