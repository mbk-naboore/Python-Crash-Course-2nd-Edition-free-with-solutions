file_name = 'learning_python.txt'

with open(file_name) as file:
    for line in file:
        print(line.replace("Python", "C"))

