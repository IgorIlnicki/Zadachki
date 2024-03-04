import pickle
сontacts= [{
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": False
    }]
def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as f:
        pickle.dump(contacts, f)
        


def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        contacts = pickle.load(fh)