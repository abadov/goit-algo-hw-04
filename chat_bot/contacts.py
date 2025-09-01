contacts = {}

def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."

def get_phone_by_name(args):
    name, = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def get_all_contacts():
    return contacts
