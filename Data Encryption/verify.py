from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
#import and read public key
key = RSA.import_key(open('public.key').read())
# read received message and signature 
file_in = open('text.txt', 'rb')
text = file_in.read()
file_in.close()

file_in = open('signature.pem', 'rb')
signature = file_in.read()
file_in.close() 

#compare both hashes
text = SHA256.new(text)

try:
    pkcs1_15.new(key).verify(text, signature)
    print("The signature is valid, Message has not been changed.")
except (ValueError, TypeError):
    print("This is not the original message")

