#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists
if not path.exists(filename):
    # Create an empty list if the file doesn't exist
    data = []
else:
    # Load the existing data from the file
    data = load_from_json_file(filename)

# Add command line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(data, filename)
