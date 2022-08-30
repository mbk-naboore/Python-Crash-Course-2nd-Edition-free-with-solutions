# the beginner way
odd_numbers=list(range(1, 21, 2))
for odd in odd_numbers:
    print(f"{odd}")


# the advanced way only one line ......
odd_number = [print(odd) for odd in range(1, 21, 2)]
