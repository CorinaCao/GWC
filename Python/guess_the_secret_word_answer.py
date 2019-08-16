import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
# current_word = ["_", "_"] # TIP: the number of letters should match the word
current_word = []
lengthOfCurrentWord = len(word)
for item in range(lengthOfCurrentWord):
    current_word.append("_ ")

print(current_word)
# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
    guess.lower()

	# check if the guess is valid: Is it one letter? Have they already guessed it?
    if guess.isalpha() == False:
        print("Please enter a letter!")
    elif guess in guesses == True:
        print("You guessed %s already, try again." %(guess))
    elif guess.isalpha() == True and len(guess) == 1 and guess not in guesses == True:
        guesses.append(guess)

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
    rightAns = True
    index = 0
    if guess in word:
        for char in word:
            if char == guess:
                current_word[index] = guessed
            index+=1
            if(index == (len(word))):
                break
    else:
	       fails = fails+1
	       print("You have " + str(maxfails - fails) + " tries left!")

    print(current_word)
    cword = ''.join(current_word)
    print(cword)
    if(cword == word):
        print("Good Job gUrl")
        break

    guessTheWord = input("Do you want to guess the word? Type Y for yes or N for no.")
    if guessTheWord == "Y":
        word_guess == word:
        print("You're correct!")
        break
    else:
        print("Wrong, try again.")
    elif guessTheWord == 'N':
        continue

        if fails == maxfails:
            print("Game Over")
