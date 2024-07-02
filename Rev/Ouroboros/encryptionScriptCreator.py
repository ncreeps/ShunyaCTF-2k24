from ciphers import cipherCodes
from random import shuffle

encriptionCodeSnippets = []

encriptionCodeSnippets.append(
	"flag = 'snakeseatsnakes'")

encriptionCodeSnippets.append(
	"import numpy as np")

decryptionCodeSnippets = [
	"import numpy as np",
]
encryptionOrder = []
for i in range(1999):
	for cipherName, codes in cipherCodes.items():
		encriptionCodeSnippets.append(codes[0])
		encryptionOrder.append(cipherName)
encriptionCodeSnippets.append(
	"print(flag)")

with open("encryptionScript.py", "w") as f:
	for codeSnippet in encriptionCodeSnippets:
		f.write(codeSnippet)
		f.write("\n")

import subprocess as s
encryptedFlag = s.check_output("python encryptionScript.py", shell = True).decode().replace("\n", "").replace(r"\n", "").replace("\r", "")
print([c for c in encryptedFlag])

decryptionCodeSnippets.append(f"flag = '{encryptedFlag}' ")
for c in encryptionOrder[::-1]:
	decryptionCodeSnippets.append(cipherCodes[c][1])

decryptionCodeSnippets.append("print(flag)")

with open("decryptionScript.py", "w") as f:
	for codeSnippet in decryptionCodeSnippets:
		f.write(codeSnippet)
		f.write("\n")


decryptedFlag = s.check_output("python decryptionScript.py", shell = True)
print(decryptedFlag)
