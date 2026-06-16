def add_password(manager):
    website=input("Enter website name")
    username=input("Enter username")
    password=input("Enter password")
    manager.add_entry(website, username, password)
    print("Password added successfully!")

def view_entries(manager):
    entries=manager.list_entries()
    if not entries:
        print("No passwords are saved")
    else:
        for number, entry in enumerate(entries, start=1):
            print(number, entry)
    
def del_entries(manager):
    entries=manager.list_entries()
    view_entries(manager)
    if not entries:
        print("Nothing to delete")
        return
    index=(int)(input("Enter the serial number you want to delete\n"))
    if index>0 and index<=len(entries):
        deleted_entry=entries[index-1]
        manager.delete_entries(index-1)
        print(f"Deleted {deleted_entry.website}")
                
    else:
        print ("Invalid index entered")

def run(manager):
    while True:
        choice=input("Enter your choice\n 1. Add Password\n 2. View Passwords\n 3. Exit\n")
        if choice=='1':
            add_password(manager)
        elif choice=='2':
            view_entries(manager)
        elif choice=='3':
            del_entries(manager)
        elif choice=='4':
            print("Exitting password manager")
            return
        else:
            print("Invalid choice entered")

