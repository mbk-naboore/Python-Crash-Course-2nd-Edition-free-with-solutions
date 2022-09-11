
guest_first_name = input("Please tell me your first name: ").strip()
guest_last_name = input("Please tell me your last name :").strip()
print("Thank you, I have added you to the guest list.")


file_name = 'guest.txt'

with open(file_name, 'w') as file:
    file.write(f"Guest: {guest_first_name.title()} {guest_last_name.title()}\n")

