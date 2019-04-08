
import sys
# simple program to onver English text into morse and vice versa
# "SOS" and "sos" should be turned into "***---***"
# "***---***" should always produce "SOS" not "sos"

# interface command: "python converter.py targetMessageFile.txt"

#initialize the dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def main():

    # read characters from a file (.txt is fine)
    targetFile = open(sys.argv[1], "r")
    message = (targetFile.read()).upper()
    print message
    # check the message; is it morse or english
    firstInitial = message[0]

    if firstInitial is '.' or firstInitial is '-':
        # convert morse to string
        convertToString(message)
        print "Transltaion done! Check for new .txt file in the folder."
        print "File is named 'converted_string_message.txt'"
    else:
        # convert string to morse
        convertToMorse(message)

        print "Transltaion done! Check for new .txt file in the folder."
        print "File is named 'converted_morse_message.txt'"



def convertToString(msg):
    print("convert to string")



def convertToMorse(msg):
    print("convert to morse")
    converted_message = ''
    for letter in msg:
        if letter != ' ':
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            converted_message += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            converted_message += ' '

    # create an output text file and paste the result in it
    outputFile = open('converted_morse_message.txt', 'w+')
    outputFile.write(str(converted_message))

if __name__ == '__main__':
    main()




# dictionary for morse characters


# Function to encrypt the string
# according to the morse code chart
'''
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher
'''
# Function to decrypt the string
# from morse to english
'''
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :
                 # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    return decipher
'''
