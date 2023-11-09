import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __str__(self):
        a = self.name
        return a


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):

        if contacts is None:
            self.contacts = []
            # self.contacts.append(contacts)
        else:
            self.contacts = []
            self.contacts.append(contacts)
        self.filename = filename
        # print(self.contacts[0])

    def save_to_file(self):
        # persons = Contacts(self.filename, self.contacts)
        with open(self.filename, 'wb') as fw:
            pickle.dump(self.contacts, fw)
        # print(persons)

    def read_from_file(self):
        with open(self.filename, 'rb') as fr:
            contacts = pickle.load(fr)
        return contacts


print('Go')

# contacts = [
#     Person(
#         "Allen Raymond",
#         "nulla.ante@vestibul.co.uk",
#         "(992) 914-3792",
#         False,
#     ),
#     Person(
#         "Chaim Lewis",
#         "dui.in@egetlacus.ca",
#         "(294) 840-6685",
#         False,
#     ),
# ]

# save
# persons = Contacts("txt.bin", contacts)
# persons.save_to_file()

# load
persons = Contacts("txt.bin")
conts = persons.read_from_file()
for memb in conts:
    for q in memb:

        print(q)
