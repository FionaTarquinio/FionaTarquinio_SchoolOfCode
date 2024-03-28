#import time
from datetime import date

today = date.today()
today_day_in_year = (int(today.strftime("%j"))) # today as a number in year counting from 1 Jan
print(f"The date today is {today}, which is day {today_day_in_year} of {today.year}")

class Birthday(date):
    def __init__(self, year, month, day):
        super().__init__()

    def calc_birthday_day_in_current_year(self):
        birthday_date_this_year = date(today.year, self.month, self.day) 
        birthday_day_in_current_year = int(birthday_date_this_year.strftime("%j"))
        return birthday_day_in_current_year

    def calc_age_now(self):
        if self.calc_birthday_day_in_current_year() > today_day_in_year:
            age_now = today.year - self.year - 1
        else:
            age_now = today.year - self.year
        return age_now

#    def calc_days_to_birthday(self):
#        days_to_birthday = 

#    def add_new_birthday(self, year, month, day):
    


jesse = Birthday(1976, 9, 23)

print(jesse.calc_birthday_day_in_current_year())
print(jesse.calc_age_now())



#owen = Birthday(2008, 6, 29)
#leon = Birthday(2010, 10, 27)
#henry = Birthday(2012, 11, 14)




# Make list of people
# Function to define new birthday via user input and add to list
# Use for loop to evaluate days to birthday for each person in list and return person with fewest days to birthday and their age
