# PDF-Scraper
Python scripts to extract text from PDFs, save it as a text file, export a list of words and their frequencies to a CSV file for further analysis, extract dates from the text, and graph the text's parts of speech.

Standalone versions of the part of speech grapher and the date scraper can be found [here](https://github.com/ian-nai/PartofSpeech_Grapher) and [here](https://github.com/ian-nai/Date-Scraper), respectively.

## To Use:
* Download the scripts in the "scripts" folder
* Place the PDF files you'd like to scrape in the same folder as the scripts
* Run pdf_scraper.py

## Dependencies
* PDF Miner (https://github.com/euske/pdfminer)
* Natural Language Toolkit (https://github.com/nltk/nltk)
* Matplotlib (https://github.com/matplotlib/matplotlib)
* Pandas (https://github.com/pandas-dev/pandas)
* Datefinder (https://github.com/akoumjian/datefinder)

## Citations
* The code for sepwords.py was adapated from DH Bridge's *Introduction to Computational Thinking* curriculum, which is open source: https://github.com/dhbridge/curriculum, http://curriculum.dhbridge.org/
