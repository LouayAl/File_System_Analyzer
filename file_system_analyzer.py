import os
import argparse
import magic


    """
    Classify the type of a file based on its extension or MIME type.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: The general type of the file based on its extension or MIME type.
    """
def classify_file_type(file_path):
    _, extension = os.path.splitext(file_path)
    if extension:
        return extension.lstrip('.')
    else:
        mime_type = magic.Magic(mime=True)
        file_type = mime_type.from_file(file_path)
        return file_type.split('/')[0] if '/' in file_type else file_type
        
#########################################################################################
    """
    Generate a report for files with unusual permissions.

    Args:
        file_path (str): Path to the file.
        permission (str): File permissions in octal format.
    """

def generate_permissions_report(file_path, permission):
    with open("permissions_report.txt", "a") as report_file:
        report_file.write(f"File: {file_path}\n")
        report_file.write(f"Permissions: {permission}\n\n")

#########################################################################################

    """
    Analyze a directory to identify file types, large files, and files with unusual permissions.

    Args:
        directory (str): Directory path to analyze.
        large_file_threshold (int): Threshold size for identifying large files (in bytes).

    Returns:
        dict: Dictionary containing file types and their total sizes.
        list: List of tuples containing paths and sizes of large files.
        int: Total number of files analyzed.
    """

def analyze_directory(directory, large_file_threshold):
    file_types = {}
    large_files = []
    total_files = 0

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            file_type = classify_file_type(file_path)

            # Update file type dictionary
            if file_type in file_types:
                file_types[file_type]["count"] += 1
                file_types[file_type]["total_size"] += file_size
            else:
                file_types[file_type] = {"count": 1, "total_size": file_size}

            # Check for large files
            if file_size > large_file_threshold:
                large_files.append((file_path, file_size))

            # Check for unusual permissions
            if os.stat(file_path).st_mode & 0o777 == 0o777:
                generate_permissions_report(file_path, oct(os.stat(file_path).st_mode)[-3:])

            total_files += 1

    return file_types, large_files, total_files

#########################################################################################
    
    """
    Main function to parse command-line arguments and initiate directory analysis.
    """

def main():
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="File System Analyzer")
    parser.add_argument("directory", nargs='?', help="Directory to analyze")
    parser.add_argument("--large-file-threshold", type=int, nargs='?', default=1000000,
                        help="Threshold size for identifying large files (in bytes)")
    args = parser.parse_args()

    # If required arguments are not provided, prompt the user for input
    if not args.directory or args.large_file_threshold is None:  # Check if directory argument is not provided or threshold is not provided
        print("Welcome to the File System Analyzer!")
        print("It looks like you didn't specify the directory or the large file threshold.")
        directory = args.directory if args.directory else input("Please enter the directory path to analyze: ")
        large_file_threshold = input("Please enter the threshold size for identifying large files (in bytes): ")
        args.directory = directory.strip() if directory else None
        args.large_file_threshold = int(large_file_threshold.strip()) if large_file_threshold else 1000000

    # Check if the provided path is a directory
    if not os.path.isdir(args.directory):
        print("Error: Invalid directory path.")
        return

    # Analyze the directory
    file_types, large_files, total_files = analyze_directory(args.directory, args.large_file_threshold)

    # Print file type analysis
    print("\nFile Type Analysis:\n")
    for file_type, data in file_types.items():
        print(f"{file_type}: {data['count']} files, Total Size: {data['total_size']} bytes")

    # Print total number of files
    print(f"\nTotal number of files analyzed: {total_files}")

    # Print large files or 0 if no large files found
    if large_files:
        print("\nLarge Files:")
        for file_path, file_size in large_files:
            print(f"{file_path}: {file_size} bytes")
    else:
        print("\nNo large files found.")

if __name__ == "__main__":
    main()
