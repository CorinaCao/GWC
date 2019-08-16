'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!


import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarityList = []
subjectivityList = []


# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)


for idx in range(len(tweetData)):
    tb = TextBlob(tweetData[idx]["text"])
    polarityList.append(tb.polarity)
    subjectivityList.append(tb.subjectivity)


sum = 0
for polarity in polaritylist:
    sum = sum + polarity
    print(sum)

avgPolarity = sum /len(polaritylist)
print("the average polarity is : %f " %(avgPolarity))

sub_sum = 0
for subjectivity in subjectivitylist:
    sub_sum = sub_sum + subjectivity

    avesubjectivity =  sub_sum/len(subjectivitylist)
print("the average subjectivity is: %f" %(avesubjectivity))
#print(polaritylist)
#print(subjectivitylist)


print(polarityList)
#print(subjectivityList)

#This is a histogram for Twitter Data

#Create the graph
plt.hist(polarityList, bins = [-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('Polarity')
plt.ylabel('Number of Tweets')
plt.axis(-1.1, 1.1, 0, 100)
plt.grid(True)
plt.show()
'''

'''
In this program, we display a histogram of the polarities of all the tweets.
[OPTIONAL]
In this program, we will also display a scatter plot of polarity vs subjectivity.
For students who finish this part of the program quickly,
they might try out the optional graph. They might also try
using the larger tweet file to generate the graph (this might take a while).
They might also try to combine both graphs into one display.
They can also play around with different bins for the histogram
or try to draw centeredaxes on the scatter plot using matplotlib "spines".
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("../TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Create a Sentiment List
polarityList = []

#[OPTIONAL] Subjectivity
subjectivityList = []

#Get Sentiment Data
for tweet in tweetData:
	tweetblob = TextBlob(tweet["text"])
	polarityList.append(tweetblob.polarity)

	#[OPTIONAL] Subjectivity
	subjectivityList.append(tweetblob.subjectivity)


#Create the Graph
plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show() #Shows out graph

#Creating a Word Cloud with Twitter Data
combinedTweets = ""

#This is a for-loop that concatenates every tweet into one big string
for tweet in tweetData:
    combinedTweets += tweet['text']

#print(combinedTweets)

#making a textblob of our entire string of tweets
tweetBlob = TextBlob(combinedTweets)

#print(dir(textBlob))

#this is a list of words I dont want in my word cloud
wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could", "automation"]

#This creates an empty dictionary
filteredDictionary = dict()

#The point of this for-loop is to filter the words in our big tweet
for word in tweetBlob.words:

    #the following if-statement are conditions for what type of words I want in my word cloud

    #skip small words
    if len(word) < 2:
        continue

    #skip words with random characters of numbers
    if not word.isalpha():
        continue

    #skip words in our wordfilter list
    if word.lower() in wordsToFilter:
        continue

    if len(word) < 5 and word.upper() != word:
        continue

    filteredDictionary[word.lower()] = textBlob.word_counts[word.lower()]

#Create the word cloud
#this is the word cloud variable
wordCloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
#this shows our word cloud
plt.show()
