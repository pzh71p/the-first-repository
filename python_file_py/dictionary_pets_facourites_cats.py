pets = []
pet_1 = {'pet_name' : 'sirius_pulse' , 'pet_ownner' : 'red_alert_3y', 'type' : 'pulseline_claw_cat_nekomusume'}
pet_2 = {'pet_name' : 'rue' , 'pet_ownner' : 'sake_shadowlessness', 'type' : 'ragdoll'} 
pet_3 = {'pet_name' : 'qui_gon' , 'pet_ownner' : 'merciless_gamer', 'type' : 'russian_knapweed'}

pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)

for value in pets:
	name_message = f"Pet name : {value['pet_name'].title()}"
	ownner_message = f"Ownner name : {value['pet_ownner'].title()}"
	type_message = f"Type : {value['type'].title()}"
	print(name_message)
	print(ownner_message)
	print(type_message + '\n')
