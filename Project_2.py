# Ilda Martinez
# Project2
# September2021
# 12pm Lab


# User Input
print('Welcome to the Pictures on the Go Program!')
print('The program will calculate how much space your storage device has.')
stop = False
while stop == False:

    # Variables
    storage = int(input('What is the capacity of the flash drive? '))



    MP = input('How many mega pixels does your camera have? (Choose 8, 12,or 16) ')
    while MP != '8' and MP != '12' and MP != '16':
        MP=input( 'Wrong value! Please enter 8, 12, or 16. ')
        
    if MP == '8':
        res= 3264 * 2448

    elif MP == '12':
        res= 4290 * 2800
        
    elif MP == '16':
        res= 4920 * 3264
        
        

    # Calculations
    oneJpeg = (res * 3 )/ 10
    onePNG =  (res * 3 )/ 8
    oneTIFF = (res * 6 )
    oneGIF = (res) / 5


    sSize = storage * 1000000000

    numJpeg = sSize / oneJpeg
    numPNG = sSize / onePNG
    numTIFF = sSize / oneTIFF
    numGif = sSize / oneGIF

    #Display Info
    print('The amount of space for Jpeg files is', (format(numJpeg, '.0f')))
    print()
    print('The amount of space for PNG files is', (format(numPNG, '.0f')))
    print()
    print('The amount of space for TIFF files is', (format(numTIFF, '.0f')))
    print()
    print('The amount of space for GIF files is', (format(numGif, '.0f')))
    print()
    #Repeat the program loop

    answer = input('Would you like to repeat the program? ')


    while answer != 'y' and answer != 'n':
        answer = input("please enter y or n ")

    if answer == 'n':
        stop == True
        print('Have an OKAY day!')
    


