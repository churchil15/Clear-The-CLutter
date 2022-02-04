# Clear-The-CLutter
A simple Python script to filter the files in a folder and add them in their respective directories according to their extension.

I created this script using simple file handling options in Python. Using the OS module of python we can
access the path of the files and folders and can manipulate them using the replace function of OS module. We can create folders using the makedirs() method and can make our custom function that will take all the files and will place them in their respective folders. The sorting of files will be done on the basis of their extensions like files with the extension of ".png", ".jpg", ".jpeg" can be added into the Images folder. os.path.splitext() method is used to to split the name of the file with its extension. Also we have to make sure to not create a folder until and unless it is already created.

Note: **We can add more extensions to our list according to our needs**

# Usage
Just add this script into your folder where you want to clear the cluttered files and sort them. Run this file by double clicking on it and you will see that each and every file present in the folder is being removed and has added in their respective folders according to their extensions. Four folders will be created, i.e Images, Docs, Medias and Others.
