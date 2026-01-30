class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def display(self, index = None):
        if index:
            print(f"{index}. {self.name} | {self.number}")
        else:
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
                contact.display(i)
    
    def search_contact(self):
        if not self.contacts:
            print("No contacts entered")
        else:
            try:
                find_name = input("Please enter name to search: ").lower()
                found = False
                for contact in self.contacts:
                    if find_name in contact.name.lower():
                        contact.display()
                        found = True

                if not found:
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
                        contact.display(i)
                        
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
                        contact.display(i)
                    
                    con = int(input("Enter contact ID you would like to delete: "))
                    if 1 <= con <= len(self.contacts):
                        removed = self.contacts.pop(con - 1)
                        print(f"{removed.name} deleted.")
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
                    print("Please select 1-6 from the options provided")
                    continue
            except ValueError:
                print("Invalid input")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")
                
manager = ContactManager()
manager.menu()
