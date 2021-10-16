def rotate(strg, n):
    return strg[n%len(strg):] + strg[:n%len(strg)]

def substitute(text,fr,to):
    return "".join([to[fr.find(a)] if a in fr else a for a in text.upper()])

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

k = int(input("input shift: "))
text = input("input text: ")

print("ciphertext:",substitute(text,alphabet,rotate(alphabet,k)))
print("deciphered:",substitute(text,rotate(alphabet,k),alphabet))