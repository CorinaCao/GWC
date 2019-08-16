'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polaritylist = []
subjectivitylist = []

'''
# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
'''

for idx in range(len(tweetData)):
    tb = TextBlob(tweetData[idx]["text"])
    polaritylist.append(tb.polarity)
    subjectivitylist.append(tb.subjectivity)

'''
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
'''
print(polarityList)
#print(subjectivityList)

#This is a histogram for Twitter Data

#Create the graph
plt.hist(polarityList, bins = [-1,1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('Polarity')
plt.ylabel('Number of Tweets')
plt.axis(-1.1, 1.1, 0, 100)
plt.grid(True)
plt.show()
