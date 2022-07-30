users = {
	'atuato' : {
		'first_name' : 'albot',
		'last_name' : 'utatishos',
		'location' : 'primintion'
	},

	'micial' : {
		'first_name' : 'minssake',
		'last_name' : 'cicasial',
		'location' : 'paris'
		}
}

for user_name, user_infor in users.items():
	print(f"\nUsername: {user_name.title()}")
	full_name = f"User's full name is {user_infor['first_name']} {user_infor['last_name']}."
	location = f"User's location is {user_infor['location'].title()}!"
	print("\t" + full_name.title())
	print("\t" + location)


