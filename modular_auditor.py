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
    return

def generate_report(total_units, failed_attempts):
    print("Total units processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

    return

total_units = 0
failed_attempts = 0

while True:
    valid_input = get_valid_input()
    if not valid_input:
        break
    elif valid_input < 0:
        failed_attempts += 1
    else:
        total_units = process_delivery(total_units, valid_input)
        if total_units > 500:
            print("Alert! Total Inventory Exceeding 500!")
            break

generate_report(total_units, failed_attempts)