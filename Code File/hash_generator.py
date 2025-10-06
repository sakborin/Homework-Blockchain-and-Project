import hashlib

text = "Hello Blockchain"
hash_object = hashlib.sha256(text.encode())
print("Hash:", hash_object.hexdigest())
