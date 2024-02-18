filename = input("Enter a filename to read: ")

try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the filename.")
except ValueError:
    print("Invalid value.")
except Exception as e:
    print(f"An error occurred: {e}")
