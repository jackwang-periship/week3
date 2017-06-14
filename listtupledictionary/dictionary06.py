'''
Created on Jun 14, 2017

@author: jwang02
'''
import random
import requests
import pprint

# Load the data from remote location (URL)
f = requests.get("https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")

# Transform the bitstream into strings
text = f.content

# Split this single string at the end of lines
lines = text.split("\n")

# Initalising the dictionary
reviews = {}

# Filling the dictionary
for line in lines:
    l = line.strip().split("\t")
  
    # These are just training wheels to see more clearly what goes into the dictionary
    score = l[0] 
    id = l[1]
    title = l[2]
    review = l[3]
  
    reviews[id] = {"score" : score, "title" : title, "review" : review}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(reviews)

# Take a random key from the dictionary and print its value
pp.pprint(reviews[random.choice(list(reviews.keys()))])



