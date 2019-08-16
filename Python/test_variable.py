print("Variable Example")

#string variable for my name
my_name = "Corina"
#interger variable for my age
my_age = 15

#print my name and age
print(my_name)
print(my_age)

#asking user how old their mom is
your_moms_age = input("How old is your mom?")
print(your_moms_age)

#printing my_name, my_age, and my_moms_age
print("Hello my name is %s. I am %d years old. My mother is %s years old." %(my_name, my_age, your_moms_age))

print("An Example on Counters")

#initializing variables.
#num_guesses increments by 1 and is the counter.
#num_loop increments by 1. keeps track of iterations
num_guesses = 0
num_loop = 0
while True:
    num_guesses += 1 #increments by 1 every iteration
    num_loop += 1

    print("You made %d guesses. This is loop number %d." %(num_guesses, num_loop))

    if(num_guesses == 100):
        print("num_guesses has reached 100. Loop with stop")
        break
