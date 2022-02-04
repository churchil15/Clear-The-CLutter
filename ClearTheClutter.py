import os

def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Custom method to replace all the files with the folders created and add them
def move(foldername, files):  
    for file in files:
        os.replace(file, f"{foldername}/{file}")

if __name__ == '__main__':
    # Everything is present inside the files list including this ClearTheCLutter.py script
    # So we need to make sure that this script is not included because we do not want to move this file.
    files = os.listdir()      
    files.remove("main.py")   
    CreateIfNotExist("Images")
    CreateIfNotExist("Docs")
    CreateIfNotExist("Medias")
    CreateIfNotExist("Others")

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".docx", ".doc", ".xlsx", ".ppt", ".pptx", ".pdf", ".rtf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp4", ".mp3", ".mkv", ".webm"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            others.append(file)

    # Now we are ready to move our files list inside the provided folders
    move("Images", images)
    move("Docs", docs)
    move("Medias", medias)
    move("Others", others)
