from manager import PasswordManager
import cli
manager=PasswordManager()
cli.run(manager)

# manager.add_entry("github.com", "aurora", "abc123")
# manager.add_entry("gmail.com", "aurora@gmail.com", "xyz789")
# entries=manager.list_entries()
# for entry in entries:
#   print(entry)