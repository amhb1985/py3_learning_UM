#this is aabout the example in inherit:
# in thsi example we try calculte the age with the current year as 2024

#1 first of all we must set one class like this:

current_year = 2024
class Person:
    #1.1 then we define inint (naturally with self, name, and the year of birth)
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born

    #1.2 so we need define the getAge and erduce this from Current Year
    def getAge(self):
        return current_year - self.year_born
    #1.3 like our tset for the Bank acount we mus at end define
    # a String for Show our result:
    def __str__(self):
        #then we need with {} set/order the text with our datas

