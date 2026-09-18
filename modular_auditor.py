def get_valid_input():
    return

def process_delivery(current_total, new_value):
    return

def calculate_tax(amount):
    return

def generate_report(total_units, failed_attempts):
    return

inventory = 0
retries = 0

while True:
    userInput = input("Enter a stock quantity (enter 'quit' to quit): ")
    if userInput.lower() == "quit":
        break
    elif not userInput.isdigit() or int(userInput) < 0:
        retries += 1
        print("invalid stock value")
    else:
        inventory += int(userInput)
        if inventory > 500:
            print("Alert! Total Inventory Exceeding 500!")
            break

print("Total units processed: ", inventory)
print("Number of Failed/Rejected Entries: ", retries)