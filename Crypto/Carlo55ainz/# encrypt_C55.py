# encrypt.py
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
import binascii

def encrypt_message(message, passphrase, salt, iv):
    # Derive key from passphrase and salt using scrypt KDF
    key = scrypt(passphrase.encode(), salt=salt.encode(), key_len=16, N=2**14, r=8, p=1)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad the message to be a multiple of AES block size (16 bytes)
    length = AES.block_size - (len(message) % AES.block_size)
    message += chr(length).encode() * length  # PKCS#7 padding
    ciphertext = cipher.encrypt(message)
    return ciphertext

if __name__ == "__main__":
    passphrase = "rotarepO htoomS"
    salt = "Scuderia Ferrari"  # Salt inspired by Scuderia Ferrari in F1
    iv = binascii.unhexlify('00112233445566778899aabbccddeeff')  # Fixed IV in hexadecimal format (16 bytes)
    message = "pit stop snacks ready"
    encrypted_message = encrypt_message(message.encode(), passphrase, salt, iv)
    
    print("Encrypted message:", encrypted_message.hex())
