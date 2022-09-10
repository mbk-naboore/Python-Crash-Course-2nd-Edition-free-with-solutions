import random

possibilities = ["a", "b", "r", "o", "m", '0', '2', '3', '4', '5', '6', '7', '8', '9']


def getting_the_ticket():
    return "".join(random.sample(possibilities, 4))


def changing_my_ticket_tell_win(winning_ticket, my_ticket):
    counter = 0
    while winning_ticket != my_ticket:
        my_ticket = getting_the_ticket()
        counter += 1
    print(f"Yes, I have Won after buying (( {counter} )) tickets only, LOL:) ...\nYou can see now the wining ticket is [ {winning_ticket} ] and mine is [ {my_ticket} ]...")
    pass

winning_ticket = getting_the_ticket()
print(f"\n\nthe winning ticket is: [ {winning_ticket} ].")

my_ticket = getting_the_ticket()
print(f"the old ticket I had was: [ {my_ticket} ].")
print("-"*75)
changing_my_ticket_tell_win(winning_ticket, my_ticket)

