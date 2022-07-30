favourites_languages = {
	'jerry' : 'python',
	'tom' : 'python',
	'phil' : 'c++',
	'lava' : 'java',
	'mofrom' : 'javascript'
}
python_terms = {
	'if' : '如果', 
	'list' : '列表', 
	'print' : '打印', 
	'get' : '获取', 
	'dictionary' : '字典', 
}

for name in sorted(favourites_languages.keys()):
	languages = favourites_languages[name].title()
	print(f"{name.title()} likes {languages.title()}")
	for terms,output_terms in sorted(python_terms.items()):
		name = terms
		favourites_languages[name] = output_terms	
		print(f"{terms.title()} : {output_terms.title()}")	
print(favourites_languages)

