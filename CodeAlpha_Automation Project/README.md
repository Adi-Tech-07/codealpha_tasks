# JPG File Organizer Automation

## Project Description

This is a Python console-based automation tool that helps organize JPG image files by moving them from a source folder to a dedicated destination folder. It was developed as part of the **CodeAlpha Python Programming Internship — Task 3**.

## CodeAlpha Internship Context

**Internship:** CodeAlpha Python Programming Internship  
**Task:** Task 3 — Automate a Repetitive Real-Life Task  
**Selected Option:** Move .jpg files automatically  

The Task 3 options provided by CodeAlpha were:
1. Move .jpg files automatically
2. Extract email addresses from a .txt file
3. Scrape the title of a fixed webpage

This project implements the first option: **JPG File Organizer Automation**.

## Objective

Create a Python program that:
- Accepts a source folder path from the user
- Validates that the source folder exists and is a directory
- Accepts a destination folder path
- Creates the destination folder automatically if it doesn't exist
- Finds all .jpg and .JPG files in the source folder
- Moves those JPG files to the destination folder using shutil
- Displays a clear summary of files found, moved, and any failures
- Handles common file-operation errors safely without unnecessary tracebacks
- Prevents accidental overwriting by generating unique filenames when conflicts exist

## Features

- **Source folder validation** — Checks existence and ensures it's a directory
- **Automatic destination creation** — Creates destination folder if missing
- **Case-insensitive JPG detection** — Recognizes both .jpg and .JPG extensions
- **Selective file moving** — Only moves JPG files; leaves all other file types untouched
- **Conflict resolution** — Generates unique names like photo_1.jpg, photo_2.jpg when a file already exists in destination
- **Clear summary output** — Shows counts of found, moved, and failed files
- **Error handling** — Handles invalid paths, permission errors, empty folders, and no-JPG cases gracefully
- **Beginner-friendly code** — Clean, modular, function-based structure using only Python standard library

## Technologies / Concepts Used

- **Python 3**
- **os module** — Filesystem operations, path handling, directory listing
- **shutil module** — Moving files safely
- **input() / print()** — Console interaction
- **Conditional statements** — Flow control
- **Loops** — Iterating over files
- **Functions** — Modular, reusable code organization
- **File/folder handling** — Reading, writing, moving files
- **Exception handling** — Safe error management without tracebacks

## Project Structure

`	ext
CodeAlpha_JPG_File_Organizer/
+-- PRD.md
+-- jpg_file_organizer.py
+-- README.md
+-- .gitignore
`

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## How to Run

1. Ensure Python 3 is installed on your system.
2. Open a terminal/command prompt.
3. Navigate to the project directory:
   `ash
   cd D:\Automation Project
   `
4. Run the program:
   `ash
   python jpg_file_organizer.py
   `

## How to Use

1. Run the program using the command above.
2. When prompted, enter the **source folder path** (the folder containing JPG files you want to organize).
3. When prompted, enter the **destination folder path** (where you want the JPG files to be moved).
4. The program will:
   - Validate the source folder
   - Create the destination folder if needed
   - Find all .jpg and .JPG files
   - Move them to the destination (with conflict handling)
   - Display a summary of the operation

## Example Input/Output

`	ext
======================================
       JPG FILE ORGANIZER
======================================

Enter source folder path: D:\TestImages
Enter destination folder path: D:\TestImages\JPG_Files

Found 3 JPG file(s).

Moved: photo1.jpg
Moved: photo2.JPG
Moved: holiday.jpg

======================================
             SUMMARY
======================================

Files found : 3
Files moved : 3
Files failed: 0

JPG files organized successfully.
======================================
`

### Example with Filename Conflict

If the destination already contains photo.jpg and the source also has photo.jpg:

`	ext
======================================
       JPG FILE ORGANIZER
======================================

Enter source folder path: D:\TestImages
Enter destination folder path: D:\TestImages\JPG_Files

Found 1 JPG file(s).

Moved: photo_1.jpg

======================================
             SUMMARY
======================================

Files found : 1
Files moved : 1
Files failed: 0

JPG files organized successfully.
======================================
`

### Example with No JPG Files

`	ext
======================================
       JPG FILE ORGANIZER
======================================

Enter source folder path: D:\EmptyFolder
Enter destination folder path: D:\EmptyFolder\JPG_Files

No JPG files found in the source folder.
`

### Example with Invalid Source Path

`	ext
======================================
       JPG FILE ORGANIZER
======================================

Enter source folder path: D:\NonExistentFolder
Enter destination folder path: D:\TestImages\JPG_Files

Error: Source folder does not exist.
`

## Error Handling

The program handles the following error cases gracefully:

| Error Case | Handling |
|------------|----------|
| Source folder doesn't exist | Clear error message, clean exit |
| Source path is not a directory | Clear error message, clean exit |
| Destination folder doesn't exist | Automatically created |
| Permission denied on source/destination | Error captured, file marked as failed, continues with other files |
| Empty source folder | Reports \"No JPG files found\", clean exit |
| No JPG files in source | Reports \"No JPG files found\", clean exit |
| Filename conflict in destination | Generates unique name (e.g., photo_1.jpg), no overwriting |
| File operation errors (locked file, etc.) | Captured per-file, summary shows failures |

## Testing Performed

All test cases from the PRD were executed and passed:

### Test 1 — Normal JPG Files
- **Source:** photo1.jpg, photo2.JPG, document.txt, image.png
- **Result:** Only photo1.jpg and photo2.JPG moved. Non-JPG files left untouched. ?

### Test 2 — No JPG Files
- **Source:** document.txt, image.png, data.csv
- **Result:** Clear message \"No JPG files found in the source folder.\" Clean exit. ?

### Test 3 — Invalid Source Folder
- **Source:** Non-existent path D:\NonExistentFolder
- **Result:** Clear error \"Source folder does not exist.\" No crash. ?

### Test 4 — Missing Destination
- **Destination:** Path that doesn't exist
- **Result:** Destination folder created automatically. ?

### Test 5 — Filename Conflict
- **Setup:** Destination already has photo.jpg, source has another photo.jpg
- **Result:** Source file moved as photo_1.jpg. No overwriting. ?

### Test 6 — Mixed File Types
- **Source:** photo.jpg, photo.JPG, image.jpeg, image.png, doc.pdf, data.txt
- **Result:** Only photo.jpg and photo.JPG moved. .jpeg, .png, .pdf, .txt left untouched. ?

### Test 7 — Empty Folder
- **Source:** Empty directory
- **Result:** Clean exit with \"No JPG files found\" message. ?

## Future Improvements

- Add support for recursive folder scanning (subdirectories)
- Add support for additional image formats (.jpeg, .png, .gif, etc.)
- Add command-line arguments for non-interactive use
- Add logging to file instead of only console output
- Add dry-run mode to preview changes without moving files
- Add progress bar for large numbers of files

## Author / Project Information

**Project:** CodeAlpha Python Programming Internship — Task 3  
**Project Name:** JPG File Organizer Automation  
**Author:** [Your Name]  
**Language:** Python 3  
**License:** Educational / Internship Project
