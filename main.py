"""
This program calculates prices for custom house signs.
"""

def calculate_charge(numChars, color, woodType):
    # Declare and initialize the charge
    charge = 35.00  # Minimum charge for all signs

    # Charge for additional characters
    if numChars > 5:
        charge += (numChars - 5) * 4

    # Charge for wood type
    if woodType == "oak":
        charge += 20.00
    # No additional charge for pine

    # Charge for character color
    if color == "gold":
        charge += 15.00
    
    return charge

# User input for testing
numChars = int(input("Enter the number of characters: "))
woodType = input("Enter the wood type (oak/pine): ").lower()
color = input("Enter the character color (black/gold): ").lower()

# Calculate charge based on user inputs
charge = calculate_charge(numChars, color, woodType)

# Output the charge for the sign
print("The charge for this sign is ${:.2f}".format(charge))
