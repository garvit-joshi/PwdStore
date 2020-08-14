import pyAesCrypt
import os

def fileNameChange(fileName,Operation):
    if(Operation==1):
        return fileName[:-4]




def fileEncrypt(password,n,fileNameAES="Data.txt.aes"):
    bufferSize = 64 * 1024
    fileName=fileNameChange(fileNameAES,1)
    try:
        dFile = open(fileName,'w')
        for i in range(0,n):
            print("\n\nEntry",i+1," of ",n,":\n")
            site=input("Enter the Name of site:")
            username=input("Enter your Username/Email:")
            passw=input("Enter your Password:")
            dFile.write(site)
            dFile.write("\n")
            dFile.write(username)
            dFile.write("\n")
            dFile.write(passw)
            dFile.write("\n")
        dFile.close()
    except:
        dFile.close()
        print("Error: Data Cannot be Written into File.")
        if(os.path.isfile(fileName)==True):
            os.remove(fileName)
        return -1
    try:
        pyAesCrypt.encryptFile(fileName,fileNameAES, password, bufferSize)
    except:
        print("Error: Data cannot be protected using Encryption.")
        os.remove(fileName)
        return -1
    os.remove(fileName)




def fileDecrypt(password,fileNameAES="Data.txt.aes"):
    count=0
    en=1
    fileName=fileNameChange(fileNameAES,1)   
    bufferSize = 64 * 1024
    if(os.path.isfile(fileNameAES)==False):
        print("Error:",fileNameAES,"Not Present.")
        return -1
    try:
        pyAesCrypt.decryptFile(fileNameAES, fileName, password, bufferSize)
    except:
        print("Error: Password may be wrong.")
        return -1
    try:
        dFile = open(fileName,'r')
    except:
        print("Error: Unable to open file:",fileName)
    Lines = dFile.readlines()
    n=len(Lines)
    n=int(n/3)
    for line in Lines:
        line=line[:-1]
        if(count%3==0):
            print("Entry",en,"of",n,":")
            print("Site:",line)
            en=en+1
        elif(count%3==1):
            print("Username/Email:",line)
        else:
            print("Password:",line)
            print("\n\n")
        count=count+1
    dFile.close()
    try:
        os.remove(fileName)
    except:
        return -1