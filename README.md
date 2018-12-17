# scripts
Collection of various short scripts that makes our daily life much easier. 
Every single day we click, type, download, organize files and folders, search for them, fill forms. There are a lot of repetitive tasks that have no ready-made software to perform them. Every day they greedily consume our time. But what if using a little bit of programming knowledge we would let our computer do the job? This is the main question and idea of the great book "Automate the Boring Stuff with Python" written by Albert Sweigart.
- apod_download.py downloads the last 10 jpg pictures from www.apod.nasa.gov You can easily download many thousands images by changing the upper limit of i parameter in the while loop.
- pdf_finder.py searches for all pdf files in a particular folder (including all subfolders) on disk D and copies them into the a new  folder. Change 'pdf' in the regular expression and find any file type you'd like.
- mapit.pyw launches GoogleMap in the browser using an address from the command line or content of clipboard. No terminal window. To use the command line interface create mapit.bat file: @pyw.exe path_to_mapit.pyw %*
- mcb.pyw saves and loads text fragments to the clipboard. No terminal window. Create mapit.bat file: @pyw.exe path_to_mapit.pyw %* Control: mcb save <keyword> - saves clipboard to a keyword value; mcb <keyword> - loads the keyword value to clipboard; mcb list - loads a list of keywords to clipboard; mcb delete - deletes all data; mcb delete <keyword> - deletes the keyword.
