def statistical_analisys(ciphertext: str):
    most_freq_let = most_frequent_letter(ciphertext)
    #print(f"The most frequent letter is {most_freq_let}")
    if most_freq_let is None: return None
    shift = (ord(most_freq_let) - ord('e')) % 26
    key_letter = chr(ord('a') + shift)
    return key_letter

def crack_knowing_key_length(ciphertext: str, k: str):
    ciphertext = ciphertext.lower()
    ciphertext = "".join(c for c in ciphertext if c.isalpha())
    groups = [""] * k

    for i in range(len(ciphertext)):
        groups[i%k] = groups[i%k] + ciphertext[i]

    possible_key = ""
    for g in groups:
        possible_key += statistical_analisys(g)
    return possible_key