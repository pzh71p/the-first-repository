users = [ ]
users_0= {
	'username' : 'red_alert_3y', 
	'first_name' : 'yaoi fandoml', 
	'last_name' : 'minecraft',  
}
users_1= {
	'username' : 'sake_shadowlessness', 
	'first_name' : 'fag_rot', 
	'last_name' : 'fifth_personality',  
}
users_2= {
	'username' : 'merciless_gamer', 
	'first_name' : 'octavio_silva', 
	'last_name' : 'apex_heroes',  
}

users.append(users_0)
users.append(users_1)
users.append(users_2)

for user_name in users:
	usernames = f"User name: {user_name['username'].title()}"
	full_name = f"User' s full name: {user_name['first_name'].title()} {user_name['last_name'].title()}"
	print(usernames)
	print(full_name + "\n")
