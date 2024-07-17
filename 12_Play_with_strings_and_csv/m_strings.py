import re

def extract_characters(input_string):
    # Define the pattern to match only characters 1-9 and a-z
    pattern = re.compile(r'[1-9a-z]')
    # Find all characters that match the pattern
    matches = pattern.findall(input_string.lower())
    # Join the matched characters into a single string
    result = ''.join(matches)
    return result


def extract_characters2(input_string):
    allowed_characters = "123456789abcdefghijklmnopqrstuvwxyz"
    result = ''.join([char for char in input_string.lower() if char in allowed_characters])
    return result


def extract_characters3(input_string):
    # Define the allowed characters
    allowed_characters = "123456789abcdefghijklmnopqrstuvwxyz"
    
    # Initialize an empty string to store the result
    result = ""
    
    # Loop through each character in the input string
    for char in input_string.lower():
        # Check if the character is in the allowed characters
        if char in allowed_characters:
            # If it is, add it to the result string
            result += char
    
    return result

# Example usage
random_string = "abc123XYZ!@#def456"
filtered_string = extract_characters(random_string)
filtered_string2 = extract_characters2(random_string)
filtered_string3 = extract_characters3(random_string)
print(filtered_string)  
print(filtered_string2)  
print(filtered_string3)  
