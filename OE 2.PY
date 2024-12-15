#OE2

class Phone:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

def display_phones(phone_list):
    if not phone_list:
        print("No phones available.")
    

def add_phone(phone_list):
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    year = input("Enter phone year: ")
    phone_list.append(Phone(brand, model, year))
    print("Phone added successfully!")

def modify_phone(phone_list):
    display_phones(phone_list)
    index = int(input("Enter the number of the phone to modify: ")) - 1
    if 0 <= index < len(phone_list):
        phone = phone_list[index]
        phone.brand = input(f"Enter new brand (current: {phone.brand}): ") or phone.brand
        phone.model = input(f"Enter new model (current: {phone.model}): ") or phone.model
        phone.year = input(f"Enter new year (current: {phone.year}): ") or phone.year
        print("Phone modified successfully!")
    else:
        print("Invalid phone number.")

def delete_phone(phone_list):
    display_phones(phone_list)
    index = int(input("Enter the number of the phone to delete: ")) - 1
    if 0 <= index < len(phone_list):
        del phone_list[index]
        print("Phone deleted successfully!")
    else:
        print("Invalid phone number.")

def main():
    phone_list = []
    while True:
        print("Phone Management System")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. Display Phones")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_phone(phone_list)
        elif choice == '2':
            modify_phone(phone_list)
        elif choice == '3':
            delete_phone(phone_list)
        elif choice == '4':
            display_phones(phone_list)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
