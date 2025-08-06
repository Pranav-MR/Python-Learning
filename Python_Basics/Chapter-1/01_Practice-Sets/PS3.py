# Importing the built-in 'os' module to interact with the operating system
import os

# Define a function to list and print all contents of a given directory
def list_directory(path='.'):  # Default path is the current directory ('.')
    """
    Prints all items in the given directory path.
    If no path is given, it lists the contents of the current directory.
    """
    try:
        # Try to get the list of entries (files/folders) in the directory
        entries = os.listdir(path)
    except OSError as e:
        # Handle any OS-related error (e.g., directory not found, no permission)
        print(f"Error accessing directory '{path}': {e}")
        return

    # Print the contents of the directory
    print(f"Contents of '{path}':")
    for name in entries:
        # Print each entry (could be file or subdirectory)
        print(name)

# This block only runs when the script is executed directly (not when imported as a module)
if __name__ == '__main__':
    dir_path = '.'  # You can change this to any other directory path
    list_directory(dir_path)  # Call the function to list contents
