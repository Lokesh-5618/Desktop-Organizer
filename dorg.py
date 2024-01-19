#importing 2 crucial models required
import os #os module used for to interact with os
import shutil #shutil module is used for performing file operations simply
#extracting desktop path
desktop_path=os.path.expanduser("~/Desktop")
#extracting all directories from desktop to further group them
directories=os.listdir(desktop_path)
#setting up a dictionary to store paths of every file in desktop
allfile_path={}
for filename in directories:
    filepath=os.path.join(desktop_path,filename)#joining filename with desktop path to make it as a path for every files in the desktop(so the loop)
    if os.path.isfile(filepath): #to check if the given file path is of a file or folder only continue if its file as folder needs no organising
        fileext=os.path.splitext(filename)[1]      #getting the .png,.jpg.word parts from the various file names to know their extension   
        if fileext not in allfile_path:
            allfile_path[fileext]=[]       #now we create a list value for every key i.e the extension(pdf,jpg...etc) its gonna be like pdf:[]...so on
        allfile_path[fileext].append(filepath)  #now we add the file path to the list (in dictionary) which has extension types as a key in this way various paths with various extensions are segregated into different keys' list
#lets move the files to respective folders thanks to the segregated dictionary data
for extname,fpath in allfile_path.items():   #looping through every file of every extensions in the dictionary
    foldername=f"{extname[1:].upper()} files" #format string method to make folder name "(extension name in capital) Files" the [.1]is to just extract the ext name leaving the . aside
    folderpath=os.path.join(desktop_path,foldername) #path for the folder is the desktop followed by the folder name which done by the o0s.path.join
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    for fpat in fpath:
        shutil.move(fpat,folderpath)
