import os, shutil

DRY_RUN = True
"""
step 1: identify the specific folders i want 
step 2: get the files from the folder
step 3: copy these files into their own individual folders 
step 4: move this folders to a new location 
step 5: move pdfs into their respective folders 
"""

WIP_path = r"/path/to/your/WIP/folder"
pdf_folder_path = r"/path/to/your/PDF/folder"

manuscript_ids = [
    "JOURNAL-2025-101-AuthorA",
    "JOURNAL-2025-102-AuthorB",
    "JOURNAL-2025-103-AuthorC",
]

for folder in os.listdir(WIP_path):

   
    if folder in manuscript_ids: 
        new_folder_name = folder.rsplit("-", 1)[0]
        new_folder_path = os.path.join(WIP_path, new_folder_name)
        folder_path = os.path.join(WIP_path, folder)
        
       
        if DRY_RUN:
            print(f"{folder} is the folder that was found")
            print(f"{new_folder_name} has been created")
        else:
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

        for pdf_file in os.listdir(pdf_folder_path):
            pdf_file_path = os.path.join(pdf_folder_path, pdf_file)
            if pdf_file.endswith(".pdf"):
                    if new_folder_name in pdf_file:
                        shutil.move(pdf_file_path, new_folder_path)          
        
        for file in os.listdir(folder_path):
            print(f"The files in {folder} is {file}")
            if file.endswith(".xml") or file.endswith(".mp4"):
                xml_mp4_source_file = os.path.join(folder_path, file)

                if DRY_RUN:
                    print(f"the xml/mp4 file in {folder} will move to {new_folder_name}")

                else: 
                    shutil.copy2(xml_mp4_source_file, new_folder_path)
                                
        shutil.move(new_folder_path, pdf_folder_path)
    

        
      
