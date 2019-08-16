#The project takes in questions and an answer and assigns it
#to a dictionary
#while loop
#use a variable as a condition to exit out of the while loop
addQues = "yes"
#initialize dictionary
inputDictionary = {}
#inputDictionary = {}
listOfAnswers = []
while True:
    #varialble to take in the question
    key = input("Type in a question: ")

    #variable to take in the answer
    answer = input("Answer: ")

    while answer == "":
        print("I need an answer!")
        print(key)
        answer = input("Answer: ")
    #set key:answer
    inputDictionary[key] = answer
    #               'Diana' = 30

    addQues = input("Do you want to add another question? ")

    if addQues == "no":
        newUser = input("Do you want to add a new user? ")
        if newUser == "yes":
            listOfAnswers.append(inputDictionary)
            inputDictionary = {}
            continue
        elif newUser == "no":
            listOfAnswers.append(inputDictionary)
            break

#print list
print(listOfAnswers)
