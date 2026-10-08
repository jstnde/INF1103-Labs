import json

fp = "inventory.json"

def add_product():
    return

def update_stock():
    return

def search_product():
    return

def display_all():
    return

def get_valid_input():
    product_name = input("Enter Product Name (enter 'quit' to quit): ")

    if product_name.lower() == "quit":
        return None

    quantity = input("Enter Quantity: ")

    if not quantity.isdigit() or int(quantity) < 0:
        print("invalid quantity value\n")
        return -1
    else:
        return product_name, int(quantity)

def process_order(current_total, inventory, last_id, valid_input):
    last_id += 1
    inventory.append((str(last_id), valid_input[0], str(valid_input[1])))
    
    print("\nNew Order Added: ")
    print(inventory[-1][0] + ", " + inventory[-1][1] + ", " + inventory[-1][2] + "\n")

    return last_id, current_total + valid_input[1]

def generate_report(total_units, failed_attempts):
    print("Total units processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

    return

def load_inventory():
    try:
        with open(fp, "r") as file:
            inventory = json.load(file)
        print(f"{fp} found.\nInventory loaded successfully.\n")
    except FileNotFoundError:
        return list()
    return inventory

def save_inventory():
    with open(fp, "w") as file:
        json.dump(inventory, file)
    return

print("="*30)
print("INVENTORY MANAGEMENT SYSTEM")
print("="*30)

inventory = load_inventory()

options = {
    "1": "Display All Products",
    "2": "Add Product",
    "3": "Update Stock",
    "4": "Search Product",
    "5": "Save Inventory",
    "6": "Exit"
}

print(f"{"-" * 7} MENU {"-" * 7}")
for key, val in options.items():
    print(f"{key}. {val}")
print(f"{"-" * 20}\n")

while True:
    option = input("Enter option: ")
    if option in options.keys():
        if option == "6":
            break
        if option == "1":
            display_all()
        elif option == "2":
            add_product()
        elif option == "3":
            update_stock()
        elif option == "4":
            search_product()
        elif option == "5":
            save_inventory()
    else:
        print("Invalid Option\n")

save_inventory()
