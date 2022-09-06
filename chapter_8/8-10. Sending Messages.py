def send_messages(list_message):

    sent_message_list = list()

    while list_message:
        popped_message=list_message.pop(0)
        print(popped_message)
        sent_message_list.append(popped_message)

    return sent_message_list


list_message_to_function = ["Hello", "How are you doing", "I love you", "Have a nice day"]
sent_message_list_from_function = send_messages(list_message_to_function)

print("------------------------------------------")

print("the list message:::", list_message_to_function)
print("the sent message list:::", sent_message_list_from_function)


# If the items were moved correctly then the (list_message_to_function) would now be empty
# and the (sent_message_list_from_function) has all the values in it...
