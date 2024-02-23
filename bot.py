def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=2)  
    cmd = parts[0].lower()  
    args = parts[1:] if len(parts) > 1 else []  
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all_contacts(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

