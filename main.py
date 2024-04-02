from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if name is None:
            raise ValueError("Name cannot be empty")
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Phone number must be a string of 10 digits")
        super().__init__(phone)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        else:
            print(f"Phone number {phone_number} not found")

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                return
        else:
            print(f"Phone number {old_phone_number} not found")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        print(f"Phone number {phone_number} not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        name = record.name.value
        self.update({name: record})

    def find(self, name):
        return self.get(name)

    def delete(self, name):
        del self[name]
        print(f"Record {name} deleted")


# Creating a new address book
addressbook = AddressBook()

# Create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Adding John to the address book
addressbook.add_record(john_record)

# Create and add a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
addressbook.add_record(jane_record)

# Output of all entries in the address book
for name, record in addressbook.data.items():
    print(record)

# Find and edit John's phone
john = addressbook.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

# Search for a specific phone in a John record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Deleting Jane's record
addressbook.delete("Jane")
