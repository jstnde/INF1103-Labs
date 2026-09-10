inventory = 0

while True:
    userInput = input("enter a stock quantity (enter 'quit' to quit)")
    if userInput == "quit":
        break
    elif not userInput.isdigit() or int(userInput) < 0:
        print("invalid stock value")
    else:
        inventory += int(userInput)
        if inventory > 500:
            print("Alert! Total Inventory Exceeding 500!")
            break