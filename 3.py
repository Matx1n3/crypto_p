from collections import Counter

def most_frequent_letter(text: str):
    letters = [ch.lower() for ch in text if ch.isalpha()]
    if not letters: return None
    cont = Counter(letters)
    most_frequent, _ = cont.most_common(1)[0]
    return most_frequent

def statistical_analisys(ciphertext: str):
    most_freq_let = most_frequent_letter(ciphertext)
    print(f"The most frequent letter is {most_freq_let}")
    if most_freq_let is None: return None
    for i in english:
        possible_key = chr(ord('a') + ((ord(most_freq_let) - ord(i)) % 26))
        possible_cleartext = decrypt(ciphertext, possible_key)
        print(f"\n{possible_cleartext[:20]}")
        option = input("Is the text above legible? (y/any)")
        if option == 'y':
            return possible_key
    return None
       