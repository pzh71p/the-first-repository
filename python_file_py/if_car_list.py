cars = ["Lamborghini","Ferrari","Bentley","Volkswagen"]

for car in cars:
	if car == "Lamborghini":
		print(car.upper())
	else:
		print(car.title())
banned_users = ["m416","alien","chengxing"]
user = "m416"

if user not in banned_users:
	print(f"{user.title()}, you can use this app!")
else:
	print(f"{user.upper()}, you can not use this app!")