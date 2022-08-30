# the beginners way(1):
one_million_list1 = list(range(1,1000001))
for number in one_million_list1:
    print(number)

# the beginners way(2):
one_million_list2 = []
for the_number in range(1, 1000001):
    print(the_number)
    one_million_list2.append(the_number)
    # this .append() method is to save the number in the list...


# the advanced way only one line:
number_list = [print(numberss) for numberss in range(1, 1000001)]
