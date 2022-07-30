while True:
    print("You can give me two numbers and I'll plus them together!")
    print("Or just hit [ENTER] to quit!")
    first_number = input("The first number?")
    if first_number == '':
        break
    second_number = input("The second number?")
    if second_number == '':
        break
    try:
        answer = float(first_number) + float(second_number)
    except ValueError:
        print("The value you entered is invalid. Please re-enter!")
    else:
        print(f"The answer to {first_number} + {second_number} is {answer}")
