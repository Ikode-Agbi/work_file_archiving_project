# Medical Journal Archiving Automation

## The Problem

I work with MMCTS (Multimedia Manual of Cardiothoracic Surgery), a peer-reviewed video manual for cardiovascular and thoracic surgery and case reports. 
To comply with PubMed indexing requirements, all published MMCTS content must be archived for long-term digital preservation. This archiving process requires uploading exactly 3 files for each manuscript:
- **PDF** - The tutorial document (created and sent to us by a partnering company)
- **MP4** - The surgical tutorial/case report video
- **XML** - The article metadata

These files must be organised into individual folders (one per manuscript), zipped together, and uploaded to Filezilla.

### The Manual Process Was Tedious

Before this script, the archiving workflow looked like this:

1. **Manuscript published** - Once up to 10 manuscript has been published, a request is sent to our partner company to create PDF's of the list of manuscripts published
2. **Save  PDF's** - Once the pdfs are provided by partner company, I save them into a local File Transfer Protocol (FTP) folder (e.g c:\FTP\2025\Batch37\{PDF files})
3. **Find manuscript folders** - Open the Work In Progress (WIP) folder containing all submitted manusccript files and find each manuscript folder (named like "MMCTS-2025-101-AuthorName") that correspond to the list of provided pdfs
4. **Create archive folder** - for each manuscript that needs to be archived, create a corresponding arching folder with just the manuscript ID (without the author name) in the FTP folder
5. **Copy the XML and MP4** - from the WIP manuscript folder copy and past the mp4 and xml files it into the new corresponding archiving folder.
6. **Move the PDF** - Find the corresponding PDF and move it into the archive folder
7. Repeat for each manuscript that needs archiving
8. Zip each folder
9. Upload to FileZilla

This was time-consuming, tedious and error-prone. As there were large mp4 files being copied i had to wait up to 5 minutes per manuscript. I would archive in a month between 20-30 manuscripts. So this mannual work could take me over 2 hours per month. 

### The Solution

I wanted to solve this problem using Python. This script automates the entire organisation process, turning hours of manual work into a single command, allowing the archiving to occur in the background whilts I do other useful work. 

## What This Script Does

The script automatically:
1. Identifies manuscript folders from the WIP directory that need archiving
2. Creates new folders named by manuscript ID only (removing author names)
3. Finds and moves the corresponding PDF from the PDF folder
4. Copies the XML and MP4 files from the manuscript's WIP folder
5. Moves all organised folders to the FTP directory, ready for zipping and upload

How it works

## Requirements

- Python 3.x
- Standard libraries: `os`, `shutil`, `zipfile`

No additional installations needed!

