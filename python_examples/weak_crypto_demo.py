# Intentionally insecure example for CodeQL demo purposes only.
# Demonstrates weak cryptographic algorithm usage.

import hashlib

def hash_password(password: str) -> str:
    # Vulnerable: MD5 is not appropriate for password hashing
    return hashlib.md5(password.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    print(hash_password("P@ssw0rd!"))
