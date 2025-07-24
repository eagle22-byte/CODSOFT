contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contacts[name] = number
    print(f"{name} added successfully.\n")

def view_contacts():
    if not contacts:
        print("Contact book is empty.\n")
    else:
        print("\nContact List:")
        for name, number in contacts.items():
            print(f"{name} : {number}")
        print()

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}\n")
    else:
        print(f"{name} not found in contact book.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted successfully.\n")
    else:
        print(f"{name} not found.\n")

while True:
    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Bye!")
        break
    else:
        print("Invalid choice. Try again.\n")
