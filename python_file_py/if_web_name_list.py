name_list = [] #["david","admin","rubbish","bitch","gamer"]

if name_list:
	for name in name_list:
		if name == "admin":
			print(f"Hello {name.title()}, would you like to see a staus report ?\n")
		else:
			print(f"Hello {name.title()}, thank you for logging in again!\n")
else:
	print("Are you sure we have users ?")

