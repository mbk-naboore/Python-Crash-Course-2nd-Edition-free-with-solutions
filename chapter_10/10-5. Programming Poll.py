file_name = 'Programming_poll.txt'
flag = "y"
while flag == "y":
    user_answer = input("\nPlease tell me why do you like programming: ").strip()
    print(f"Thank you, I have added that to the file.")
    with open(file_name, 'a') as file:
        file.write(user_answer+"\n")
    flag = input("\nType[y/Y] to continue else you will quite.\n>>> ").lower()


