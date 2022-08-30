# the beginner way
cube_list = []
for number in range(1, 11):
    answer = number**3
    cube_list.append(answer)
    print(f"the cube of {number} is {answer}..")


# the advanced way only one line ......
cube_list = [print(f"the cube for number {x} is", x**3) for x in range(1, 11)]
