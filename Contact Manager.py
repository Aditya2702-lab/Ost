
contacts={}
def add_contact(key, no):
    contacts.update({key : no})
def search_contact(key):
    if key in contacts:
        print(f"Contact found : {contacts[key]}")
    else:
        print("Contact not found!")
def view_all_contacts(contact):
    print("Available contacts : ")
    for i in contact:
        print(i)
def delete_contact(contact,key):
    del contact[key]
    print(f"contact {key} is deleted!")

while True:
    print("******** Your Contact Manager ********")
    ch=int(input("New Contact : 1\nSearch Contact : 2\nView all contacts : 3\nDelete contact : 4\nExit : 5\nEnter your choice :  "))
    if ch==5:
        break

    match ch:
        case 1:
            name =input("Name : ")
            num = int(input("Contact :"))
            add_contact(name,num)
            print("Contact added successfully!")
        case 2 :
            k=input("Enter the name to find contact : ")
            search_contact(k)
        case 3 :
            if len(contacts)==0:
                print("You don't have any contacts saved!")
            else:
                view_all_contacts(contacts)
        case 4 :
            n=input("Enter contact to delete : ")
            if n in contacts:
                delete_contact(contacts,n)
            else:
                print(f"{n} is not found!")

        case _:
            print("Invalid choice!, please enter a valid choice.")



