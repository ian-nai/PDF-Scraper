import nltk
from nltk import word_tokenize
from collections import Counter
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as mpl
import pandas as pd
import os

def grapher(): 

    with open("scrape.txt", 'r') as file1:
        text1 = file1.read()
    
    tokenizer = nltk.word_tokenize
    tokens = tokenizer(text1)
    text =  nltk.Text(tokens)
    tags = nltk.pos_tag(text)


    counts = Counter(tag for word, tag in tags)
    print counts

    graphtags = [tag for word, tag in tags]
    graphfreqs = nltk.FreqDist(graphtags)
    graphfreqs.tabulate(25)
    graphfreqs.plot(20)
    
    pdf_again = raw_input("Would you like to scrape another PDF?")
    if pdf_again == "y":
        os.system("python pdf_scraper.py")
        exit(0)
    if pdf_again == "n":
        print "Bye!"
        exit(0)
    else:
        print "Please enter a valid input."
           
grapher()




    
