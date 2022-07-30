aliens = [ ]

for alien_number in range(30):
	new_alien = {'color' : 'green', 'speed' : 'slow', 'points' : '5'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = '15'
for alien in aliens[:5]:
	print(alien)
print("……")

print(f"The total of the aliens is {len(aliens)}")
