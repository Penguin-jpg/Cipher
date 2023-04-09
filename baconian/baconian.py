# Python program to implement Baconian cipher

'''This script uses a dictionary instead of 'chr()' & 'ord()' function'''

'''
Dictionary to map plaintext with ciphertext
(key:value) => (plaintext:ciphertext)
This script uses the 26 letter baconian cipher
in which I, J & U, V have distinct patterns
'''
lookup = {'A': 'aaaaaa', 'B': 'aaaaba', 'C': 'aaabaa', 'D': 'aaabba', 'E': 'aabaaa',
          'F': 'aababa', 'G': 'aabbaa', 'H': 'aabbba', 'I': 'abaaaa', 'J': 'abaaba',
          'K': 'ababaa', 'L': 'ababba', 'M': 'abbaaa', 'N': 'abbaba', 'O': 'abbbaa',
          'P': 'abbbba', 'Q': 'baaaaa', 'R': 'baaaba', 'S': 'baabaa', 'T': 'baabba',
          'U': 'babaaa', 'V': 'bababa', 'W': 'babbaa', 'X': 'babbba', 'Y': 'bbaaaa',
          'Z': 'bbaaba', '0': 'aaaaab', '1': 'aaaabb', '2': 'aaabab', '3': 'aaabbb',
          '4': 'aabaab', '5': 'aababb', '6': 'aabbab', '7': 'aabbbb', '8': 'abaaab', '9': 'abaabb'}
# Added Numbers and an extra digit, because 2**6 > 36 > 2**5.
# Letters end in a, numbers end in b.

# Function to encrypt the string according to the cipher provided


def encrypt(message):
    cipher = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # adds the ciphertext corresponding to the
            # plaintext from the dictionary
            cipher += lookup[letter]
        else:
            # adds space
            cipher += ' '

    return cipher


# Function to decrypt the string
# according to the cipher provided


def decrypt(message):
    decipher = ''
    i = 0

    # emulating a do-while loop
    while True:
        # condition to run decryption till
        # the last set of ciphertext
        if (i < len(message) - 5):
            # extracting a set of ciphertext
            # from the message
            substr = message[i:i + 6]
            # checking for space as the first
            # character of the substring
            if (substr[0] != ' '):
                '''
                This statement gets us the key(plaintext) using the values(ciphertext)
                Just the reverse of what we were doing in encrypt function
                '''
                decipher += list(lookup.keys()
                                 )[list(lookup.values()).index(substr)]
                i += 6  # to get the next set of ciphertext

            else:
                # adds space
                decipher += ' '
                i += 1  # index next to the space
        else:
            break  # emulating a do-while loop

    return decipher


def main():
    message = "helloworld123"
    result = encrypt(message.upper())
    print(result)

    # message = "AABAAABBABABAABABBBABBAAA"
    result = decrypt(result.lower())
    print(result)


# Executes the main function
if __name__ == '__main__':
    main()