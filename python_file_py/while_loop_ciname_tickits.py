while True:
    age = input("Type a age to check your cinma tickets cost, or hit [ENTER] to end!")
    if age != "":
        age = int(age)
        print(f"Your age is {age}!")
        if age < 3:
                print(f"Your tickets cost [FREE]!")
        elif age < 12:
                print(f"Your tickets cost 12$")
        else:
                print(f"Your tickets cost 15$")
