def vigenere_decrypt(ciphertext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower().replace(' ', '')
    key_repeated = ''.join(key[i % len(key)] for i in range(len(ciphertext)))
    plaintext = ''
    
    for i in range(len(ciphertext)):
        if ciphertext[i].lower() in alphabet:
            shift = alphabet.index(key_repeated[i])
            decrypted_index = (alphabet.index(ciphertext[i].lower()) - shift) % 26
            if ciphertext[i].isupper():
                plaintext += alphabet[decrypted_index].upper()
            else:
                plaintext += alphabet[decrypted_index]
        else:
            plaintext += ciphertext[i]  # non-alphabetic characters are not decrypted
    
    return plaintext

ciphertext = "IyphchLhmlp"
key = "InthePenalColony"
flag = vigenere_decrypt(ciphertext, key)
print("Decrypted Message (Flag):", flag)