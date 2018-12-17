#! python3
# pdf_finder.py - searches for all pdf files in a particular folder (incl.
#                 subfolders) on disk D: and copies them into the new folder.

import os, re, shutil

# Creating a regular expression for *.pdf files.
re_pdf = re.compile(r'\.pdf$')

# Asking for a source folder on disc D:\
folder = input('Source folder on disk D:\\')

# Searching for the source folder
found = False
for folder_name, subfolders, file_names in os.walk('D:\\'):
    if os.path.basename(folder_name) == folder:
        found = True
        abs_source_path = folder_name
        break

if found:
    # Asking for a folder to copy files.
    new_folder = input('Destination folder on disk D:\\')
    abs_destination_path = 'D:\\' + new_folder
    os.makedirs(abs_destination_path, exist_ok=True)
    
    # Searching for pdf files and copying them.
    for folder_name, subfolders, file_names in os.walk(abs_source_path):
        for file_name in file_names:
            mo = re_pdf.search(file_name)
            if mo == None:
                continue
            shutil.copy(folder_name+'\\'+file_name, abs_destination_path)
            print('File %s has been copied.' % (folder_name+'\\'+file_name))
else:
    print('There is no such folder on disk D:\\')            
