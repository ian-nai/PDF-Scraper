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
                   print("Bye!")
                   exit(0)
        if prompt == "q":
               print("Bye!")
               exit(0)
        else:
               print("Please enter a valid input.")
     if save == "n":
        if prompt2 == "n":
             print "Bye!"
             exit(0)
        else:
             print("Please enter a valid input.")
      
     
scraper()
    
                
