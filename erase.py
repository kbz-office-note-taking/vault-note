import os
import shutil

def delete_paths(file_path):
    # Check if the file with paths exists
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' does not exist.")
        return

    # List to hold paths that couldn't be deleted
    remaining_paths = []

    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Strip any whitespace or newline characters
            path = line.strip()
            
            # Check if the path is a directory
            if os.path.isdir(path):
                try:
                    # Delete the directory
                    shutil.rmtree(path)
                    print(f"Deleted directory: {path}")
                except Exception as e:
                    print(f"Error deleting directory {path}: {e}")
                    remaining_paths.append(path)  # Add to list if deletion fails

            # Check if the path is a file
            elif os.path.isfile(path):
                try:
                    # Delete the file
                    os.remove(path)
                    print(f"Deleted file: {path}")
                except Exception as e:
                    print(f"Error deleting file {path}: {e}")
                    remaining_paths.append(path)  # Add to list if deletion fails

            # If the path does not exist, add to remaining paths
            else:
                print(f"Path not found: {path}")
                remaining_paths.append(path)

    # Rewrite the file with only remaining paths
    with open(file_path, 'w') as file:
        for path in remaining_paths:
            file.write(path + '\n')

# Specify the path to 'deleted_these.txt'
file_path = 'delete_these.txt'

# Run the function
delete_paths(file_path)
