# Ilda Martinez
# Project6(Final)
# December2021
# 12pm Lab


# Welcome Message function

def displayWelcome():
    print('Welcome to the Shipping Program!')
    print()
    print('The program will calculate shipping costs in different states.')
    print()

# user input of what state they want to calculate
def getState():

    # abreviated states list(Tuple)
    abrevStates = (('AL'), ('AK'), ('AZ'), ('AR'), ('CA'), ('CO'), ('CT'), ('DE'), ('FL'), ('GA'),
                   ('HI'), ('ID'), ('IL'), ('IN'), ('IA'), ('KS'), ('KY'), ('LA'), ('ME'), ('MD'),
                   ('MA'), ('MI'), ('MN'), ('MS'), ('MO'), ('MT'), ('NE'), ('NV'), ('NH'), ('NJ'),
                   ('NM'), ('NY'), ('NC'), ('ND'), ('OH'), ('OK'), ('OR'), ('PA'), ('RI'), ('SC'),
                   ('SD'), ('TN'), ('TX'), ('UT'), ('VT'), ('VA'), ('WA'), ('WV'), ('WI'), ('WY'),
                   ('DC'))

    # user input of state
    chooseState = input('Please enter an abbreviated state. ')
    chooseState = chooseState.upper()
    print()

    # Error check while loop
    while chooseState not in abrevStates:
        chooseState = input('INVALID RESPONSE! PLEASE ENTER THE CORRECT ABBREVIATED STATE. ')
        chooseState = chooseState.upper()
        print()

    return(chooseState)

# error check function for all of user input
def errorCheck(inp):
    try:
        value = float(inp)
        stop = True

    except ValueError:
        print('INVALID RESPONSE!')
        stop = False
        value = ''

    return(value, stop)

# User Input Function assighnment/error check
def productInput():
    
    itemList = []
    
    quantInput = True

    # Quantity input/error check
    while quantInput == True:

        quantStop = False

        while quantStop == False:
            quantity = input('Please enter the quantity (Enter 0 if done): ')
            print()
            quantity, quantStop = errorCheck(quantity)

        if quantity == 0:

            quantInput = False
        
        # weight input/ error check
        else:
            weightStop = False

            while weightStop == False:
                itemWeight = input('Please enter the weight of the item: ')
                print()
                itemWeight, weightStop = errorCheck(itemWeight)

            costStop = False

            # cost input/ error check
            while costStop == False:
                itemCost = input('Please enter the cost of the item: ')
                print()
                itemCost, costStop = errorCheck(itemCost)

                
            itemList.append([quantity, itemWeight, itemCost])
            
    return itemList
            
            
# Calculation function for variables
def calculations(itemList, chooseState):
    boxWeight = 0

    subTotal = 0
    
    #Calculations for items
    for mainIndex in range(len(itemList)):
        quantity, itemWeight, itemCost = itemList[mainIndex]

        boxWeight = boxWeight + quantity * itemWeight
        
        subTotal = subTotal + quantity * itemCost

    # Tax error check for input if input is California
    if chooseState == 'CA':
        tax = subTotal * .08
    
    else:
        tax = 0.00

# Shipping and Handeling calculations
    shipping = .25 * boxWeight

    if boxWeight == 0:
        handeling = 0

    elif boxWeight < 10:
        handeling = 1

    elif boxWeight > 100:
        handeling = 5

    else:
        handeling = 3

# Calculating totals of total due and the shipping and handeling costs
    shipHand = shipping + handeling

    totalDue = subTotal + tax + shipHand

    return(subTotal, tax, shipHand, totalDue)

# Format of the Final Display
def formatSubtotal(subTotal, tax, shipHand, totalDue):
    print(format('SubTotal:', '<25'), format(subTotal, '>25,.2f'))
    print()

    print(format('Tax:', '<25'), format(tax, '>25,.2f'))
    print()

    print(format('Shipping and Handeling:', '<25'), format(shipHand, '>25.2f'))
    print()

    print(format('Total Due:', '<25'), format(totalDue, '>25.2f'))
    print()


 # User input asking for the Repetition the program loop   

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


# ------Main------

# While Loop
stopMain = False
while stopMain == False:

# Display Function
    displayWelcome()

# defined choose state to equal state tuple function
    chooseState = getState()

# defined item list to equal user input function, so item list can have inputs
    itemList = productInput()

# The variables are retrieving user inputs and calculating 
    subTotal, tax, shipHand, totalDue = calculations(itemList, chooseState)

# Formatting Display Info
    formatSubtotal(subTotal, tax, shipHand, totalDue)

# repeat of the program loop check

    stopMain = repeatProgram()
