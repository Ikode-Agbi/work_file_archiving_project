# Portico Archiving Automation

## The Problem

I work with MMCTS (Multimedia Manual of Cardiothoracic Surgery), a peer-reviewed medical journal that publishes step-by-step surgical technique tutorials. 

To comply with PubMed indexing requirements, all published MMCTS content must be archived to Portico for long-term digital preservation. This archiving process requires uploading exactly 3 files for each manuscript:
- **PDF** - The tutorial document (created and sent to us by our partners wont discole the name)
- **MP4** - The surgical technique video
- **XML** - The article metadata

These files must be organised into individual folders (one per manuscript), zipped together, and uploaded via FTP to Portico.

### The Manual Process Was Tedious

Before this script, the archiving workflow looked like this:

1. list of published manuscripts pdfs are provided by partner comany 
2. Open the Work In Progress (WIP) folder containing manusccript files
3. Manually find each manuscript folder (named like "MMCTS-2025-101-AuthorName") that correspnd to the list of porvided pdfs
4. Create a new folder with just the manuscript ID (without the author name)
5. Copy the XML and MP4 files from the manuscript folder
6. Navigate to an FTP folder where the pdfs provded by Cardio Projects are saved
7. Find the matching PDF and copy it into the new folder
10. Repeat for each manuscript
11. Zip each folder
12. Upload to FileZilla

For multiple manuscripts, this meant lots of clicking, copying, pasting, and double-checking to make sure nothing was missed. It was time-consuming and error-prone. As there were large mp4 files being copied i had to wait up to 5 minutes per manuscript. I would archive in a month between 20-35 manuscripts. So this mannual work could take me up to 3 hours per month. 

### The Solution

I wanted to solve this problem using Python. This script automates the entire organisation process, turning hours of manual work into a single command, allowing the archiving to occur in the background. 

## What This Script Does

The script automatically:
1. Identifies manuscript folders from the WIP directory that need archiving
2. Creates new folders named by manuscript ID only (removing author names)
3. Finds and moves the corresponding PDF from the PDF folder
4. Copies the XML and MP4 files from the manuscript's WIP folder
5. Moves all organised folders to the FTP directory, ready for zipping and upload

## Requirements

- Python 3.x
- Standard libraries: `os`, `shutil`, `zipfile`

No additional installations needed!

