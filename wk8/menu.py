from file import File
from inventory import Inventory
from product import Product


def display_all_products(inventory:Inventory):
    print(f"\nCurrent Inventory\n{"-" * 25}")
    inventory.display_all()
    print(f"{"-" * 25}\n")


def add_product(inventory:Inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    if inventory.search_product(product_id):
        print("Product ID already exists!\n")
        return
    name = input("Product Name: ")
    price = input("Price: ")
    try:
        if float(price) < 0:
            raise ValueError("Invalid price")
    except:
        print("Invalid Price.\n")
        return
    stock = input("Stock Quantity: ")
    if not stock.isdigit() or int(stock) < 0:
        print("Invalid Stock Quantity.\n")
        return
    product = Product(product_id, name, float(price), int(stock))

    inventory.add_product(product)
    print("\nProduct added successfully!\n")


def update_stock(inventory:Inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is not None:
        quantity = input("New Stock Quantity: ")
        if not quantity.isdigit() or int(quantity) < 0:
            print("Invalid Stock Quantity.")
        else:
            product.update_stock(quantity)
            print("\nStock updated successfully!\n")


def search_product(inventory:Inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is not None:
        product.display_information()


def save_inventory(file:File, inventory:Inventory, exiting:bool = False):
    file.save_inventory(inventory, exiting)


class Menu:
    def __init__(self):
        self.__options = {
            "1": "Display All Products",
            "2": "Add Product",
            "3": "Update Stock",
            "4": "Search Product",
            "5": "Save Inventory",
            "6": "Exit"
        }
        self.__status = True # Continue: True, Exit: False

    @property
    def status(self):
        return self.__status

    def display_menu(self):
        print(f"{"-" * 7} MENU {"-" * 7}")
        for key, val in self.__options.items():
            print(f"{key}. {val}")
        print(f"{"-" * 20}\n")

    def is_valid_option(self, option) -> bool:
        return option in self.__options.keys()

    def execute_option(self, option:str, file:File, inventory:Inventory):
        if option == "6":
            save_inventory(file, inventory, exiting=True)
            self.__status = False
        if option == "1":
            display_all_products(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            save_inventory(file, inventory)
