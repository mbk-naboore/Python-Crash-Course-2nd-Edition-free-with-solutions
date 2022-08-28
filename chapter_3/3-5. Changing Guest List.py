guest=["muhammad ali", "mike tyson", "mbk-naboore"]

print("\n")
print(f"You Are invited to my house Mr.{guest[0].title()}","at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[1].title()}","at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[2].title()}","at 7:00 pm.")
print("="*50)

print(f"\nsorry to hear that Mr.{guest[2].title()} is not coming tonight...\n")
guest.pop(2)
guest.append("elon musk")
print("="*50)

print(f"You Are invited to my house Mr.{guest[0].title()}","at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[1].title()}","at 7:00 pm.")
print(f"You Are invited to my house Mr.{guest[2].title()}","at 7:00 pm.")
