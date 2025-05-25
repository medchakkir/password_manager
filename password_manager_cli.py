def view():
    try:
        with open('passwords.txt', 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No saved passwords found.")
                return
            for line in lines:
                data = line.rstrip()
                if '|' in data:
                    user, passw = data.split("|")
                    print("Username:", user, "| Password:", passw)
                else:
                    print("Malformed line:", data)
    except FileNotFoundError:
        print("No password file found. Start by adding a password.")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')
    print("Password added successfully.")

def main():
    while True:
        mode = input("\nType 'add' to add a new password, 'view' to see existing ones, or 'q' to quit: ").lower()

        if mode == "q":
            print("Goodbye!")
            break
        elif mode == 'view':
            view()
        elif mode == 'add':
            add()
        else:
            print("Invalid option. Please type 'add', 'view', or 'q'.")

if __name__ == "__main__":
    main()
