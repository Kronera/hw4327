
#Part 1: Caesar Cipher
def ceasars_encrypt(text, key):
    ciphertext = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('a') + key) % 26
            ciphertext += chr(shifted + ord('a'))
        else:
            ciphertext += char
    return ciphertext

plaintext = "natan najera cpts"
# my student ID is 11731471, so my key is 1
key = 1
ciphertext = ceasars_encrypt(plaintext, key)
print("Encrypted text:", ciphertext)

def ceasars_decrypt(text, key):
    plaintext = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('a') - key) % 26
            plaintext += chr(shifted + ord('a'))
        else:
            plaintext += char
    return plaintext

decrypted_text = ceasars_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)

#Part 2: Vigenere Cipher

import nltk
from nltk.corpus import words
nltk.download("words")
word_list = set(words.words())

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
            
            if checkWords(decrypted_text):
                return decrypted_text, key

    
    return "Key not found", "Key not found"

def checkWords(text, threshold=0.6): # if 60% of the words are in the dictionary then it is considered as a valid text
    words_in_text = text.split()
    accum = 0
    if not words_in_text:
        return False
    for word in words_in_text:
        word = word.strip().lower()
        if word in word_list:
            accum += 1
    return accum / len(words_in_text) >= threshold

#decrypted_text = vigenere_decrypt(ciphertext, key)
#print("Decrypted text:", decrypted_text)
#key = "university"
# getting a char from a file and decrypting it
file = open('cipher6.txt', 'r')
content = file.read().strip()
#decrypted_text = vigenere_decrypt(content,key)
file2 = open('cipher7.txt', 'r')
content2 = file2.read().strip()


decryptedC, bruteKey = bruteForceVigenere(content)
decryptedC2, bruteKey2 = bruteForceVigenere(content2)

print("\ncipher 6:\nDecrypted text:", decryptedC)
print("Key: ", bruteKey)

print("\ncipher 7:\nDecrypted text: ", decryptedC2)
print("Key: ", bruteKey2)