def get_valid_input():
    return

def process_delivery(current_total, new_value):
    return

def calculate_tax(amount):
    return

def generate_report(total_units, failed_attempts):
    print("Total units processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

    return

total_units = 0
failed_attempts = 0

while True:
    userInput = input("Enter a stock quantity (enter 'quit' to quit): ")
    if userInput.lower() == "quit":
        break
    elif not userInput.isdigit() or int(userInput) < 0:
        failed_attempts += 1
        print("invalid stock value")
    else:
        total_units += int(userInput)
        if total_units > 500:
            print("Alert! Total Inventory Exceeding 500!")
            break

generate_report(total_units, failed_attempts)