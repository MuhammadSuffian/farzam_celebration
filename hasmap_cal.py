import hashlib
HASHED_PASSWORD = hashlib.sha256("SalehaMariDost".encode("utf-8")).hexdigest()
print(HASHED_PASSWORD)