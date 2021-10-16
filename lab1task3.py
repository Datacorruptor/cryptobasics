def rotate(strg, n):
    return strg[n%len(strg):] + strg[:n%len(strg)]

def substitute_cipher(text,chain):
    res = ""
    i=1
    for a in text.upper():
        res += chain[i][chain[0].find(a)] if a in chain[0] else a
        i = (i)%(len(chain)-1)+1
    return res

def substitute_decipher(text,chain):
    res = ""
    i=1
    for a in text.upper():
        res += chain[0][chain[i].find(a)] if a in chain[i] else a
        i = (i)%(len(chain)-1)+1
    return res

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

k1 = int(input("input shift 1: "))
k2 = int(input("input shift 2: "))
text =   input("input text: ")

chain =[
    alphabet,
    rotate(alphabet,k1),
    rotate(alphabet,k2)
]

print("ciphertext:",substitute_cipher(text,chain))
print("deciphered:",substitute_decipher(text,chain))