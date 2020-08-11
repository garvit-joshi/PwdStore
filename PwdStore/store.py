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
        print("Error:1")
        dFile.close()
        return -1
    try:
        pyAesCrypt.encryptFile("Data.txt","Data.txt.aes", password, bufferSize)
    except:
        print("Error:2")
        return -1
    os.remove("Data.txt")
def fileDecrypt(password):
    count=0
    bufferSize = 64 * 1024
    try:
        pyAesCrypt.decryptFile("Data.txt.aes", "Data.txt", password, bufferSize)
    except:
        print("Error:3\nPassword may be wrong")
        return -1
    dFile = open("Data.txt",'r')
    Lines = dFile.readlines()
    for line in Lines:
        if(count%3==0):
            print("Entry ",(count%3)+1,":\n")
            print("Site:",line)
        elif(count%3==1):
            print("Username/Email:",line)
        else:
            print("Password:",line,)
        count=count+1
    dFile.close()
    try:
        os.remove("Data.txt")
    except:
        return 0
    