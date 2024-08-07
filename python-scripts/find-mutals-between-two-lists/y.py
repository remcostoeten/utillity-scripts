import pandas as pd
import pyperclip
import os

# Define the filenames
filename1 = "file1.xlsx"
filename2 = "file2.xlsx"

# Check if the files exist in the current directory
if not os.path.isfile(filename1):
    print(f"{filename1} not found in the current directory.")
    exit()
if not os.path.isfile(filename2):
    print(f"{filename2} not found in the current directory.")
    exit()

# Load the Excel files
df1 = pd.read_excel(filename1)
df2 = pd.read_excel(filename2)

# Extract the 'Username' columns
usernames1 = df1['Username'].dropna()
usernames2 = df2['Username'].dropna()

# Find mutual usernames
mutual_usernames = set(usernames1) & set(usernames2)

# Sort the mutual usernames
sorted_mutual_usernames = sorted(mutual_usernames)

# Convert the list to a single string with each username on a new line
result = '\n'.join(sorted_mutual_usernames)

# Attempt to copy the result to the clipboard
try:
    pyperclip.copy(result)
    print("Mutual usernames have been extracted, sorted, and copied to the clipboard.")
except pyperclip.PyperclipException as e:
    print(f"Failed to copy to clipboard: {e}")
    print("Ensure you have 'xclip' or 'xsel' installed on your system.")
    print("To install, run: sudo apt-get install xclip or sudo apt-get install xsel")

