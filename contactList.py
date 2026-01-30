class Contact:
    def __init__(self, name, numebr):
        self.name = name
        self.number = numebr
        
    def display(self):
        print(f"{self.name} | {self.number}")
        
class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self):
        try:
            number = int(input("Enter number: "))
            name = input("Enter contact name: ")
            
            contact = Contact(name, number)
            self.contacts.append(contact)
            print("Contact added!")
        
        except ValueError:
            print("Invalid input")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts added")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, start = 1):
                print(f"{i}. {contact.name} | {contact.number}")
    
    def search_contact(self):
        if not self.contacts:
            print("No contacts entered")
        else:
            try:
                find_name = input("Please enter name to search: ").lower()
                
                for contact in self.contacts:
                    if find_name in contact.name.lower():
                        print(f"{contact.name} | {contact.number}")
                    else:
                        print("Contact not found")
            
            except ValueError:
                print("Invalid input")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")
            
    
    def edit_contact(self):
        if not self.contacts:
            print("No contacts")
        
        else:
            try:
                while True:
                    for i, contact in enumerate(self.contacts, start = 1):
                        print(f"{i}. {contact.name} | {contact.number}")
                    con = int(input("Enter contact ID you would like to edit: "))
                    number = int(input("Enter number: "))
                    name = input("Enter contact name: ")
                    if 1 <= con <= len(self.contacts):
                        update = Contact(name, number)
                        self.contacts[con - 1] = update
                        
                        print(f"Updated {update.name}")
                        break
                    elif con == 0:
                        break
                    else:
                        print("Please select a contact ID from the list provided")
                        continue
            
            except ValueError:
                print("Invalid input")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")
                
    def delete_contact(self):
        if not self.contacts:
            print("No contacts to delete")
        else:
            try:
                while True:
                    for i, contact in enumerate(self.contacts, start = 1):
                        print(f"{i}. {contact.name} | {contact.number}")
                    
                    con = int(input("Enter contact ID you would like to delete: "))
                    if 1 <= con <= len(self.contacts):
                        print(f"{contact.name(con - 1)} deleted!")
                        self.contacts.pop(con - 1)
                        break
                    elif con == 0:
                        break
                    else:
                        print("Please select a contact ID from the list provided")
                        continue
            
            except ValueError:
                print("Invalid input")
    
    def menu(self):
        while True:
            print("Select option: ")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contacts")
            print("4. Delete Contact")
            print("5. Edit Contact")
            print("6. Exit")
            
            try:
                select = int(input())

                if select == 1:
                    self.add_contact()
                
                elif select == 2:
                    self.view_contacts()
                    
                elif select == 3:
                    self.search_contact()
                    
                elif select == 4:
                    self.delete_contact()
                    
                elif select == 5:
                    self.edit_contact()
                elif select == 6:
                    break
                else:
                    print("Please select 1-5 from the options provided")
                    continue
            except ValueError:
                print("Invalid input")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")
                
manager = ContactManager()
manager.menu()
