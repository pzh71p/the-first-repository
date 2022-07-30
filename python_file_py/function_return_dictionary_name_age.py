def build_person(first_name,last_name,age=None):
	person = {'first_name' : first_name, 'last_name' : last_name}
	if age:
		person['age'] = age
	return person 

person = build_person('red','alert')
print(person)