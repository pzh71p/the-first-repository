unconfirmed_users = ["alice", "caon", "biam"]
confirmed_users = [ ]

while unconfirmed_users:
    current_users = unconfirmed_users.pop() 
    print(f"This user have been confirmed: {current_users.title()}")
    confirmed_users.append(current_users)
print(f"These following users have been confirmed:" )
for user in confirmed_users:
	print("\t" + user.title())