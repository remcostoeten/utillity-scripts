import pandas as pd
import pyperclip
from pathlib import Path

# Define the path to your Excel file
file_path = Path('./file.xlsx')  # Replace with your actual file path

# Load the Excel file
df = pd.read_excel(file_path)

# Extract the 'Username' column and drop any NaN values
usernames = df['Username'].dropna().astype(str)

# Sort the usernames
sorted_usernames = usernames.sort_values()

# Convert the sorted usernames to a single string with each username on a new line
usernames_str = '\n'.join(sorted_usernames)

# Copy the sorted usernames to the clipboard
pyperclip.copy(usernames_str)

print("Sorted usernames have been copied to the clipboard.")

