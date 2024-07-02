DIVINE_MESSAGE = "i am groot"

def encrypt(msg:str) -> str:
	phrase = [c for c in DIVINE_MESSAGE]

	# abc -> ["61", "62", "63"] -> [(6, 1), (6, 2), (6, 3)]
	chrs = [(int(d) for d in str(ord(c))) for c in msg]

	cipher = ""

	for letter_ascii in chrs:
		for digit in letter_ascii:
			p = phrase[::]
			p[digit] = p[digit].upper()
			if p[digit] == " ":
				p[digit] = chr(0)
			cipher += "".join(p)
			cipher += "\n"
		cipher += "\n"

	return cipher


def phraseToDigit(phrase:str):
	if len(phrase) != len(DIVINE_MESSAGE):
		raise ValueError(f"Does not follow the divine teachings of groot. (Does not match the 'i am groot' message length.) |{phrase}|")

	for i, c in enumerate(phrase):
		if c != DIVINE_MESSAGE[i]:
			return i

	return -1
def decrypt(msg:str):
	msg = msg.split("\n\n")
	msg = [asc.split("\n") for asc in msg if asc != ""]

	# abc -> ["61", "62", "63"] -> [(6, 1), (6, 2), (6, 3)]
	decrypted = []
	for asc in msg:
		digits = []
		for d in asc:
			digits.append(phraseToDigit(d))
		number = 0
		for i, d in enumerate(digits[::-1]):
			number += d*(10**i)
		decrypted.append(chr(number))

	return "".join(decrypted)

print(decrypt(encrypt("asnkhwrhsvdqirvoiwqhd982174981u 1 yn21uvoijrok oi i eroio")))


flag = "0CTF{Groot_I_Am}"
with open("enc.txt", "w") as f:
	f.write(encrypt(flag))

with open("enc.txt", "r") as f:
	decrypted = decrypt(f.read())
	print(decrypted)
	assert flag == decrypted