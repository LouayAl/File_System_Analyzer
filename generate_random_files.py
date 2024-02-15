import os
import random
import string

def generate_random_string(length):
    """
    Generate a random string of specified length.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_file(directory, file_count):
    """
    Generate random files with random content.
    """
    for i in range(file_count):
        file_name = f"file_{i+1}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            file.write(generate_random_string(random.randint(50, 200)))  # Random content length

def generate_random_folder(directory, folder_count, file_count_per_folder):
    """
    Generate random folders with random files inside them.
    """
    for i in range(folder_count):
        folder_name = f"folder_{i+1}"
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path)
        generate_random_file(folder_path, file_count_per_folder)

def main():
    directory = input("Enter the directory path to generate random files and folders: ")
    folder_count = int(input("Enter the number of folders to generate: "))
    file_count_per_folder = int(input("Enter the number of files per folder to generate: "))

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate random folders and files
    generate_random_folder(directory, folder_count, file_count_per_folder)

    print(f"Random files and folders generated successfully in {directory}.")

if __name__ == "__main__":
    main()
