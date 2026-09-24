def get_valid_input():
    userInput = input("Enter a stock quantity (enter 'quit' to quit): ")

    if userInput.lower() == "quit":
        return None
    elif not userInput.isdigit() or int(userInput) < 0:
        print("invalid stock value")
        return -1
    else:
        return int(userInput)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * .1

def generate_report(total_units, failed_attempts):
    print("Total units processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

    return

total_units = 0
failed_attempts = 0

# create load inventory
# create save inventory

# at start, attempt to load inventory,
# if inventory file does not exist, start with an empty inventory

while True:
    valid_input = get_valid_input()
    if not valid_input:
        # save final total and the transaction history list to inventory.txt
        break
    elif valid_input < 0:
        failed_attempts += 1
    else:
        total_units = process_delivery(total_units, valid_input)
        # use list to store every valid transaction amount entered
        print("current calculated tax: ", calculate_tax(total_units))
        if total_units > 500:
            print("Alert! Total Inventory Exceeding 500!")
            break

generate_report(total_units, failed_attempts)