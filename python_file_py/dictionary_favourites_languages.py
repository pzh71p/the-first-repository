#9 for name, language in favourites_languages.items():
#10 	print(f"\n{name.title()}'s favourite language is {language.title()}")
 

favourites_languages = {
	'jerry' : 'python',
	'tom' : 'python',
	'phil' : 'c++',
	'lava' : 'java',
	'mofrom' : 'javascript'
	}
test_names = ['jerry', 'tom', 'phil', 'lava', 'mofrom', 'earn','rubbish','actu']
friends = ['jerry','tom','lava']

for name in sorted(favourites_languages.keys()):
	print(f"Hi {name.title()}.")
	if name in friends:
		languages = favourites_languages[name].title()
		print(f"{name.title()}, I see you love {languages.title()}!\n")

for test_name in sorted(test_names):
	if test_name in sorted(favourites_languages.keys()):
		print(f"\n{test_name.title()}, thank for your attending!")
	else:
		print(f"\n{test_name.title()}, why are you not in test?")

print("The following lnaguages are methioned")
for favourites_language in set(favourites_languages.values()):
	print(f"{favourites_language.title()}")


