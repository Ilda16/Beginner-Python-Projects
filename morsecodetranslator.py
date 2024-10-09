# Ilda Martinez
# Project 4
# OCTOBER2021
# 12pm Lab

# Welcome Message

print('Greetings, Welcome to the Morse Code translator program! ')
print()
print('The program will help you translate morse code to and from English.')
print()
print('Please remember to answer in spaces when translating morse code to english.')
print()

morseCodetranslator = (('A', '.-' ), ('B', '-...' ), ('C', '-.-.' ), ('D', '-..' ), ('E', '.' ), ('F', '..-.' ), ('G', '--.' ), ('H', '....' ),
                           ('I', '..' ),  ('J', '.---' ), ('K', '-.-' ), ('L', '.-..' ), ('M', '--' ), ('N', '-.' ), ('O', '---' ), ('P', '.--.' ),
                           ('Q', '--.-' ), ('R', '.-.' ), ('S', '...' ), ('T', '-' ), ('U', '..-' ), ('V', '...- ' ), ('W', '.--' ), ('X', '-..-'),
                           ('Y', '-.--' ), ('Z', '--..' ))

# While Loop
stop = False
while stop == False:
    output = ''

# Variables
    choose = input('Please choose M to go from morse code to English or E to go from english to morse code . ')
    choose = choose.upper()

    

    while choose != 'M' and choose != 'E':
        choose = input('INVALID RESPONSE! ENTER M TO TRANSLATE FROM MORSE CODE TO ENGLISH OR E TO TRANSLATE FROM ENGLISH TO MORSE CODE . ')
        choose = choose.upper()
        
    translatePhrase = input('What message would you like to translate? ')
        



# else if statements

    if choose == 'E':
        translatePhrase = translatePhrase.upper()
        fromIndex = 0
        toIndex = 1
    else:
        translatePhrase = translatePhrase.split()
        fromIndex = 1
        toIndex = 0

# TRANSLATION

    for letter in translatePhrase:
        located = False

        if choose == 'E':
            for mainIndex in morseCodetranslator:
                if letter == mainIndex[fromIndex]:
                    output = output + ' ' + mainIndex[toIndex]
                    located = True

        else:
            for mainIndex in morseCodetranslator:
                if letter == mainIndex[fromIndex]:
                    output = output + mainIndex[toIndex]
                    located = True


# OUTPUT LINES

    if choose == 'E':
        print(translatePhrase, 'is', output )
        print()
    else:
        print(translatePhrase, 'is', output )
        print()

# Repeat the program Loop

    answer = input('Would you like to repeat the program? Please enter y/n ')
    answer = answer.lower()
    print()
 
    while answer != 'y' and answer != 'n':
        answer = input('please enter y or n ')
        answer = answer.lower()

    if answer == 'n':
        stop = True
        print('Have a Great day :)!')
    
        

    
    
    
   
                    
        
        
        
        
        
