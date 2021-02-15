from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

text = b'This message is from me'
#import the private key
key = RSA.import_key(open('private.key').read())
#hash the text 
hash = SHA256.new(text)

#sign the hashed text
#create an object we can use to sign the hashed text.
signer = pkcs1_15.new(key)
#my hash signed by private key
signature = signer.sign(hash) 

#write signature and text to a file
file_out = open('signature.pem', 'wb')
file_out.write(signature)
file_out.close()

file_out = open('text.txt', 'wb')
file_out.write(text)
file_out.close()

print (signature.hex())
print(signature)
