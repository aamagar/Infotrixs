import csv

CONTACTS_FILE = "contacts.csv"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    fieldnames = ["name", "number"]
    with open(CONTACTS_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    while True:
        number = input("Enter the contact's number: ")
        if len(number) == 10 and number.isdigit():
            break
        else:
            print("Invalid mobile number. Please enter a 10-digit number.")
    for contact in contacts:
        if contact["number"] == number:
            print("Contact already exists with this name or number.")
            return
       
    contact = {
        "name": name,
        "number": number
    } 

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter the name to search: ")
    found_contacts = []

    for contact in contacts:
        if name.lower() in contact["name"].lower():
            found_contacts.append(contact)

    if found_contacts:
        print("Found contact(s):")
        for contact in found_contacts:
            print_contact(contact)
    else:
        print("No contacts found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if name.lower() == contact["name"].lower():
            new_number = input("Enter the new number: ")

            contact["number"] = new_number

            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if name.lower() == contact["name"].lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")
def view_contacts(contacts):
    if contacts:
        print("*" *50)
        print("Contact List")
        print("*" *50)
        for contact in contacts:
            print_contact(contact)
    else:
        print("Contact list is empty.")

def print_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Number: {contact['number']}")
    print("-" * 20)

def main():
    contacts = load_contacts()

    while True:
       print("*"* 50)
       print("Contact Diary".center(50))
       print("*"* 50)
       print("1. Add Contact   "   )
       print("2. Search Contact")
       print("3. Update Contact")
       print("4. Delete Contact")
       print("5. View Contacts " )
       print("6. Exit          ")
       print("-"* 50)
       choice = input("Please Enter option from above (1-6):")

       if choice == "1":
          add_contact(contacts)
       elif choice == "2":
            search_contact(contacts)
       elif choice == "3":
            update_contact(contacts)
       elif choice == "4":
            delete_contact(contacts)
       elif choice == "5":
            view_contacts(contacts)
           
       elif choice == "6":
            print("Thankyou for Using Our Contact Diary")
            break
       else:
           print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

