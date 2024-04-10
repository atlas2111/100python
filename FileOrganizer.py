import os
import shutil


def organize_files(source_dir):
    # Define destination directories for different file types
    file_types = {
        '.txt': 'TextFiles',
        '.jpg': 'Images',
        '.png': 'Images',
        '.pdf': 'PDFs',
        '.mp4': 'Videos',
        # Add more file types and corresponding directories as needed
    }

    # Create destination directories if they don't exist
    for directory in file_types.values():
        os.makedirs(os.path.join(source_dir, directory), exist_ok=True)

    # List all files in the source directory
    files = os.listdir(source_dir)

    # Organize files
    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):
            _, ext = os.path.splitext(file)
            ext = ext.lower()  # Normalize file extension to lowercase

            # Move file to its corresponding directory
            if ext in file_types:
                dest_dir = os.path.join(source_dir, file_types[ext])
                shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
                print(f"Moved {file} to {dest_dir}")


if __name__ == "__main__":
    source_directory = input("Enter the path of the directory to organize: ")
    organize_files(source_directory)
