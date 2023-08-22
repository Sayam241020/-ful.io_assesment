import re

def validate_contact_number(number):
    # Regular expression to match valid phone number formats
    pattern = r'^\+?\d?[-\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}?'
    
    # Match the given number against the pattern
    match = re.match(pattern, number)
    
    if match:
        return True
    else:
        return False

# List of example contact numbers
contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

# Validate and print the results
for number in contact_numbers:
    if validate_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
