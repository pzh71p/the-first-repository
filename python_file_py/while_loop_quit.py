prompt = "\nTell me something and I'll repeat it back to you!"
prompt += "\nOr enter 'quit' to quit!"
 
while True:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(message)