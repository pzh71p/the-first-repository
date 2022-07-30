def make_album(singer_name,album_name,quantitly=None):
	message = {'singer name' : singer_name.title(), 'album name' : album_name.title(), 'quantitly' : quantitly}
	return message

while True:
	print("\nType something to make albums!")
	print("Or just hit 'q' to quit")
	singer = input("Singer name?")
	if singer == 'q':
		break
	album = input("Album name?")
	if album == 'q':
	    break
	quantitly_input = input("Quantitly if you have!")
	if quantitly_input == 'q':
		break
	output = make_album(singer,album,quantitly_input)
	print(output)

