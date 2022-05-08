from math import e
from operator import index
from pickle import FALSE, TRUE
from re import S
import os
import sys


List = {
    "UK": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
    "US": [00, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
    "FR": [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54],
    "IT": [34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58],
    "JA": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],
    "AU": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
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


# Function to validate size value and get its index from list.
def search(list, v):

    i = 0
    for i in range(len(List[a])):
        if list[i] == v:
            my_pos = i
            return my_pos


os.system("cls" if os.name == "nt" else "clear")

my_option = ""
while my_option != "quit":

    a = input("Enter your start locale: ")
    if a in List.keys():
        if a == "ALPHA":
            while True:
                w = input("Enter you cloth size: ")
                if w in List[a]:
                    break
                else:
                    print("Invalid size, try again! ")

            while True:
                c = input("Enter your target locale: ")
                if c in List.keys():
                    x = search(List[a], w)
                    print("Your converted size is: ", List[c][x])
                    my_option = input("Enter 'quit' to exit or any key to continue: ")
                    if my_option == "quit":
                        sys.exit()
                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        break
                else:
                    print("Invalid target locale, try again! ")

        if a != "ALPHA":
            while True:
                b = int(input("Enter you cloth size: "))
                try:
                    val = int(b)
                    break
                except ValueError:
                    print("Invalid size value, try again!")
                if w in List[a]:
                    break
                else:
                    print("Invalid size, try again! ")

            while True:
                c = input("Enter your target locale: ")
                if c in List.keys():
                    x = search(List[a], b)
                    print("Your converted size is: ", List[c][x])
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

