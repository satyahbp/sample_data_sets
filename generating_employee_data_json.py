# ALL LISTS USED HERE ARE AVAILABLE IN constants.py

# This code generates Random names first_name and last_name lists present in constants.py, 
# it takes department data from departments list in te
# and randomly selects one, and it randomly selects salary and date of birth
# and generates jsons of employee data in a file named employees.json. 

# date_of_birth is in YYYY-MM-DD format

# The number of jsons will be same as the number of names in first name.

# The generate_json() below generates the json. 
# Feel free to modify it according to your needs and use it.

import json
from random import choice
from datetime import date

from constants import Constants

salary_range = range(Constants.salary_start, Constants.end_salary)
birth_date_range = range(Constants.start_birth_date, Constants.end_birth_date)
birth_month_range = range(1, 13)
birth_year_range = range(Constants.start_birth_year, Constants.end_birth_year)

def generate_json():

    data_list = list()
    for index, each_name in enumerate(Constants.first_names):
        temp_json = dict()
        temp_json["user_id"] = f"user_{index + 1}"
        temp_json["name"] = (each_name + " " + choice(Constants.last_names)).title()
        temp_json["department"] = (choice(Constants.departments)).title()
        temp_json["salary"] = choice(salary_range)
        
        date_of_birth = date(
            year=choice(birth_year_range),
            month=choice(birth_month_range),
            day=choice(birth_date_range)
        )
        temp_json["date_of_birth"] = date_of_birth.strftime("%Y-%m-%d")

        data_list.append(temp_json)
    
    with open("employees.json", "w") as json_file:
        json.dump(
            obj=data_list,
            fp=json_file
        )

generate_json()