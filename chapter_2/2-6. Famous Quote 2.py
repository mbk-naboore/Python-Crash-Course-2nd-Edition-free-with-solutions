the_quote = "Impossible is temporary. Impossible is nothing."
famous_person = "muhammad ali"


# first way:
message = f'{famous_person.title()} once said, "{the_quote}"'
print(message)

# second way:
message = f"{famous_person.title()} once said, \"{the_quote}\""
print(message)
# the second way we used the escape-character (\)...


