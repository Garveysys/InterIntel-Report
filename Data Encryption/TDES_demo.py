from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Raises Value error if the key is not 16 or 24 bytes
#Raises ValueError if the key becomes single DES
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        print(key)
        break
    except ValueError:
        pass

cipher = DES3.new(key, DES3.MODE_CFB) 
# plain text has to be a multiple of 8   
plaintext= b'We are no longer the knights who say no!' 
# check to see if string is multiple of eight
print(len(plaintext))
# run the encryption cipher
msg = cipher.iv + cipher.encrypt(plaintext)
print(msg)

# run the decryption cipher
cipher_decrypt = DES3.new(key, DES3.MODE_CFB) 
original_text = cipher.iv + cipher_decrypt.decrypt(msg)
print(original_text)

# re_encrypt again
re_encrypted_text = cipher.iv + cipher.encrypt(original_text)
print(re_encrypted_text)

