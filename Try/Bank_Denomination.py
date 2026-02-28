def compute_change(amount):
    # Define available denominations
    denominations = [500, 200, 100, 50, 20, 10]
    
    # Dictionary to hold the count of each denomination
    change = {}
    
    for denomination in denominations:
        if amount >= denomination:
            count = amount // denomination  # Determine how many of this denomination
            change[denomination] = count     # Store the count
            amount -= count * denomination     # Reduce the amount accordingly
    
    # Check for the highest denomination available 
    # If we can't use 500, show in terms of 100s leading downwards
    if change.get(500) is None:
        if change.get(200) is None:
            if change.get(100) is None:
                if change.get(50) is None:
                    if change.get(20) is None:
                        if change.get(10) is None:
                            return f"No denominations available to construct {amount} rupees."
    
    return change

# Input amount
amount_input = int(input("Enter the amount in rupees: "))
change_output = compute_change(amount_input)

# Display the result
result = []
for denomination, count in change_output.items():
    result.append(f"{count} x {denomination}")

# Join the result list into a single string for output
output_message = ", ".join(result)
print(output_message)