from chat_bot.contacts import add_contact, get_all_contacts, change_contact, get_phone_by_name

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "all":
            print(get_all_contacts())
        elif command == "phone":
            print(get_phone_by_name(args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
