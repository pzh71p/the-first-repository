def build_person(first_name,last_name,**user_information):
    user_information['first name'] = first_name.title()
    user_information['last name'] = last_name.title()
    return user_information


red = build_person('red','3y',middle_name='Alter',pet_name='sirius_pulse',pet_type='pulseline_claw_cat_nekomusume')
print(red)