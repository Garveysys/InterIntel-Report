import hashlib

# create an instance of an md5 object
md5hash = hashlib.md5()

#convert to byte string since md5 only uses byte string
md5hash.update(b'This is the string to be hashed')

#to obtain the hash we call the digest method
print(md5hash.digest())

#to get the hex digest call the hex digest method
print(md5hash.hexdigest())



