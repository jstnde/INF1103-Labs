from file import File
from inventory import Inventory
from menu import Menu

file = File()
inventory = Inventory(file.load_inventory())
menu = Menu()

menu.display_menu()
while menu.status:
    try:
        option = input("Enter option: ")
        if menu.is_valid_option(option):
            menu.execute_option(option, file, inventory)
        else:
            print("Invalid Option\n")
    except KeyboardInterrupt, EOFError:
        break

print("Thank you for using Inventory Management System.")
print("Program Terminated.")
