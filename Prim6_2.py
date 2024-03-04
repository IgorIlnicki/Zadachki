from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def check_if_10(self):
        length=self
        if len(length)!=10:
            raise Exception("Wrong phone number format. Should be 10 digits.")
        else:
            return self
              
class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,item):
        try:
            self.phones.append(str(Phone.check_if_10(item)))
        except Exception as e:
            print(e)
        
    def remove_phone(self,item):
        if item in self.phones:
            self.phones.remove(item)
    
    def edit_phone(self,old,new):
        if old in self.phones:
            self.phones.remove(old)
            try:
                self.phones.append(str(Phone.check_if_10(new)))
            except Exception as e:
                print(e)
            # return f"{self.name.value}:{'; '.join(p for p in self.phones)}"
        
    def find_phone(self,phone):
        if phone in self.phones:
            return f"{self.name}: {phone}"
        else:
            return "Not found"
        
    def list(self):
        # self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        i = 0
        for key in self.data1:
                i +=1
                len2=0 
                print(f"{i:2}. {key:10} Телефон: """, end="")
                len1 = len(self.data1[key])
                for value in self.data1[key]:
                    len2 +=1
                    if len2 < len1:
                        print(f"{value}"", ", end="")
                    else:
                        print(f"{value}")   
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

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

class AddressBook(UserDict):
    def add_record (self,item):
        self.data[item.name.value]=item
    
    def find(self,item):
        return self.data.get(item)
            
    def delete(self,item):
        if item in self.data:
            del self.data[item]

def main():
        addressBook = AddressBook()

        print("Ласкаво просимо до бота-помічника!")
        while True:
            user_input = input("Введіть команду: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                record = Record(args[0])
                record.add_phone(args[1])
            #    addressBook.add_record(record.name, record.phones)
            elif command == "list":
                addressBook.list() 
            elif command == "findname":
                addressBook.find_name(args[0])
            elif command == "remove":
                addressBook.remove_name(args[0])
            elif command == "changename":
                addressBook.change_name(args[0],args[1])
            elif command == "changephone":
                record = Record(args[0])
                record.add_phone(args[1])
                addressBook.change_phone(record.name, record.phones)
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()