import math

def shanon_entropy(text: str):

    text = text.lower()
    text = ''.join(c for c in text if c.isalpha())
    if len(text) == 0: return 0

    entropy = 0
    for _, freq in Counter(text).items():
        p = freq / len(text)
        entropy += p * math.log2(p)
    return -entropy

def guess_key_length(ciphertext: str, min_key_length: int, max_key_length: int, amount: int):
    ciphertext = ciphertext.lower()
    ciphertext = "".join(c for c in ciphertext if c.isalpha())

    scored = []

    for k in range(min_key_length, max_key_length):
        groups = [""] * k

        for i in range(len(ciphertext)):
            groups[i%k] = groups[i%k] + ciphertext[i]

        av_entropy = 0 # Calculamos la media en vez de la suma para no favorecer claves cortas (tendrian mas subtextos con entropias que sumar)
        for g in groups:
            av_entropy += shanon_entropy(g)
        av_entropy /= k

        scored.append((k, av_entropy))

    scored = sorted(scored, key=lambda x: x[1])
    scored = [d[0] for d in scored]
    return scored[:amount]


def crack_vigenere(ciphertext: str, min_key_length: int, max_key_length: int, amount: int):
    likely_key_lengths = guess_key_length(ciphertext, min_key_length, max_key_length, amount)
    print(f"Likely key legths: {likely_key_lengths}")

    scored = []
    for k in likely_key_lengths:
        likely_key = crack_knowing_key_length(ciphertext, k) 
        entropy = shanon_entropy(vigenere_decrypt(ciphertext, likely_key))
        scored.append((likely_key, entropy))

    scored = sorted(scored, key=lambda x: x[1])
    for s in scored:
        print(s)