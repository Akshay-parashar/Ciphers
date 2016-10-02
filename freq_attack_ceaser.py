ALPHA = 'abcdefghijklmnopqrstuvwxyz'
freq = [0]*26

def freq_attack(ciphertext):
    plaintext = ''
    ciphertext = filter(str.isalpha,ciphertext.lower())
    for i in range(0,len(ciphertext)):
        freq[ALPHA.index(ciphertext[i])] += 1
    most_occ_char = ALPHA[freq.index(max(freq))]
    shift = abs(ord(most_occ_char)- ord('e'))
    #Now as we know the shift val we can decipher it easily
    for char in ciphertext:
        tot = ord(char)
        tot = (((tot - 97)-shift)%26)+97
        plaintext += chr(tot)
    return plaintext
        
    



        
    
