m = ["hello rea alter 3y","bb needs feeding","cars form space","卡其脱离态"]
sent = []

def show_message(input_message):
    for message in input_message:
        print(message.title())


def send_message(sent_message,input_message):
    while input_message:
        current_message = input_message.pop()
        print(current_message)
        sent_message.append(current_message)


show_message(m)
send_message(sent,m[:])
print(m)
print(sent)
