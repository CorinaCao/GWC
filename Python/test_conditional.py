'''
leftHandUp = True
rightHandUp = False

if(leftHandUp and rightHandUp):
    print("Jump!")
elif(leftHandUp or rightHandUp):
    print("one hand up but not both!")
else: 7
    print("no hands up?")
'''

leftHand = input("left hand up or dowm?")
rightHand = input("right hand up or down?")

if(leftHand == "up" and rightHand == "up"):
    print("Jump!")
elif(leftHand == "down" or rightHand == "down"):
    print("one hand up but npt both!")
else:
    print("no hands up!")
