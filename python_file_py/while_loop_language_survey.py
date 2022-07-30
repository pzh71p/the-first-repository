from class_survey import Survey

question = "What language did you first learn to speak?"
my_survey = Survey(question)

my_survey.show_question()
print("Enter q at anytime to quit.\n")
while True:
    response = input("Language : ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("Thank you to everybody who take part in this survey!")
my_survey.show_result()