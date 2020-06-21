import string

def addChar(a,b):
    AB.insert(0, a)
    AB.append(b)

def encrypt(text):
    code = ""

    for char in text:
        code += AB[len(AB) - AB.index(char) - 1]
    return code

AB = list(string.ascii_lowercase)
addChar(" ", ",")
addChar("é", "á")

while True:
    print(encrypt(str(input("Encripitar: ").lower())))
    print()