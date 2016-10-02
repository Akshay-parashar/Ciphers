from itertools import cycle

ALPHA = 'abcdefghijklmnopqrstuvwxyz'.upper()

def encrypt(key,plaintext):
    """Encrypt the string and return the cipher text"""
    plaintext = filter(str.isalpha,plaintext.upper()) # to remove non alpha characters particularly whitespaces here
    """or  you can also do this """
    # plaintext = plaintext.replace(" ","").upper()
    pairs = zip(plaintext,cycle(key.upper()))
    ciphertext = ''

    for pair in pairs:
        tot = reduce(lambda x,y: ALPHA.index(x) + ALPHA.index(y), pair)
        ciphertext += ALPHA[tot%26]

    return ciphertext.lower()

def decrypt(key,ciphertext):
    """Decrypt and return the decrypted string"""
    ciphertext = filter(str.isalpha, ciphertext.upper())
    """ or you can do the same as we did while encrypting """
    # ciphertext = ciphertext.replace(" ", "").upper()
    pairs = zip(ciphertext,cycle(key.upper()))
    plaintext = ''

    for pair in pairs:
        final = reduce(lambda x,y: ALPHA.index(x) - ALPHA.index(y),pair)
        plaintext += ALPHA[final%26]

    return plaintext.lower()


def run_prog():
    while True:
        print "Press e to encrypt or d to decrypt"
        choice = raw_input()
        if( choice in "e d" ):
            if( choice == 'e'):
                print "Enter message to encrypt: ",
                mess = raw_input()
                print "Enter key : ",
                key = raw_input()
                print encrypt(key,mess)
                return
            else:
                print "Enter message to decrpyt: ",
                ciph = raw_input()
                print "Enter key : ",
                key = raw_input()
                print decrypt(key,ciph)
                return
        else:
            print "Wrong input" 

run_prog()

            
