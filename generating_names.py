# This code will generate Random names from the First and Last name written in the 
# respective lists.

# The generate_names() below generates the random full names and add them to a 
# names.csv file.
# If you want to use the names for something, feel free to run it and generate the
# names.csv file and use the names, else modify the function according to your
# needs and use the names.

from random import choice

first_names = [
    "satyajeet", "surya", "shiva", "poram", "sanjeeb",
    "sanjeev", "isani", "salonee", "jyoti", "anant",
    "deepak", "akaash", "yuvraj", "rahul", "ashutosh",
    "sudhi", "anurag", "biswajit", "biswa", "ramesh",
    "rajni", "anjali", "ravi", 
    "sumbul", "sonali", "sheetal", "partibha", "saswat",
    "lipsita", "manoj", "arpita", "amandeep", "ayushi",
    "shristy", "daya", "sneha", "uma", "aliva", 
    "soamesh", "shruti", "swati", "annu", "illisha",
    "raktim", "raj", "arpan", "prakash", "rupesh",
    "akshay", "prachi", "krishna", "madhuleena", "vaisakh",
    "aviral", "pramod", "mona", "smruti", "bhanu", 
    "ramya", "priyanka", "pooja", "tapan", 
    "varshini", "aaliya", "abhishek", "ajit", "chanchal"
    "ronak", "aayush", "ashish", "niraj", "namrata"
]

last_names = [
    "sahu", "sahoo", "kumar", "singh", "uppal", 
    "panda", "pandey", "math", 
    "bhat", "dutta", "mukherjee", "srivastava", "sinku",
    "sharma", "pradhan", "khattar", "nayak", "naik",
    "nair", "sinha", "nath", "chakraborty", "jena", 
    "dash", "das", "giri", "patra", "mallick", "maharana",
    "bag", "mohanty", "panigrahi", "barik", "mahapatra",
    "agrawal", "acharya", "banarjee", "chopra", "choudhary",
    "deshmukh", "bhardwaj", "jain", "jha", "joshi", 
    "kapoor", "lal", "patel", "patnaik", "prasad",
    "rao", "ray", "sarkar", "yadav"
]

def generate_names():

    with open("names.csv", "a") as name_file:
        for each_name in first_names:
            current_name = (each_name + " " + choice(last_names)).title()
            name_file.write(current_name + "\n")

generate_names()