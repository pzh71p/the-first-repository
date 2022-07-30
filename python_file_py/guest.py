guest = ["Albert Einstein","Isaac Newton","Stephen William Hawking"]

invitation = f"\nWelcome {guest[0].title()}, {guest[1].title()}, {guest[2].title()} for party!"
print(invitation)

print(f"\nOh, I just know that Mr.{guest[1].title()} can not attend our party")
guest.insert(1,"毛泽东")

invitation = f"\nWelcome {guest[0].title()}, {guest[1].title()}, {guest[2].title()} for party!"
print(invitation)

print("\nI just order a biger table for the party")
guest.insert(0,"Markus Persson Notch")
guest.insert(2,"James Clerk Maxwell")
guest.append("James Watt")

invitation = f"\nWelcome {guest[0].title()}, {guest[1].title()}, {guest[2].title()}, {guest[3].title()}, {guest[4].title()}, {guest[5].title()}, {guest[6].title()} for party!"
print(invitation)

print("What a pity! I just know my table can not arrive on time! So I can only invite two guests!")
for i in range(len(guest)-2):
	message = guest.pop()
	print(f"Sorry I can't invite you, {message}!")

print(f"I can still invite you {guest[0].title()} and {guest[1].title()}")
print(f"I have invitied {len(guest)} guests to my party!")

for i in range(len(guest)):
    del guest[0]
print(guest)
