#import time
from datetime import date

today = date.today()
today_day_in_year = (int(today.strftime("%j"))) # today as a number in year counting from 1 Jan
print(f"The date today is {today}, which is day {today_day_in_year} of {today.year}")

class Birthday(date):
    def __init__(self, year, month, day):
        super().__init__()
        
    def birthday_in_current_year(self): # returns date of birthday in current year
        return date(today.year, self.month, self.day) 
    
    def birthday_in_next_year(self): # returns date of birthday in next year
        return date(today.year + 1, self.month, self.day)
    
    def next_birthday(self): # returns date of next birthday
        if today <= self.birthday_in_current_year():
            return self.birthday_in_current_year()
        else:
            return self.birthday_in_next_year()
    
    def days_to_next_birthday(self): # calculates number of days to next birthday from today
        number_of_days = self.next_birthday() - today
        return number_of_days.days

    def age_next_birthday(self):
        if self.birthday_in_current_year() > today:
            return today.year - self.year
        else:
            return today.year - self.year + 1
        
# Instantiate Birthday objects:

jesse = Birthday(1976, 9, 23)
fiona = Birthday(1980, 5, 26)
owen = Birthday(2009, 6, 29)
leon = Birthday(2010, 10, 27)
henry = Birthday(2012, 11, 14)

birthday_dictionary = {
    "Jesse":jesse,
    "Fiona":fiona,
    "Owen":owen,
    "Leon":leon,
    "Henry":henry
}

birthday_list = [jesse, fiona, owen, leon, henry]

for birthday in birthday_list:
    a = birthday.days_to_next_birthday
    print(a)

