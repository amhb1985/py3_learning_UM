#adding other Methods in a Class

'''
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(slef):
        return self.x
    def getY(slef):
        return self.y
    

point1 = Point(10, 100)

#for printing both of our adding x and y we can use point1.x or .y
#it will comming bach in our point1 
print(point1.x)
print(point1.y)

'''

#so another example for the adding to class:

#1. we have the cities names as List
cityNames = ['Detroit','Ann Arbor', 'Pittsburgh','Mars', 'New York']
#1.2. creat another List for the Population for every City
populations = [680000,116732, 30366, 14023, 850000]
#1.3. set or creat another List as States
states = ['MI', 'MI', 'PA', 'PA', 'NY']

#2. ZIP or add all of list in one list
city_tuples = zip(cityNames, populations, states)
print(city_tuples)

#3.creat a class 
#3.1 def init method for/with 3 diffrent n p s and define every word
#3.2  def str method 
class City:
    def __init__(self, n, p, s):
        self.name = n
        self.poulation = p
        self.state = s
    def __str__(self):
        return '{},{} (pop: {})'.format(self.name, self.state, self.poulation)
'''
#4 create one empty List as citiies
cities =  []

#5. set a loop for city_tup in >> city_tuples
for city_tup in city_tuples:
    name, pop, state = city_tup
    city = City(name, pop, state) # instace of City class
    #and then we can see it as class but we must change the self.pop to poulation
    cities.append(city)
    print(cities)

    # we can see the all of result now
    #print(name, pop, state)
'''
#6 but now we can simple the levels 4 and 5 of level to below:
#cities = [City(n,p,s) for (n,p,s) in city_tuples]
#6.00 the another things that we'll use it that instead of (n,p,s) wer can use (*t). and (t). like this:
cities = [City(*t) for (t) in city_tuples]
print(cities) # we cal see the same result like further levels


