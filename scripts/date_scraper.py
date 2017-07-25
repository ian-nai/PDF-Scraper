import datefinder
import datetime
import os

def date_scraper():

    with open("scrape.txt", 'r') as file1:
        text1 = file1.read()

    string_with_dates = text1

    matches = datefinder.find_dates(string_with_dates)

    for match in matches:
        print match
   
    
    saving = raw_input("Would you like to save these as 'dates.txt'? Note: this will overwrite previous saves. Type 'y' for yes and 'n' for no.")
    if saving == "y":
        text_file1 = open("dates.txt", "w")
        string_with_dates = text1
        matches = datefinder.find_dates(string_with_dates)
        for match in matches:
            string_dates1 = (str(match))
            text_file1.write(string_dates1 + '\n')
        text_file1.close()
        pdf_again = raw_input("Save successful! Would you like to scrape another PDF?")
        if pdf_again == "y":
            os.system("python pdf_scraper.py")
            exit(0)
        if pdf_again == "n":
            print "Bye!"
            exit(0)
        else:
            print "Please enter a valid input."
    if saving == "n":
        pdf_again = raw_input("Would you like to scrape another PDF?")
        if pdf_again == "y":
            os.system("python pdf_scraper.py")
            exit(0)
        if pdf_again == "n":
            print "Bye!"
            exit(0)
        else:
            print "Please enter a valid input."
    else:
        print "Please enter a valid input."

date_scraper()
