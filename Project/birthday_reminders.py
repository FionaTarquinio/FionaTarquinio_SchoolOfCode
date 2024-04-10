from datetime import date

today = date.today()
today_day_in_year = (int(today.strftime("%j"))) # today as a number in year counting from 1 Jan
print(f"\nThe date today is {today}, which is day {today_day_in_year} of {today.year}.")

class Birthday(date):
    def __init__(self, year, month, day):
        super().__init__()
        
    def birthday_last_year(self): # returns date of birthday last year
        return date(today.year - 1, self.month, self.day)
    
    def birthday_in_current_year(self): # returns date of birthday in current year
        return date(today.year, self.month, self.day) 
    
    def birthday_next_year(self): # returns date of birthday next year
        return date(today.year + 1, self.month, self.day)
    
    def next_birthday(self): # returns date of next birthday
        if today <= self.birthday_in_current_year():
            return self.birthday_in_current_year()
        else:
            return self.birthday_next_year()
        
    def last_birthday(self): # returns date of last birthday
        if today > self.birthday_in_current_year():
            return self.birthday_in_current_year()
        else:
            return self.birthday_last_year()
    
    def days_to_next_birthday(self): # calculates number of days to next birthday from today
        number_of_days = self.next_birthday() - today
        return number_of_days.days
    
    def days_from_last_birthday(self): # calculate number of days since most recent birthday
        number_of_days = today - self.last_birthday()
        return number_of_days.days

    def age_next_birthday(self): # calculates age at next birthday
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

# ***TO INCLUDE ADDITIONAL BIRTHDAYS: add names and DOBs to birthday objects and birthday dictionary above***


def find_next_birthday():
    days_to_nearest_birthday = 366
    for key, value in birthday_dictionary.items(): # Run for loop to find next birthday/s
        a = value.days_to_next_birthday()
        if a < days_to_nearest_birthday:
            days_to_nearest_birthday = a
            person_with_nearest_birthday = key
            date_of_nearest_birthday = value.next_birthday()
            age_on_birthday = str(value.age_next_birthday())
        elif a == days_to_nearest_birthday:
            person_with_nearest_birthday = person_with_nearest_birthday + " and " + key
            age_on_birthday = age_on_birthday + " and " + str(value.age_next_birthday()) + " respectively"
    print(f"\nNext birthday is {person_with_nearest_birthday} on {date_of_nearest_birthday}.")
    print(f"This is in {days_to_nearest_birthday} days.")
    print(f"{person_with_nearest_birthday} will turn {age_on_birthday}.")

def find_last_birthday():
    days_from_last_birthday = 366
    for key, value in birthday_dictionary.items(): # Run for loop to find most recent birthday/s
        a = value.days_from_last_birthday()
        if a < days_from_last_birthday:
            days_from_last_birthday = a
            person_with_last_birthday = key
            date_of_last_birthday = value.last_birthday()
            age_last_birthday = str(value.age_next_birthday() - 1)
        elif a == days_from_last_birthday:
            person_with_last_birthday = person_with_last_birthday + " and " + key
            age_last_birthday = age_last_birthday + " and " + str(value.age_next_birthday() - 1) + " respectively"
    print(f"\nLast birthday was {person_with_last_birthday} on {date_of_last_birthday}.")
    print(f"This was {days_from_last_birthday} days ago.")
    print(f"{person_with_last_birthday} turned {age_last_birthday}.")

find_next_birthday()
find_last_birthday()