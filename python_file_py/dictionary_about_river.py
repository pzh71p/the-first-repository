rivers = {
	'nile' : 'egypt', 
	'yangtze river' : 'china', 
	'mississippi river' : 'american'
} 
for river in sorted(rivers.keys()):
	print(f"The {river.title()} runs through {rivers[river].title()}")
for i in sorted(rivers.keys()):
	print(i.title())
for r in sorted(rivers.values()):
	print(r.title())