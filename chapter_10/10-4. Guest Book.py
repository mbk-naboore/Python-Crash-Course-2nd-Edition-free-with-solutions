flag = "y"
file_name = 'guest_book.txt'
while flag == "y":
    guest_first_name = input("\nPlease tell me your first name: ").strip()
    guest_last_name = input("Please tell me your last name: ").strip()
    print(f"Thank you,{guest_first_name.title()} {guest_last_name.title()}, I have added you to the guest list.")

    with open(file_name, 'a') as file:
        file.write(f"Guest: {guest_first_name.title()} {guest_last_name.title()}\n")
    flag = input("\nType[y/Y] to continue else you will quite.\n>>> ").lower()

