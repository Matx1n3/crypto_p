def encrypt(plaintext: str, key: str):
    if len(key) != 1:
        print("Length of key must be 1")
        return
    
    shift = ord(key.lower()) - ord('a')
    
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ciphertext += chr((ord(ch) - base + shift) % 26 + base)

        else:
            ciphertext += ch

    return ciphertext

def decrypt(ciphertext: str, key: str):
    if len(key) != 1:
        print("Length of key must be 1")
        return
    
    shift = ord(key.lower()) - ord('a')
    
    plaintext = ""
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            plaintext += chr((ord(ch) - base - shift) % 26 + base)
        else:
            plaintext += ch

    return plaintext 