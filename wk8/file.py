import json


class File:
    def __init__(self, filepath = "inventory.json"):
        self.__filepath = filepath

    def load_inventory(self):
        try:
            with open(self.__filepath, "r") as file:
                inventory = json.load(file)
                print(f"{self.__filepath} found.\nInventory loaded successfully.\n")
        except FileNotFoundError:
            return list()
        return inventory

    def save_inventory(self, inventory, exiting):
        if exiting:
            print("\nSaving inventory before exit...")
        else:
            print("\nSaving inventory...")

        with open(self.__filepath, "w") as file:
            json.dump(inventory, file, indent=1)

        if exiting:
            print("Inventory saved successfully.\n")
        else:
            print(f"Inventory saved successfully to {self.__filepath}.\n")
