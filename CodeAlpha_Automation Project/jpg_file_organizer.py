import os
import shutil


def validate_source_folder(source_folder):
    if not os.path.exists(source_folder):
        return False, "Source folder does not exist."
    if not os.path.isdir(source_folder):
        return False, "Source path is not a directory."
    return True, ""


def create_destination_folder(destination_folder):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        return True, ""
    except Exception as e:
        return False, f"Failed to create destination folder: {e}"


def find_jpg_files(source_folder):
    jpg_files = []
    try:
        for filename in os.listdir(source_folder):
            filepath = os.path.join(source_folder, filename)
            if os.path.isfile(filepath) and filename.lower().endswith('.jpg'):
                jpg_files.append(filename)
    except Exception as e:
        print(f"Error reading source folder: {e}")
    return jpg_files


def get_unique_destination_path(destination_folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1
    return os.path.join(destination_folder, new_filename), new_filename


def move_jpg_files(source_folder, destination_folder, jpg_files):
    moved_files = []
    failed_files = []
    
    for filename in jpg_files:
        source_path = os.path.join(source_folder, filename)
        try:
            dest_path, dest_filename = get_unique_destination_path(destination_folder, filename)
            shutil.move(source_path, dest_path)
            moved_files.append(dest_filename)
        except Exception as e:
            failed_files.append((filename, str(e)))
    
    return moved_files, failed_files


def display_summary(jpg_files, moved_files, failed_files):
    print("\n" + "=" * 38)
    print("             SUMMARY")
    print("=" * 38)
    print()
    print(f"Files found : {len(jpg_files)}")
    print(f"Files moved : {len(moved_files)}")
    print(f"Files failed: {len(failed_files)}")
    print()
    if moved_files:
        print("Moved files:")
        for f in moved_files:
            print(f"  - {f}")
    if failed_files:
        print("Failed files:")
        for f, err in failed_files:
            print(f"  - {f}: {err}")
    print()
    if len(moved_files) > 0 and len(failed_files) == 0:
        print("JPG files organized successfully.")
    elif len(moved_files) > 0 and len(failed_files) > 0:
        print("JPG files organized with some failures.")
    else:
        print("No JPG files were moved.")
    print("=" * 38)


def main():
    print("=" * 38)
    print("       JPG FILE ORGANIZER")
    print("=" * 38)
    print()
    
    source_folder = input("Enter source folder path: ").strip()
    print()
    
    valid, error = validate_source_folder(source_folder)
    if not valid:
        print(f"Error: {error}")
        return
    
    destination_folder = input("Enter destination folder path: ").strip()
    print()
    
    valid, error = create_destination_folder(destination_folder)
    if not valid:
        print(f"Error: {error}")
        return
    
    jpg_files = find_jpg_files(source_folder)
    
    if not jpg_files:
        print("No JPG files found in the source folder.")
        return
    
    print(f"Found {len(jpg_files)} JPG file(s).")
    print()
    
    moved_files, failed_files = move_jpg_files(source_folder, destination_folder, jpg_files)
    
    for filename in moved_files:
        print(f"Moved: {filename}")
    
    display_summary(jpg_files, moved_files, failed_files)


if __name__ == "__main__":
    main()
