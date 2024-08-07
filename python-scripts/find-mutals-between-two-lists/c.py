
import pandas as pd
import pyperclip
import os

# Define the filename
filename = "file.xlsx"

# Check if the file exists in the current directory
if not os.path.isfile(filename):
    print(f"{filename} not found in the current directory.")
    exit()

# Load the Excel file
df = pd.read_excel(filename)

# Extract the 'Username' column
usernames = df['Username']

# Drop NaN values if any
usernames = usernames.dropna()

# Sort the usernames
sorted_usernames = sorted(usernames)

# Convert the list to a single string with each username on a new line
result = '\n'.join(sorted_usernames)

# Attempt to copy the result to the clipboard
try:
    pyperclip.copy(result)
    print("Usernames have been extracted, sorted, and copied to the clipboard.")
except pyperclip.PyperclipException as e:
    print(f"Failed to copy to clipboard: {e}")
    print("Ensure you have 'xclip' or 'xsel' installed on your system.")
    print("To install, run: sudo apt-get install xclip or sudo apt-get install xsel")
