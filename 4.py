def vigenere_encrypt(plaintext: str, key: str):
    if not key.isalpha():
        print("Key must contain only alphabetic characters")
        return

    ciphertext = ""
    key = key.lower()
    key_index = 0
    key_len = len(key)

    for ch in plaintext:
        if ch.isalpha():
            shift = ord(key[key_index % key_len]) - ord('a')
            base = ord('A') if ch.isupper() else ord('a')
            ciphertext += chr((ord(ch) - base + shift) % 26 + base)
            key_index += 1
        else:
            ciphertext += ch

    return ciphertext


def vigenere_decrypt(ciphertext: str, key: str):
    if not key.isalpha():
        print("Key must contain only alphabetic characters")
        return

    plaintext = ""
    key = key.lower()
    key_index = 0
    key_len = len(key)

    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(key[key_index % key_len]) - ord('a')
            base = ord('A') if ch.isupper() else ord('a')
            plaintext += chr((ord(ch) - base - shift) % 26 + base)
            key_index += 1
        else:
            plaintext += ch

    return plaintext