# Import PDF Miner, codecs, re, io, sys, and os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import codecs
import io
import sys
import os
import re
import nltk
import string
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
from nltk import tokenize
from string import ascii_letters, digits, punctuation, whitespace

def scraper():
     print "Welcome! First, enter the name of the PDF file you would like to scrape."

     # Specify the url
     filepath = raw_input("PDF file to scrape: ")
     
     pages=None
     if not pages:
        pagenums = set()
     else:
        pagenums = set(pages)

     output = StringIO()
     manager = PDFResourceManager()
     converter = TextConverter(manager, output, laparams=LAParams())
     interpreter = PDFPageInterpreter(manager, converter)

     infile = file(filepath, 'rb')
     for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
     infile.close()
     converter.close()
     text = output.getvalue()
     output.close
     print text 
    
     save = raw_input("Save the text file as scrape.txt? Note: this will overwrite your existing scrape file if you haven't renamed it from 'scrape.txt'. Type 'y' for yes or 'n' for no.")
     if save == "y":
        text_file = open("scrape.txt", "w")
        text = re.sub("\s\s+", " ", text)
        text_file.write("%s" % text)
        text_file.close()
        prompt = raw_input("Save successful! Type 'c' to continue, or 'q' to quit.")
        if prompt == "c":
               prompt3 = raw_input("Would you like to scrape another file? Type 'y' for yes or 'n' for no.")
               if prompt3 == "y":
                   scraper()
               if prompt3 == "n":
                   prompt4 = raw_input("Would you like to split the text into separate words? Type 'y' for yes and 'n' for no.")
                   if prompt4 == "y":
                           sep_words()
                   if prompt4 == "n":
                           print("Bye!")
                           exit(0)
        if prompt == "q":
               print("Bye!")
               exit(0)
        else:
               print("Please enter a valid input.")
     if save == "n":
             print "Bye!"
             exit(0)
     else:
             print("Please enter a valid input.")
                

def sep_words():

    print "Please enter the name of the text file you'd like to work with in the format [filename].txt. To use the text you just scraped, type 'scrape.txt'."

    text1 = raw_input("Filename: ")
    with open(text1, 'r') as file:
        f_text = file.read()
        tokenizer = nltk.word_tokenize
        tokens = tokenizer(f_text)
        for elem in tokens:
            print elem 
        
    save_sep_lines = raw_input("Would you like to save the words as 'words.txt'? Type 'y' for yes and 'n' for no.")
    if save_sep_lines == "y":
        text_file = open("words.txt", "w")
        for words in tokens:
            wordsplit = words.split()
            for word in wordsplit:
                text_file.write(str(word + '\n'))
        text_file.close()
    else:    
        start_over = raw_input("Would you like to run the program again? Type 'y' for yes and 'n' for no.")
        if start_over == "y":
            scraper()
        if start_over == "n":
            print "Bye!"
            exit(0)
        else: 
            print("Please enter a valid input.")
            
    start_over = raw_input("Would you like to run the program again? Type 'y' for yes and 'n' for no.")
    if start_over == "y":
        scraper()
    if start_over == "n":
        print "Bye!"
        exit(0)
    else: 
        print("Please enter a valid input.")
        
scraper()
                
