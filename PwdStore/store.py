import pyAesCrypt
import os
def fileEncrypt(password,n):
    bufferSize = 64 * 1024
    try:
        dFile = open("Data.txt",'w')
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
        if(os.path.isfile("Data.txt")==True):
            os.remove("Data.txt")
        return -1
    try:
        pyAesCrypt.encryptFile("Data.txt","Data.txt.aes", password, bufferSize)
    except:
        print("Error: Data cannot be protected using Encryption.")
        os.remove("Data.txt")
        return -1
    os.remove("Data.txt")
def fileDecrypt(password):
    count=0
    en=1
    bufferSize = 64 * 1024
    if(os.path.isfile("Data.txt.aes")==False):
        print("Error: Data.txt.aes Not Present.")
        return -1
    try:
        pyAesCrypt.decryptFile("Data.txt.aes", "Data.txt", password, bufferSize)
    except:
        print("Error: Password may be wrong.")
        return -1
    dFile = open("Data.txt",'r')
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
        os.remove("Data.txt")
    except:
        return -1