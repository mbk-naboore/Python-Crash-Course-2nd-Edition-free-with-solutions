print("\n\tTHIS CODE WILL ADD ANY TWO NUMBERS YOU ARE GOING TO GIVE\t")
print("you can quit any time by pressing 'q'.")
n1 = input("the first number is: ").strip()
if n1 == "q":
    exit()
n2 = input("the second number is: ").strip()
if n2 == "q":
    exit()
try:
    answer = int(n1) + int(n2)
    print(f"your answer is ({answer}).")
    print("-"*75)
except ValueError:
    print("Sorry, you can not add strings.")
    print("-" * 75)
print("Thank you for using my code...")