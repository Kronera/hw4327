
#Part 1: Caesar Cipher
def ceasars_encrypt(text, key):
    ciphertext = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('A') + key) % 26
            ciphertext += chr(shifted + ord('A'))
        else:
            ciphertext += char
    return ciphertext

#plaintext = "Natan Najera cpts"
# my student ID is 11731471, so my key is 1
#key = 1
#ciphertext = ceasars_encrypt(plaintext, key)
#print("Encrypted text:", ciphertext)

def ceasars_decrypt(text, key):
    plaintext = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('A') - key) % 26
            plaintext += chr(shifted + ord('A'))
        else:
            plaintext += char
    return plaintext

#decrypted_text = ceasars_decrypt(ciphertext, key)
#print("Decrypted text:", decrypted_text)

#Part 2: Vigenere Cipher


word_list = set()
file = open('words_alpha.txt', 'r')
for line in file:
    word_list.add(line.strip())

def vigenere_encrypt(text, key):
    ciphertext = ""
    text = text.lower()
    key = key.lower()
    key_length = len(key)
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            shifted = (ord(char) - ord('a') + shift) % 26
            ciphertext += chr(shifted + ord('a'))
            i += 1
        else:
            ciphertext += char
    return ciphertext

#plaintext = "attack at dawn"
#key = "lemon"
#ciphertext = vigenere_encrypt(plaintext, key)
#print("Encrypted text:", ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    ciphertext = ciphertext.lower()
    key = key.lower()
    i = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            shifted = (ord(char) - ord('a') - shift) % 26
            plaintext += chr(shifted + ord('a'))
            i += 1
        else:
            plaintext += char
    return plaintext

def bruteForceVigenere(ciphertext):
    for key in word_list:
        if len(key) < 10:
            decrypted_text = vigenere_decrypt(ciphertext, key)
            if checkWord(decrypted_text):
                return decrypted_text, key
    return "Key not found", "Key not found"
def checkWord(word):
    words_in_text = word.split()

    # If there's no text, return False immediately
    if not words_in_text:
        return False

    # Remove punctuation and check each word
    for word in words_in_text:
        clean_word = word.strip().lower()
        if clean_word not in word_list:
            print(f"Word not found in dictionary: {clean_word}")  # Debugging line
            return False  # If even one word is missing, it's not valid
    return True
#decrypted_text = vigenere_decrypt(ciphertext, key)
#print("Decrypted text:", decrypted_text)
#key = "washington"
# getting a char from a file and decrypting it
file = open('cipher6.txt', 'r')
content = file.read().strip()
#decrypted_text = vigenere_decrypt(content,key)

#decryptedC, bruteKey = bruteForceVigenere(content)
#print("Decrypted text:", decryptedC)
#print("Key:", bruteKey)
print(word_list)