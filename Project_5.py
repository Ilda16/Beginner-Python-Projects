# Ilda Martinez
# Project5 with Functions
# October2021
# 12pm Lab

# Welcome Messages
def displayWelcome():
    print('Hello Welcome to the Metric Conversion Program!')
    print()
    print('This program was created to help you! The user to find metric conversions quick and easy with short responses.')
    print()



# user input of the metric units

def measurementInput():
    unit = input('what unit would you like to convert (O, G, I, C, M, or K? ')
    unit = unit.upper()
    print()


    while unit != 'O' and unit != 'G' and unit != 'I' and unit != 'C' and unit != 'M' and unit != 'K':
        unit=input('INVALID RESPONSE! Please enter (O, G, I, C, M, or K. ')
        unit = unit.upper()


    Measurement = float(input('What is the unit you would like to calculate? '))

    return unit, Measurement

# else if statements that are calculating the unit conversions


def unitCalculations(unit, Measurement):
    if unit == 'O':
        print()
        ouncesTograms = Measurement * 28.3495231
        print(Measurement, 'ounces is equal to', format(ouncesTograms, '.2f'), 'grams.')
        print()

    elif unit == 'G':
        print()
        gramsToounces = Measurement / 28.3495231
        print(Measurement, 'grams is equal to', format(gramsToounces, '.2f'), 'ounces.')
        print()

    elif unit == 'I':
        print()
        inchesTocentimeters = Measurement * 2.54
        print(Measurement, 'inches is equal to', format(inchesTocentimeters, '.2f'), 'centimeters.')
        print()

    elif unit == 'C':
        print()
        centimetersToinches = Measurement /2.54
        print(Measurement, 'centimeters is equal to', format(centimetersToinches, '.2f'), 'inches.')
        print()

    elif unit == 'M':
        print()
        milesTokilometers = Measurement * 1.609344
        print(Measurement, 'miles is equal to', format(milesTokilometers, '.2f'), 'kilometers.')
        print()
        
    elif unit == 'K':
        print()
        kilometersTomiles = Measurement / 1.609344
        print(Measurement, 'kilometers is equal to', format(kilometersTomiles, '.2f'), 'miles.')
        print()

        
    # Repeat the program loop  

def repeatProgram():
    stop = False
    
    answer = input('Would you like to repeat the program? Please enter y/n ')
    answer = answer.lower()
    print()
 
    while answer != 'y' and answer != 'n':
        answer = input('please enter y or n ')
        answer = answer.lower()

    if answer == 'n':
        stop = True
        print('Have a Great day :)!')

    return stop


    # ----MAIN----

 # While Loop
stopMain = False

while stopMain == False:

    # Welcome messages

    displayWelcome()

    # user input of metric units

    unitMain, measurementMain = measurementInput()

    # Units are calculated

    unitCalculations(unitMain, measurementMain)

    # repeat of the program loop check

    stopMain = repeatProgram()
