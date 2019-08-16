#This project takes in a question and an answer and assigns it
#to a dictionary.

#while loop
#use a varaible as a condition to exit out of while loop
done = "YES"

while done != "no":
    #initialize dictionary
    inputDictionary = {}
    #variable to take in the question
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

    done = input("Do you want to add another question?")

#print dictionary
print(inputDictionary)
