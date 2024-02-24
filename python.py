import json

class Contact:
    def __init__(self, name, phone, email, address=None, birthday=None, notes=None, job_title=None, company=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
        self.notes = notes
        self.job_title = job_title
        self.company = company

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "birthday": self.birthday,
            "notes": self.notes,
            "job_title": self.job_title,
            "company": self.company
        }

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}, Birthday: {self.birthday}, Notes: {self.notes}, Job Title: {self.job_title}, Company: {self.company}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact}")
        else:
            print("No contacts found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Contact found:")
                print(contact)
                return
        print("Contact not found.")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)
        print("Contacts saved to file.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(**data) for data in contacts_data]
            print("Contacts loaded from file.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address (optional): ")
            birthday = input("Enter birthday (optional): ")
            notes = input("Enter notes (optional): ")
            job_title = input("Enter job title (optional): ")
            company = input("Enter company (optional): ")
            contact = Contact(name, phone, email, address, birthday, notes, job_title, company)
            address_book.add_contact(contact)
        elif choice == "2":
            address_book.view_contacts()
        elif choice == "3":
            name = input("Enter name of contact to delete: ")
            address_book.delete_contact(name)
        elif choice == "4":
            name = input("Enter name of contact to search: ")
            address_book.search_contact(name)
        elif choice == "5":
            filename = input("Enter filename to save contacts: ")
            address_book.save_to_file(filename)
        elif choice == "6":
            filename = input("Enter filename to load contacts from: ")
            address_book.load_from_file(filename)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
