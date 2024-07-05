# decrypt.py
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
import binascii

def decrypt_message(ciphertext, passphrase, salt, iv):
    # Derive key from passphrase and salt using scrypt KDF
    key = scrypt(passphrase.encode(), salt=salt.encode(), key_len=16, N=2**14, r=8, p=1)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext)
    # Remove PKCS#7 padding
    pad_length = decrypted_message[-1]
    decrypted_message = decrypted_message[:-pad_length]
    return decrypted_message.decode('utf-8')

if __name__ == "__main__":
    encrypted_message_hex = " dbbe8d593137891af1811b3a1efa98f80fe0607024527d72a2324cdf9339e8d3"

    passphrase = "rotarepO htoomS"
    salt = "Scuderia Ferrari"  # Same salt as used in encryption
    iv = binascii.unhexlify('00112233445566778899aabbccddeeff')  # Same fixed IV as used in encryption (16 bytes)

    encrypted_message = bytes.fromhex(encrypted_message_hex)
    decrypted_message = decrypt_message(encrypted_message, passphrase, salt, iv)
    
    print("Decrypted message:", decrypted_message)
