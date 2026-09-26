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

def process_order(current_total, new_value):
    return current_total + new_value

def generate_report(total_units, failed_attempts):
    print("Total units processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

    return

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory = file.read().split("\n")
    except FileNotFoundError:
        return list()
    return inventory

def save_inventory(inventory):
    with open("inventory.txt", "a") as file:
        for item in inventory:
            file.write(item[0] + "," + item[1] + "," + item[2] + "\n")
    return

inventory = []
total_units = 0
failed_attempts = 0

print("Current Orders:\n")
for order in load_inventory():
    item = order.split(",")
    print(item[0] + ", " + item[1] + ", " + item[2])
    total_units += int(item[-1])
print()

while True:
    valid_input = get_valid_input()
    if not valid_input:
        # save final total and the transaction history list to inventory.txt
        break
    elif valid_input == -1:
        failed_attempts += 1
    else:
        total_units = process_order(total_units, valid_input[1])
        # use list to store every valid transaction amount entered

generate_report(total_units, failed_attempts)