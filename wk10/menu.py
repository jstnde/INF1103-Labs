from file import File
from inventory import Inventory
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct


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
    def status(self) -> bool:
        return self.__status

    def display_menu(self) -> None:
        print(f"{"-" * 7} MENU {"-" * 7}")
        for key, val in self.__options.items():
            print(f"{key}. {val}")
        print(f"{"-" * 20}\n")

    def is_valid_option(self, option: str) -> bool:
        return option in self.__options.keys()

    def execute_option(self, option:str, file:File, inventory:Inventory) -> None:
        if option == "6":
            self.save_inventory(file, inventory, exiting=True)
            self.__status = False
        if option == "1":
            self.display_all_products(inventory)
        elif option == "2":
            self.add_product(inventory)
        elif option == "3":
            self.update_stock(inventory)
        elif option == "4":
            self.search_product(inventory)
        elif option == "5":
            self.save_inventory(file, inventory)

    @staticmethod
    def display_all_products(inventory:Inventory) -> None:
        print(f"\nCurrent Inventory\n{"-" * 25}")
        inventory.display_all()
        print(f"{"-" * 25}\n")

    @staticmethod
    def add_product(inventory:Inventory) -> None:
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

        product_type = input("Product Type (physical: 0, digital: 1): ")
        if product_type == "0":
            weight = input("Weight (kg): ")
            if not weight.isdigit() or int(weight) < 0:
                print("Invalid Weight Value.\n")
                return
            product = PhysicalProduct(product_id, name, float(price), int(stock), int(weight))
        elif product_type == "1":
            download_size = input("Download Size (MB): ")
            if not download_size.isdigit() or int(download_size) < 0:
                print("Invalid Download Size.\n")
                return
            product = DigitalProduct(product_id, name, float(price), int(stock), int(download_size))
        else:
            print("Invalid product type.\n")
            return

        inventory.add_product(product)
        print("\nProduct added successfully!\n")

    @staticmethod
    def update_stock(inventory:Inventory) -> None:
        print("\nUpdate Stock")
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)
        if product is not None:
            quantity = input("New Stock Quantity: ")
            if not quantity.isdigit() or int(quantity) < 0:
                print("Invalid Stock Quantity.")
            else:
                product.update_stock(int(quantity))
                print("\nStock updated successfully!\n")

    @staticmethod
    def search_product(inventory:Inventory) -> None:
        print("\nSearch Product")
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)
        if product is not None:
            product.display_information()

    @staticmethod
    def save_inventory(file:File, inventory:Inventory, exiting:bool = False) -> None:
        file.save_inventory(inventory, exiting)
