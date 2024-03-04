import csv
contacts = [
{'name': 'AllenRaymond','email':'nulla.ante@vestibul.co.uk','phone':9929143792,'favorite':False},
{'name': 'ChaimLewis','email':'dui.int@egetlacus.ca','phone':2948406685,'favorite':False},
{'name': 'KennedyLane','email':'mattis.Cras@nonenimMauris.net','phone':5424517038,'favorite':True},
{'name': 'WyliePope','email':'est@utquamvel.net','phone':6928022949,'favorite':False},
{'name': 'CyrusJackson','email':'nibh@semsempererat.com','phone':5014725218,'favorite':True}
]

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ['name','email','phone','favorite']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for con in contacts:
            writer.writerow(con)
def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        contacts = []
        for row in reader:
            favor = row.get('favorite')
            clean = favor.strip("'")
            clean = clean == 'True'
            print(f"clean = {clean}")
            favor = row.pop('favorite')
            row.update({'favorite':clean})
            contacts.append(row)
    # return contacts
    # print(f"contacts = {contacts}") 
    i = 0
    for value in contacts:
        i +=1
        print(f"{i:5}.  {value}")  
    # print(f"contacts = {contacts}")
if __name__ == "__main__":
    write_contacts_to_file(r'D:\Projects\Module6\Module6\A8.csv', contacts)
    read_contacts_from_file(r'D:\Projects\Module6\Module6\A8.csv')