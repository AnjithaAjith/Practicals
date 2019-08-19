def main():
    password = get_password(6)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter password of at least 6 characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password of at least 6 characters: ")
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()