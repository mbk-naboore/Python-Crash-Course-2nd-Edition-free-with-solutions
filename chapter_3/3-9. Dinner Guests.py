# the code is copied from (3-7. Shrinking Guest List) exercise...
# the new line is the new 51 line....

guest=["muhammad ali", "mike tyson", "mbk-naboore"]

print("\n")
print(f"You Are invited to my house Mr.{guest[0].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[1].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[2].title()}", "at 7:00 pm.")
print("="*50)

print(f"\nsorry to hear that Mr.{guest[2].title()} is not coming tonight...\n")
guest.pop(2)
guest.append("elon musk")
print("="*50)

print(f"You Are invited to my house Mr.{guest[0].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[1].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[2].title()}", "at 7:00 pm.")
print("="*50)

print("\nI have found the best place for the invitation and it will be 6 people...\n")
guest.insert(0, "jack")
guest.insert(3, "sparrow")
guest.append("sheldon")
print("="*50)

print(f"You Are invited to my house Mr.{guest[0].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[1].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[2].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[3].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[4].title()}", "at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[5].title()}", "at 7:00 pm.")
print("="*50)

print("\nI am really sorry to all of the invited guests, I am being informed right now that I will be able to invite 2 guests only.\n")
print("="*50)

removed_guest = guest.pop(0)
print(f"I am really sorry to not invite you Mr.{removed_guest}.")
removed_guest = guest.pop()
print(f"I am really sorry to not invite you Mr.{removed_guest}.")
removed_guest = guest.pop()
print(f"I am really sorry to not invite you Mr.{removed_guest}.")
removed_guest = guest.pop()
print(f"I am really sorry to not invite you Mr.{removed_guest}.")
print("="*50)

print(f"You are still invited to my house Mr.{guest[0]}.")
print(f"You are still invited to my house Mr.{guest[1]}.")
print(f"I have invited only {len(guest)} guests.")
print("="*50)


del guest[1]
del guest[0]
print(guest)


