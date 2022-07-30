alien_color =  ["red"] #["green"] ["yellow"] ["red"]
score = 0

if "green" in alien_color:
	score = 5
elif "yellow" in alien_color:
	score = 10
else:
	score = 15

print(f"You got {score} score!")