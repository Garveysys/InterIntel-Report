from Crypto.Cipher import AES
from Crypto.Util.Padding import pad 

# generate key manually
key = b'mysecretpassword'

# create the cipher and select mode
cipher = AES.new(key, AES.MODE_CBC) 

plaintext = b"This is a classified message for top officials"

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# print(ciphertext)

#write ciphertext and iv to a file
with open('cipher_file', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphertext)