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

# Copy the result to the clipboard
pyperclip.copy(result)

print("Usernames have been extracted, sorted, and copied to the clipboard.")

