import random

# A list of words that
potential_words = ["panda", "fox", "sheep", "tiger", "pengiun"]

word = random.choice(potential_words)
#The number of indices in the word
aWord = word[0] + word[(len(word)-1):(len(word))]

# Use to test your code:
print("Welcome to Guess the Secret Animal! Game")
print("You have 7 tries at guessing letters included in the word")
print("Let's get started!")
# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
myWord = ["p", "a", "n", "d", "a" or "f", "o", "x" or "s", "h", "e", "e", "p" or "t", "i", "g", "e", "r" or "p", "e", "n", "g", "u", "i", "n"] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

myWord.append("_")

while fails < maxfails:
	guess = input("Guess a letter: ")
    usedLetters[]
    print(usedLetters)
	# check if the guess is valid: Is it one letter? Have they already guessed it?
    if guess in word:
        print("Getting Closer!")

    if guess not in word:
        print("Guess Again")
	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")

    if maxfails == 7
    break
