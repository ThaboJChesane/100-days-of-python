from lib2to3.pgen2.token import EQUAL


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def Caesar (startText, shiftAmount, cipherDirection):
    if cipherDirection == "decode":
        decrypt(startText,shiftAmount)
    elif cipherDirection == "encode":
        encrypt(startText, shiftAmount)
    else:
        print("Invalid input")


def encrypt(Plaintext, shiftAmount):
    mylist = []
    for letter in Plaintext:
        pos  = alphabet.index(letter)
        newPos = pos + shiftAmount
        if newPos > 26:
            newPos = newPos - 26
        mylist.append(alphabet[newPos])

    cipherText = "".join(mylist)
    print(cipherText)    

def decrypt(cipherText, shiftAmount):
    mylist = []
    for letter in cipherText:
        pos  = alphabet.index(letter)
        newPos = pos - shiftAmount
        if newPos < 0:
            newPos = newPos + 26
        mylist.append(alphabet[newPos])

    Plaintext = "".join(mylist)
    print(Plaintext)

    

Caesar(text, shift, direction)
