favourites_numbers = {
	'tom' : ['5','7','10'],
	'bay' : ['14','3'], 
	'merrysit' : ['23','35','67'],
	'noth' : ['322','64378'],
	'ccas' : ['1', '6'],
}

for name,numbers in favourites_numbers.items():
	print(f"{name.title()} likes these numbers : ")
	for number in numbers:
		print(f"\t{number}")
		