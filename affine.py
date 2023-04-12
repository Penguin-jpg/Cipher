# Implementation of Affine Cipher in Python
 
# Extended Euclidean Algorithm for finding modular inverse
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 
 
# affine cipher encryption function
# returns the cipher text
def affine_encrypt(text, key):
    # remove the space in the string
    text = text.replace(' ', '')
    cipher = ''
    for t in text:
        # calculate x: 0~9 no change; A~Z is 10~35; a~z is 36~61
        if ord(t) < 65:
            x = ord(t)-ord('0')
        elif ord(t) > 90:
            x = ord(t)-ord('a')+36
        else:
            x = ord(t)-ord('A')+10
        
        # calculate C: C = (a*P + b) % 62
        x = ( key[0]*x + key[1] ) % 62

        # product the Cipher: x = 0~9 -> number 0~9; x = 10~35 -> A~Z; x = 36~61 -> a~z
        if x < 10:
            cipher+=chr(x + ord('0'))
        elif x > 35:
            cipher+=chr(x - 36 + ord('a'))
        else:
            cipher+=chr(x - 10 + ord('A'))
    
    return cipher
 

# affine cipher decryption function
# returns original text
def affine_decrypt(cipher, key):
    plain = ''
    for c in cipher:
        # calculate y: 0~9 no change; A~Z is 10~35; a~z is 36~61
        if ord(c) < 65:
            y = ord(c)-ord('0')
        elif ord(c) > 90:
            y = ord(c)-ord('a')+36
        else:
            y = ord(c)-ord('A')+10
        
        # calculate P: P = (a^-1 * (C - b)) % 62
        y = (modinv(key[0], 62)*(y - key[1])) % 62

        # product the Plain: y = 0~9 -> number 0~9; y = 10~35 -> A~Z; y = 36~61 -> a~z
        if y < 10:
            plain+=chr(y + ord('0'))
        elif y > 35:
            plain+=chr(y - 36 + ord('a'))
        else:
            plain+=chr(y - 10 + ord('A'))
    
    return plain
    # return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ])

 
# Driver Code to test the above functions
def main():
    # declaring text and key
    text = 'Hello 123'
    key = [17, 20]
 
    # calling encryption function
    affine_encrypted_text = affine_encrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
 
    # calling decryption function
    print('Decrypted Text: {}'.format( affine_decrypt(affine_encrypted_text, key) ))
    
    
 
if __name__ == '__main__':
    main()
# This code is contributed by
# Bhushan Borole