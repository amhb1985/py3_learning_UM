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
        #then we need with return and {} set/order the text with our datas
        return 'Hello dear {} your age is: ({}).'.format(self.name, self.getAge() )
    
#so at the end we test our code we some name
# we must set one name for our varibleand use Person() as our main class 
# and then add one String AND   then the year of birth

#Joe = Person('Joe Becker', 1977)
#print(Joe)
# so we will chnage the all of code with the input commend:
#so it isnt currect and we must change it again
'''
t0=Person(input(str('whats your name: '))
                ,input(int())
print(t0)

'''
# so now we will copy the class to make another class as  Student.
#so every Student is a person:
class Student(Person):
    #1.1 then we define inint (naturally with self, name, and the year of birth)
    def __init__(self, name, year_born ):
        self.name = name
        self.year_born = year_born
        #we set another for self.knowleg
        self.knowledge = 0

    #so now we define another Methode for the Study:
    def study(self):
        self.knowledge =+ 1

    #1.2 so we need define the getAge and erduce this from Current Year
    # so in this case we must remove get age from the student class
   ''' def getAge(self):
        return current_year - self.year_born
        '''
    #1.3 like our tset for the Bank acount we mus at end define
    # a String for Show our result:
    def __str__(self):
        #then we need with return and {} set/order the text with our datas
        return 'Hello dear {} your age is: ({}).'.format(self.name, self.getAge() )

alice = Student('Alice Smithe', 1989)
#print(alice)
alice.study()
print(alice.knowledge)



