'''
friends = ["Beyonce", "Jay-Z", "Chrissy Teigen", "Barak Obama", "Stephen Colbert"]
weights = [153.4, 81.2, 1293.4, 432.6]
random_data = ["George", 8, 10.2]
'''
from random import *
#this is a LIST of women in tech
womenInTech = ["Amanda Randles", "Dr. Aprille Joy Ericsson", "Cindy Alvarez", "Dorothy Vaughan", "Jess Lee"]

#this is a FOR loop that PRINTS each name in the LIST
for women in womenInTech:
    print(women)

#this is a list named list that stores random data types
list = ["stuff", 2 ,343, "more stuff"]

#this is a FOR loop that PRINTS each data type from the list called 'list'
for item in list:
    print(item)

#one way to print out the number of women in tech is my list
print("This is the number of women attending the conference: ")
print(len(womenInTech))

#STORING THE SIZE OF THE LIST IN A VARIABLE CALLED 'numberOfWomen'
numberOfWomen = len(womenInTech)
print("This is the number of women attending the conference: %d" %(numberOfWomen))

#CHECKING TO SEE IF JESS LEE IS IN THE list
print("Is Jess Lee in the list?")
print("Jess Lee" in womenInTech)

#CHECKING TO SEE IF KRIS JENNER IS IN THE list
print("Is Kris Jenner a computer scientist?")
print("Kris Jenner" in womenInTech)

#Seeing a loop using the built in function called 'range'
for i in range(len(womenInTech)):
    print(womenInTech[i])

#This is how many times the for loop runs
limit = range(len(womenInTech))
#print("The range is: %d" %(limit)) #printing to confirm it is FIVE

#Seeing a loop using the built in function called 'range'
for i in range(len(womenInTech)):
    print(womenInTech[i]) #womenInTech[i] accesses the element at the index i

#chossing a random guest speaker
aRandomNumber = randint(0,5) #randint is a built in function that
                             #takes in a start and end
print("The random number generator chose: %d" %(aRandomNumber))

randomGuestSpeaker = womenInTech[aRandomNumber]
print(randomGuestSpeaker)
