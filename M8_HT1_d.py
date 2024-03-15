import pickle
from collections import UserDict

class BaseClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Phone(BaseClass):
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError(f'Invalid phone format: {phone}')
        super().__init__(phone)

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = None

    def add_date(self, birthday):
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones = phone

class AddressBook(UserDict):
    def __init__(self, filename):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            self.data = []

    def save_data(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.data, f)

    # Implement other methods as before
def parse_input(user_input): #ввод команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    # args0.clear()
    # for a in args:
    #     print(f" a = {a}")
    #     if str(a).isdigit():
    #         args0.append(a)
    #         print(f" 0 args0 = {args0}")
    # print(f" args0 = {args0}")
    return cmd, *args

def main():
    addressBook = AddressBook('A1.pkl')
    print("Welcome to the assistant bot!")
    print("Commands format:\nclose or exit\nadd [name] [phone]\nlist\nfindname [name]\nremove [name]\nchangephone [name] [new phone]\naddbirthday [name] [YYYY.MM.DD]")
    print("findbirthday [name]\nbirthday")
    
    while True: 
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "add":
            addressBook.add_record(args[0], args[1])
        elif command == "list":
            addressBook.list() 
        elif command == "findname":
            addressBook.find_name(args[0])
        elif command == "remove":
            addressBook.remove_name(args[0])
        elif command == "changephone":
            addressBook.change_phone(args[0], args[1])
        elif command == "addbirthday":
            addressBook.add_birthday(args[0], args[1])
        elif command == "findbirthday":
            addressBook.find_birthday(args[0])
        elif command == "birthday":
            addressBook.get_upcoming_birthdays()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()