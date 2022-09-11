# the file_name(path)
file_name = 'learning_python.txt'

# Reading the entire file_content...
with open(file_name) as file:
    contents = file.read()
    print(contents)


# Looping over the file content line by line...
with open(file_name) as file:
    for line in file:
        print(line)

# making a list of all the lines in the file...
with open(file_name) as file:
    lines = file.readlines()
for line in lines:
    print(line)
