import pandas as pd
import pyperclip

# Load the Excel file
file_path = './file1.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Extract the 'Username' column
usernames = df['Username']

# Convert the usernames to a single string with each username on a new line
usernames_str = '\n'.join(usernames.dropna().astype(str))

# Copy the usernames to the clipboard
pyperclip.copy(usernames_str)

print("Usernames have been copied to the clipboard.")

