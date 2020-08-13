# PwdStore

PwdStoreis a Python 3 file-encryption module and script that uses AES256-CBC to encrypt/decrypt your Username and Passwords.

PwdStore is compatible with the AES Crypt file format (version 2).

It is Free Software, released under MIT License

PwdStore is brought to you by Garvit Joshi - garvitjohi9@gmail.com

IMPORTANT SECURITY NOTE: version 2 of the AES Crypt file format does not authenticate the "file size modulo 16" byte. This implies that an attacker with write access to the encrypted file may alter the corresponding plaintext file size by up to 15 bytes.

NOTE: there is no low-level memory management in Python, hence it is not possible to wipe memory areas were sensitive information was stored.

## Module usage example:

### Encrypt Data:

#### If you want to store data in Data.txt.aes
```
import PwdStore
n=int(input("Enter the No. of Credentials you want to Save:"))
mPassword=input("Enter A Password You want to create for the file:")
PwdStore.fileEncrypt(mPassword,n)
```

#### If you want to store data in your own file:
Add a third Argument in  ```PwdStore.fileEncrypt()``` with the name of file you want to stre data in:
```
import PwdStore
n=int(input("Enter the No. of Credentials you want to Save:"))
mPassword=input("Enter A Password You want to create for the file:")
PwdStore.fileEncrypt(mPassword,n,"Hello.txt.aes")
```
**Please Enter Suffix ```.txt.aes``` at the end of file**

### Decrypt Data:

#### if you want to retrieve data from Data.txt.aes
```
import PwdStore
mPassword=input("Please Enter Your master Password:")
PwdStore.fileDecrypt(mPassword)
```

#### If you want to retrieve data from your own file
```
import PwdStore
mPassword=input("Please Enter Your master Password:")
PwdStore.fileDecrypt(mPassword,"Hello.txt.aes")
```

**Please Enter Suffix ```.txt.aes``` at the end of file**

#### Notes:
1. Buffer Size=64 * 1024
2. Data will be written in ```Data.txt.aes``` by default, may change name of file in later builds.