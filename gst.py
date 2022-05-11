 from asyncore import read
import csv
from datetime import datetime
from encodings import utf_8_sig
from lib2to3.pgen2.token import NEWLINE
from math import e
from operator import index
from pickle import FALSE, TRUE
from re import S
import os
from sqlite3 import Timestamp
import sys
import argparse
from time import sleep
from tracemalloc import stop



List = {
    "UK": ["2","4","6","8","10","12","14","16","18","20","22","24","26"],
    "US": ["00","0","2","4","6","8","10","12","14","16","18","20","22"],
    "FR": ["30","32","34","36","38","40","42","44","46","48","50","52","54"],
    "IT": ["34","36","38","40","42","44","46","48","50","52","54","56","58"],
    "JA": ["1","3","5","7","9","11","13","15","17","19","21","23","25"],
    "AU": ["2","4","6","8","10","12","14","16","18","20","22","24","26"],
    "ALPHA": [
        "No equivalent size available",
        "XXXS",
        "XXS",
        "XS",
        "S",
        "M",
        "L",
        "XL",
        "XXL",
        "XXXL",
        "No equivalent size available",
        "No equivalent size available",
        "No equivalent size available",
    ],
}
List2= []
csv_file = 'garments.csv'


#Function to handle the addtional arguments for the csv file convertion 
def readOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Additional commands to process CSV files.")
    parser.add_argument("-f","--file", type=str,required=False, help="Type the csv file name to convert.")
    parser.add_argument("-t","--target",required=False, help="Type your target locale.")
    my_args = parser.parse_args()
    return my_args

 #Function to validate size value and get its index from list.
def search(list, v):
    i = 1
    for i in range(len(List[ct])):
        if list[i] == v:
            my_pos = i
            return my_pos


#Function to read csv file and store it into a new list
def csv_function(file):
    with open(csv_file,'r') as f:
      count = 0
      csv_reader = csv.reader(f)
      for row in csv_reader:
            count = count+1
            List2.append(row) 
    #List2[0].append('size_convertion') 
        
            


#Clear screen            
os.system("cls" if os.name == "nt" else "clear")

# File conversion
# Commnad lines arguments
arg_option = readOptions(sys.argv[1:])

if arg_option.file is not None and arg_option.target in List.keys():
        csv_file=arg_option.file
        csv_function(csv_file)
        #CSV File conversion settings
        file_header = ['garment_id','coutry_code','size','size_'+arg_option.target]
        file = open('garment_converted.csv', 'w', encoding='utf_8_sig')
        writer = csv.writer(file)
        writer.writerow(file_header)
        # Index / values iteration
        from tqdm import tqdm
        for i in tqdm(range(len(List2)-1)):
            ...
            i=i+1
            gt= str(arg_option.target)
            gc=str(','.join(List2[i][0:1]))
            cc=str(','.join(List2[i][1:2]))
            ct = str(','.join(List2[i][1:2]))
            cs = str(','.join(List2[i][2:3]))
            y = (search(List[ct],cs))
            # Finding value index
            tc = List[gt][y]
            List3 = []
            # Comparing command line size argument with garment records
            if gt == cc:
                tc = 'SAME SIZE'
                #with open('garment_converted.csv', 'a') as file:
                List3 = [gc,cc,cs,tc]
                file = open('garment_converted.csv', 'a', newline='')   
                writer.writerow(List3) 
                file.close()
                
            else: 
               #with open('garment_converted.csv', 'a') as file:
                List3 = [gc,cc,cs,tc]
                file = open('garment_converted.csv', 'a', newline='')
                writer.writerow(List3)
        file.close()
        file_timestamp = datetime.now()
        sys.exit("Conversion completed! ")
else:
    pass              
               

    
# 1st. exercise requirement: 
#Command line conversion 

    my_option = ""
    while my_option != "quit":
        a = input("Enter your start locale: ")
        ct = a
        if a in List.keys():
                while True:
                    w = input("Enter you cloth size: ")
                    if w in List[a]:
                        break
                    else:
                        print("Invalid size, try again! ")

                while True:
                    c = input("Enter your target locale: ")
                    if c in List.keys():
                        x = search(List[ct],w)
                        print("Converted size is: " ,List[c][x])
                        my_option = input("Enter 'quit' to exit or any key to continue: ")
                        if my_option == "quit":
                            sys.exit()
                        else:
                            os.system("cls" if os.name == "nt" else "clear")
                            break
                    else:
                        print("Invalid target locale, try again! ")     
        else:
            print("Invalid start locale, try again! ")

    
