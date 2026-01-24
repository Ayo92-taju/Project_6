import string
contacts = []

def menu():
    while True:
        print("Select option: ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Exit")
        select = int(input())

        if select == 1:
            add(contacts)
            continue
        elif select == 2:
            view(contacts)
            continue
        elif select == 3:
            search(contacts)
            continue
        elif select == 4:
            delete(contacts)
            continue
        elif select == 5:
            edit(contacts)
        elif select == 6:
            break
        else:
            print("Please select 1-5 from the options provided")
            continue
        
def add(contacts):
    try:
        number = int(input("Enter number: "))
        name = input("Enter contact name: ")
        contact = {"Name": name, "Number": number}
        print("Contact added!")
        return contacts.append(contact)
        
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

def view(contacts):
    if not contacts:
        print("No contacts added")
    else:
        try:
            for i, contact in enumerate(contacts, start = 1):
                print(f"{i}. {contact["Name"]} | {contact["Number"]}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
        
def delete(contacts):
    if not contacts:
        print("No contacts to delete")
    else:
        while True:
            for i, contact in enumerate(contacts, start = 1):
                print(f"{i}. {contact["Name"]} | {contact["Number"]}")
            con = int(input("Enter contact ID you would like to delete: "))
            if 1 <= con <= len(contacts):
                removed = contacts.pop(con - 1)
                print(f"Removed {removed["Name"]}")
                break
            elif con == 0:
                break
            else:
                print("Please select a contact ID from the list provided")
                continue
            
def edit(contacts):
    if not contacts:
        ("No contacts")
    else:
        while True:
            for i, contact in enumerate(contacts, start = 1):
                print(f"{i}. {contact["Name"]} | {contact["Number"]}")
            con = int(input("Enter contact ID you would like to edit: "))
            new_num = int(input("Enter number: "))
            new_name = input("Enter contact name: ")
            if 1 <= con <= len(contacts):
                update = {"Name": new_name, "Number": new_num}
                contacts[con - 1] = update
                
                print(f"Updated {update["Name"]}")
                break
            elif con == 0:
                break
            else:
                print("Please select a contact ID from the list provided")
                continue
        
            
def search(contacts):
    while True:
        if not contacts:
            print("No contacts entered")
            break
        else:
            find_name = input("Please enter name to search: ").lower()
            
            for contact in contacts:
                if find_name in contact["Name"].lower():
                    print(f"{contact["Name"]} | {contact["Number"]}")
                    found = True
                else:
                    found = False
            if not found:
                    print("Contact not found")
                    break
            break
print("Contact List\n")
menu()