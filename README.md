# PwdStore

PwdStoreis a Python 3 file-encryption module and script that uses AES256-CBC to encrypt/decrypt files.

PwdStore is compatible with the AES Crypt file format (version 2).

It is Free Software, released under MIT License

PwdStore is brought to you by Garvit Joshi - garvitjohi9@gmail.com

IMPORTANT SECURITY NOTE: version 2 of the AES Crypt file format does not authenticate the "file size modulo 16" byte. This implies that an attacker with write access to the encrypted file may alter the corresponding plaintext file size by up to 15 bytes.

NOTE: there is no low-level memory management in Python, hence it is not possible to wipe memory areas were sensitive information was stored.