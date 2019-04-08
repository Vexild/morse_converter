
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

    #break up the parameters
    targetFileName = open(sys.argv[1], "r")
    outputFileName = sys.argv[2]
    convertMode = sys.argv[3]

    #get the message
    message = (targetFileName.read()).upper()
    print message

    if convertMode == 'tostring':
        # convert morse to string
        convertToString(message, outputFileName)


    if convertMode == 'tomorse':
        # convert string to morse
        convertToMorse(message, outputFileName)

    if convertMode == None:
        print "Please select converting method: 'tomorse' to turn string into morese"
        print "or 'tostring' to turn morse into string"


def convertToString(msg, endfile):

    # Small adjustments have been made considering the task description.
    # Logic in the description was to seperate characters with dots and make possible there can
    # be no double dots. In this function the logic goes: characters are separated with space and
    # words are separated with 2 spaces like "sos sos" -> ... --- ...  ... --- ...


    converted_message = ''
    morseCharacter = ''
    for letter in msg:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            morseCharacter += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2 :
                 # adding space to separate words
                 converted_message += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                converted_message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morseCharacter)]
                morseCharacter = ''
    outputFile = open(endfile, 'w+')
    outputFile.write((converted_message).upper())

    print "Transltaion done! Check for new .txt file in the folder."
    print "File is named '"+endfile+"'"


def convertToMorse(msg, endfile):
    converted_message = ''
    for letter in msg:
        if letter != ' ':
            # convert every single character into morse character.
            # a space is also added before next character
            converted_message += MORSE_CODE_DICT[letter] + ' '
        else:
            # second space is added to separate words
            converted_message += ' '

    # create an output text file and paste the result in it
    outputFile = open(endfile, 'w+')
    outputFile.write(converted_message)

    print "Transltaion done! Check for new .txt file in the folder."
    print "File is named '"+ endfile +"'"

if __name__ == '__main__':
    main()
