import json

from inventory import Inventory
from product import Product
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct


class File:
    def __init__(self, filepath: str = "inventory.json"):
        self.__filepath = filepath

    def load_inventory(self) -> list[Product]:
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
            weight = item.get("weight", None)
            download_size = item.get("download_size", None)
            if product_id is None or name is None or price is None or stock is None or (weight is None and download_size is None):
                continue # faulty entry
            if weight:
                inventory.append(PhysicalProduct(product_id, name, price, stock, weight))
            elif download_size:
                inventory.append(DigitalProduct(product_id, name, price, stock, download_size))
        return inventory

    def save_inventory(self, inventory:Inventory, exiting: bool) -> None:
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
