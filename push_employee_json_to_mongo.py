# ALL LISTS USED HERE ARE AVAILABLE IN constants.py

# This code generates Random names first_name and last_name lists present in constants.py, 
# it takes department data from departments list in te
# and randomly selects one, and it randomly selects salary and date of birth
# and generates jsons of employee, which is then pushed to MongoDB

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
collection = db["employees"]

def generate_mongo_json():

    data_list = list()
    for index, each_name in enumerate(Constants.first_names):
        temp_json = dict()
        temp_json["user_id"] = f"user_{index + 1}"
        temp_json["name"] = (each_name + " " + choice(Constants.last_names)).title()
        temp_json["department"] = (choice(Constants.departments)).title()
        temp_json["salary"] = choice(salary_range)
        
        date_of_birth = datetime(
            year=choice(birth_year_range),
            month=choice(birth_month_range),
            day=choice(birth_date_range)
        )
        temp_json["date_of_birth"] = date_of_birth

        data_list.append(temp_json)

    collection.insert_many(data_list)
    
    

generate_mongo_json()