import os

def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):   #Ex: Images, images
    for file in files:
        os.replace(file, f"{foldername}/{file}")
    # yha pr hmne file me "double inverted commma" isiliye nhi lgaya hai kyuki ye ek list hai jisme saare elements hai
    # shayad hm loop ke saath kaam krrhe hai isliye f-string use kiya hai

if __name__ == '__main__':
    files = os.listdir()      #files list me hmare saare files and folders moujood hai including this main.py script
    files.remove("main.py")   #main.py script ko remove krdenge
    # print(files)
    CreateIfNotExist("Images")
    CreateIfNotExist("Docs")
    CreateIfNotExist("Medias")
    CreateIfNotExist("Others")

    # "file" bas ek iterable hai jo ki iterate krrha hai files list ko jisme saari cheejen maujood hai

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    # print(images)

    docExts = [".txt", ".docx", ".doc", ".xlsx", ".ppt", ".pptx", ".pdf", ".rtf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    # print(docs)

    mediaExts = [".mp4", ".mp3", ".mkv", ".webm"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    # print(medias)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            others.append(file)

    # print(others)
    # print(others) #apne ko files move krni hai folders nhi move krne hai

    # os.path.isfile(file) ka mtlb ye hai ki usko file hona bhi zaroori hoga tbhi vo
    # others folder me jayega

    """
    a = os.path.isfile("C:/Users/admin/Desktop")
    print(a)
    This will return False because the path entered is not an file

    b = os.path.isfile("C:/Users/admin/Desktop/Jashane Bahara - SLOW + REVERB Bollywood Music.webm")
    print(b)
    This will return True because the path entered is an file
 
    """
    # abb hum log tyaar hai files move krne ke liye --

    move("Images", images)
    move("Docs", docs)
    move("Medias", medias)
    move("Others", others)

