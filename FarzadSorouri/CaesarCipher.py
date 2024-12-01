import string

def caesar_encrypt(simpleText, shiftKey):
    newtext = []
    for i in simpleText:
        if i.isdigit():
            newtext.append(i)  # The numbers are unchanged
        elif i.isspace():
            newtext.append(i)  # Spaces are unchanged
        elif i in string.punctuation:
            newtext.append(i)  # Punctuation unchanged
        elif i.isalpha():  # The letters change
            # Checking whether the letter is small or large
            if i.islower():
                new_char = chr(((ord(i) - ord('a') + shiftKey) % 26) + ord('a'))
            else:
                new_char = chr(((ord(i) - ord('A') + shiftKey) % 26) + ord('A'))
            newtext.append(new_char)
        else:
            newtext.append(i)  # Other characters are unchanged
    result = ''.join(newtext)
    print(result)

if __name__ == '__main__':

    while True:
        inputtxt = input('Do you want to use the caesar_encrypt function?(Y/Yes): ')
        if inputtxt == 'Y' or inputtxt == 'y' or inputtxt.lower() == 'yes':
            encryptInput=input('Please insert your text and shift key separated by a space: ')
            parts= encryptInput.split()
            if  len(parts) != 2 or not (parts[1].lstrip('-').isdigit()):
                print("Error: Please provide both text and shift key!")
            else:
                text, key= parts[0], parts[1]
                caesar_encrypt(text, int(key))
        else:
            break
