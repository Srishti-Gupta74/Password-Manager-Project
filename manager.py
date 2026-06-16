from models import PasswordEntry
class PasswordManager:
    def __init__(self):
        self.entries=[]

    def add_entry(self, website, username, password):
        new_entry=PasswordEntry(website, username, password)
        self.entries.append(new_entry) 

    def list_entries(self):
        return self.entries

    def delete_entries(self, index):
        del (self.entries[index])       