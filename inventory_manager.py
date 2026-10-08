import json

fp = "inventory.json"

def add_product(item):
    if item:
        inventory.append(item)
    return

def update_stock(item):
    if item:
        print(f"""\nProduct Found:
Name: {item.get("name")}
Current Stock: {item.get("stock")}\n""")
        new_stock = input("New Stock Quantity: ")
        if not new_stock.isdigit() or int(new_stock) < 0:
            print("Invalid Stock Quantity.")
        else:
            item["stock"] = new_stock
            print("\nStock Updated Successfully!\n")
    return

def search_product(product_id, display: bool = True):
    for item in inventory:
        if item.get("id") == product_id:
            if display:
                print(f"""\nProduct Found\n{"-" * 25}
ID: {item.get("id")}
Name: {item.get("name")}
Price: ${item.get("price")}
Stock: {item.get("stock")}
{"-" * 25}\n""")
            return item
    if display:
        print("\nProduct Not Found.\n")
    return None

def display_all():
    print(f"\nCurrent Inventory\n{"-" * 25}")
    if len(inventory) == 0:
        print("Current Inventory is Empty!")
    else:
        for item in inventory:
            print(f"ID: {item.get("id")} | Name: {item.get("name")} | Price: {float(item.get("price")):.2f} | Stock: {item.get("stock")}")
    print(f"{"-" * 25}\n")
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
            print("\nAdd New Product")
            add_product()
        elif option == "3":
            print("\nUpdate Stock")
            item = search_product(input("Enter Product ID: "), False)
            update_stock(item)
        elif option == "4":
            print("\nSearch Product")
            search_product(input("Enter Product ID: "))
        elif option == "5":
            save_inventory()
    else:
        print("Invalid Option\n")

save_inventory()
