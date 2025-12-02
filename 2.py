def crack(ciphertext: str):
    for i in (range(ord('a'), ord('z') + 1)):
        print(f"{i-96}) {decrypt(ciphertext, chr(i))[:20]}")
    
    key = int(input("Enter the legible text [1-25] or 0 for None: "))
    if key == 0:
        print("Couldn't find the key")
        return None
    return chr(key+96)

# Para la siguiente
english = "etaoinshrdlcumwfgypbvkjxqz"

text1 = (
    "The very first well-documented description of a polyalphabetic cipher was by Leon Battista Alberti "
    "around 1467 and used a metal cipher disk to switch between cipher alphabets. Alberti's system only "
    "switched alphabets after several words, and switches were indicated by writing the letter of the "
    "corresponding alphabet in the ciphertext. Later, Johannes Trithemius, in his work Polygraphia "
    "(which was completed in manuscript form in 1508 but first published in 1518), invented the tabula "
    "recta, a critical component of the Vigenère cipher. The Trithemius cipher, however, provided a "
    "progressive, rather rigid and predictable system for switching between cipher alphabets. In 1586 "
    "Blaise de Vigenère published a type of polyalphabetic cipher called an autokey cipher – because its "
    "key is based on the original plaintext – before the court of Henry III of France. The cipher now "
    "known as the Vigenère cipher, however, is based on that originally described by Giovan Battista "
    "Bellaso in his 1553 book La cifra del Sig. Giovan Battista Bellaso. He built upon the tabula recta "
    "of Trithemius but added a repeating countersign to switch cipher alphabets every letter. Whereas "
    "Alberti and Trithemius used a fixed pattern of substitutions, Bellaso's scheme meant the pattern of "
    "substitutions could be easily changed, simply by selecting a new key. Keys were typically single "
    "words or short phrases, known to both parties in advance, or transmitted 'out of band' along with "
    "the message. Bellaso's method thus required strong security for only the key. As it is relatively "
    "easy to secure a short key phrase, such as by a previous private conversation, Bellaso's system was "
    "considerably more secure. Note, however, as opposed to the modern Vigenère cipher, Bellaso's cipher "
    "didn't have 26 different 'shifts' (different Caesar ciphers) for every letter, instead having 13 "
    "shifts for pairs of letters. In the 19th century, the invention of this cipher, essentially designed "
    "by Bellaso, was misattributed to Vigenère. David Kahn, in his book The Codebreakers, lamented this "
    "misattribution, saying that history had 'ignored this important contribution and instead named a "
    "regressive and elementary cipher for him [Vigenère] though he had nothing to do with it'. The "
    "Vigenère cipher gained a reputation for being exceptionally strong. Noted author and mathematician "
    "Charles Lutwidge Dodgson (Lewis Carroll) called the Vigenère cipher unbreakable in his 1868 piece "
    "'The Alphabet Cipher' in a children's magazine. In 1917, Scientific American described the Vigenère "
    "cipher as 'impossible of translation'. That reputation was not deserved. Charles Babbage is known to "
    "have broken a variant of the cipher as early as 1854 but did not publish his work. One hypothesis is "
    "that he intentionally kept the general method secret, since he was a cryptographical adviser to his "
    "friend, Rear-Admiral Sir Francis Beaufort, during the Crimean War. Kasiski entirely broke the cipher "
    "and published the technique in the 19th century, but even in the 16th century, some skilled "
    "cryptanalysts could occasionally break the cipher."
)
