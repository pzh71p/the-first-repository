my_favourite_basketball_player = ["Michael Jordan","Shaquille O'Neal","Kyrie Irving","Giannis Antetokounmpo","Stephen Curry","Kobe Bean Bryant"]

#print(f"The first three players in the list are: \n\t{basketball_player[:3]}")
#print(f"Three basketball player from the middle: \n\t{basketball_player[2:4]}")
#print(f"The last three baskerball player in the list are \n\t{basketball_player[-3:]}")

her_favourite_basketball_player = my_favourite_basketball_player[:]

my_favourite_basketball_player.append("Kevin Wayne Durant")
her_favourite_basketball_player.append("LeBron Raymone James")

print(f"Her favourite basketball players are {her_favourite_basketball_player}")
print(f"My favuorite basketball players are {my_favourite_basketball_player}")

for hers in her_favourite_basketball_player:
	print(f"Her favourite basketball players are {hers.title()}")
for mine in my_favourite_basketball_player:
	print(f"My favourite basketball players are {mine.title()}")