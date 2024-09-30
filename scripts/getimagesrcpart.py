import re
import json

# Define the regex pattern
pattern = r'(?<=\?i=)[^\"\s]+';

try:
    # Open the file and read its contents
    with open('test.txt', 'r') as file:
        content = file.read()

    # Find all matches and store them in a list
    matches_list = []
    matches = re.findall(pattern, content)
    matches_list.extend(matches)

    print(matches_list)

except FileNotFoundError:
    print("Error: The file 'test.txt' was not found.")
except IOError as e:
    print(f"Error reading the file: {e}")
except re.error as e:
    print(f"Regex error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
