import json

from inventory import Inventory
from product import Product


class File:
    def __init__(self, filepath = "inventory.json"):
        self.__filepath = filepath

    def load_inventory(self):
        try:
            with open(self.__filepath, "r") as file:
                unprocessed_inventory = json.load(file)
                if type(unprocessed_inventory) is not list:
                    raise Exception
                print(f"{self.__filepath} found.\nInventory loaded successfully.\n")
        except FileNotFoundError, Exception:
            return list()

        inventory = list()
        for item in unprocessed_inventory:
            product_id = item.get("product_id", None)
            name = item.get("name", None)
            price = item.get("price", None)
            stock = item.get("stock", None)
            if product_id is None or name is None or price is None or stock is None:
                continue # faulty entry
            inventory.append(Product(product_id, name, price, stock))
        return inventory

    def save_inventory(self, inventory:Inventory, exiting):
        if exiting:
            print("\nSaving inventory before exit...")
        else:
            print("\nSaving inventory...")

        with open(self.__filepath, "w") as file:
            json.dump(inventory.__dict__(), file, indent=1)

        if exiting:
            print("Inventory saved successfully.\n")
        else:
            print(f"Inventory saved successfully to {self.__filepath}.\n")
