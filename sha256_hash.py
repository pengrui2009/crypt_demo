import hashlib

def sha256_hex(data_hex):
    data_bytes = bytes.fromhex(data_hex)
    sha256_hash = hashlib.sha256(data_bytes)
    return sha256_hash.hexdigest()

data_hex = "0123456789abcdef"
print(sha256_hex(data_hex))
