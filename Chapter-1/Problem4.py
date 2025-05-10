import os

# Get the directory path from the user or use current directory
directory = 'D:\\Users'

# Use current directory if input is blank
if not directory:
    directory = os.getcwd()

try:
    # List all files and directories
    contents = os.listdir(directory)
    print(f"\nContents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
except Exception as e:
    print(f"An error occurred: {e}")
