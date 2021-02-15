import hashlib

#create a hash instance & call the hex digest method
sha = hashlib.sha1(b'This is secure hash algorithm').hexdigest()
sha256 = hashlib.sha256(b'This is secure hash algorithm').hexdigest()
sha512 = hashlib.sha512(b'This is secure hash algorithm').hexdigest()
print(sha)
print(sha256)
print(sha512)