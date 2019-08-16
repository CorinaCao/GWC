'''
In this program, we will print out all the text data from our twitter JSON file.
'''

import json

#Open JSON file. Tag file as "r" read only because we are only
#looking at the data.
tweetFile = open("../TwitterData/tweets_small.json", "r")

#We use the JSON library to get data from the file as JSON datascience
tweetData = json.load(tweetFile)

#Close the file now that we have locally stored the data
tweetFile.close()

#Print the data of ONE tweet
#The [0] denotes the *first* tweet object
print("Tweet id:", tweetData[0]["id"])

#Print text of first object
print("Tweet text: ", tweetData[0]["text"])

#Print out "text" key in JSON file
for idx in range(len(tweetData)):
    print("Tweet text: " + tweetData[idx]["text"])
