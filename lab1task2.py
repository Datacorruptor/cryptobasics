def first_word_alphabet(alphabet,word):
    if len(set(word)) == len(word):
        return word.upper()+"".join([letter for letter in alphabet if letter not in word.upper()])
    else:
        print("no duplicate letters")
        exit(1)


def substitute(text,fr,to):
    return "".join([to[fr.find(a)] if a in fr else a for a in text.upper()])


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

word = input("input key word: ")
text = input("input text: ")

print(first_word_alphabet(alphabet,word))

print("ciphertext:",substitute(text,alphabet,first_word_alphabet(alphabet,word)))
print("deciphered:",substitute(text,first_word_alphabet(alphabet,word),alphabet))