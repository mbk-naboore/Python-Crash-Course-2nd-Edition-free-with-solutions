file1 = "cats_10_8.txt"
file2 = "dogs_10_8.txt"


def printing_the_contents(file_path):
    try:
        with open(file_path) as file:
            print(f"\nThe file ({file_path}) content is: ")
            print(file.read().strip().title())
            print("---------------------------------------------------")
    except FileNotFoundError:
        print(f"The file ({file_path}) was not found.")
    pass


printing_the_contents(file1)
printing_the_contents(file2)

