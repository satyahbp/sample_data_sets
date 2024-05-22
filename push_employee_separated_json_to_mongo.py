# ALL LISTS USED HERE ARE AVAILABLE IN constants.py

# This code generates Random names first_name and last_name lists present in constants.py, 
# it takes department data from departments list in te
# and randomly selects one, and it randomly selects salary and date of birth
# and generates 3 different lists of employees and pushes to MONGODB

# The number of jsons will be same as the number of names in first name.

# The generate_mongo_json() below generates the data. 
# Feel free to modify it according to your needs and use it.

# Just change the host and port to your host and port before running it. By default it is localhost:27017

import pymongo
from random import choice
from datetime import datetime

from constants import Constants

salary_range = range(Constants.salary_start, Constants.end_salary)
birth_date_range = range(Constants.start_birth_date, Constants.end_birth_date)
birth_month_range = range(1, 13)
birth_year_range = range(Constants.start_birth_year, Constants.end_birth_year)

host = "localhost"
port = "27017"
mongo_connection = pymongo.MongoClient(f"mongodb://{host}:{port}/")

db = mongo_connection["organisation"]
employees_collection = db["employees"]
salary_collection = db["salary"]
dob_collection = db["dob"]


def generate_mongo_json():

    name_list = list()
    salary_list = list()
    dob_list = list()
    for index, each_name in enumerate(Constants.first_names):
        user_id = f"user_{index + 1}"
        name = (each_name + " " + choice(Constants.last_names)).title()
        department = (choice(Constants.departments)).title()
        salary = choice(salary_range)
        date_of_birth = datetime(
            year=choice(birth_year_range),
            month=choice(birth_month_range),
            day=choice(birth_date_range)
        )
        
        name_list.append({
            "user_id": user_id,
            "name": name,
            "department": department
        })

        salary_list.append({
            "user_id": user_id,
            "salary": salary
        })

        dob_list.append({
            "user_id": user_id,
            "date_of_birth": date_of_birth
        })

    employees_collection.insert_many(name_list)
    salary_collection.insert_many(salary_list)
    dob_collection.insert_many(dob_list)
    
    

generate_mongo_json()