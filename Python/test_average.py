'''
#1 Make a list of ages.
ages = [2, 22, 16, 4, 17]

#2 Add all ages. -> store in a variable
sum = 0
for age in ages:
    sum += age

#Print sum to verify that it is correct
print("The sum of all ages is %d" %(sum))

#3 Divide by length
average = sum/len(ages)

#Print the average to verify that it is correct
print("The average age is: %d" %(average))
'''

#This program will create a list of ages (through user input) AND calculates the average

#This is a list that will store all of the user's ages
listOfAges = []

#This is a variable that acts as a counter for how many ages are in the list
numberOfAges = 0

while(numberOfAges <=5):
    #This retrieves user input and stores it into a variable called 'age'
    age = input("Please enter an age: ")
    #age = int(age)
    print(age)
    listOfAges.append(age) #append=built in function that adds age to list
    numberOfAges+=1

print("Here is your list: ")
print(listOfAges)
