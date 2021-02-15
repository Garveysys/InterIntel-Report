from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad 

# generate key
key = b'mysecretpassword'

#open up a cipher_file file to retrieve the iv and cipher text
with open('cipher_file', 'rb') as c_file:
    #read the first 16bytes
    iv = c_file.read(16)
    #pull subsqeuent bytes
    ciphertext = c_file.read()

#create a cipher to decrypt
#takes key mode and iv
cipher = AES.new(key, AES.MODE_CBC, iv )

#plaintext is unpadded and decrypted
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

# print the original message in byte format
print(plaintext)
print(plaintext.decode())