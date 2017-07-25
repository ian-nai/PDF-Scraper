# This code was adapted from DH Bridge's Introduction to Computational Thinking: http://curriculum.dhbridge.org/, https://github.com/dhbridge/curriculum

# Import Libraries
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import *
import csv
import os

# Set Variables
with open('scrape.txt', 'r') as file:
    cooking_text = file.read()

file = csv.writer(open('word_frequencies.csv', 'w'))

cooking_tokens = word_tokenize(cooking_text)
text = nltk.Text(cooking_tokens)

# Load in Stopwords Library
stopwords = stopwords.words('english')

word_set = []

# Define Functions
def normalize_text(text):
    # Work through all the words in text and filter
    for word in text:
        # Check if word is a word, and not punctuation, AND check against stop words
        if word.isalpha() and word.lower() not in stopwords:
            # If it passes the filters, save to word_set
            word_set.append(word.lower())
    return word_set

normalize_text(text)

fd = FreqDist(word_set)
print fd.most_common(200)

for key, count in fd.most_common(200):
    file.writerow([key, count])


pdf_again = raw_input("Save successful! Would you like to scrape another PDF?")
if pdf_again == "y":
    os.system("python pdf_scraper.py")
    exit(0)
if pdf_again == "n":
    print "Bye!"
    exit(0)
else:
    print "Please enter a valid input."
  
