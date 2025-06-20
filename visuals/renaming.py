import os
import re

def rename_png_files(folder_path):
    # Regular expression pattern to match the UUID prefix and capture the remaining numbers
    pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}-(\d+)(\.png)$', re.IGNORECASE)
    
    # Get all PNG files in the folder
    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
    
    for filename in png_files:
        match = pattern.match(filename)
        if match:
            # Extract the number and extension
            number = match.group(1)
            extension = match.group(2)
            
            # Create new filename
            new_filename = f"{number}_w{extension}"
            
            # Rename the file
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Skipped (doesn't match pattern): {filename}")

if __name__ == "__main__":
    folder_path = "D:/pomodoro-timer/visuals/waiting_shadow/"
    if os.path.isdir(folder_path):
        rename_png_files(folder_path)
        print("Renaming complete!")
    else:
        print("Error: The specified path is not a valid directory.")