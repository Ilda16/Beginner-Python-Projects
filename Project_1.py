#Ilda Martinez
#Project 1
#September 2021
#12:00pm LAB

#The program will calculate a cost of a trip using distance

#variables
MPG = float(input('What was the MPG for this trip? '))
pricePG = float(input('what is the price per gallon? '))
distance = float(input('How far will you travel? '))

#Calculations
gallonsUsed = distance / MPG
totalCost = pricePG * gallonsUsed

#Final cost 
print('The total cost of this trip is $', format(totalCost, '.2f'))
