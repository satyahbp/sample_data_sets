# This code generates random names, taking names from first_name list and last_names list
# available in the file constants.py

# The generate_names() below generates the random full names and add them to a 
# names.csv file.
# If you want to use the names for something, feel free to run it and generate the
# names.csv file and use the names, else modify the function according to your
# needs and use the names.

from random import choice
from constants import Constants

def generate_names():

    with open("names.csv", "a") as name_file:
        for each_name in Constants.first_names:
            current_name = (each_name + " " + choice(Constants.last_names)).title()
            name_file.write(current_name + "\n")

generate_names()