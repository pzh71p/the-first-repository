current_users = ["david","admin","rubbish","bitch","gamer"]
new_users = ["david","curry","Mark","Aarn","William"]

for new_use in new_users:
	if new_use.lower() in new_users:
		print(f"{new_use.title()}, this name have been used, please type another name!")
	else:
		print(f"{new_use.title()}, you can surly use this name!")
