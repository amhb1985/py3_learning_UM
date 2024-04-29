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
cityName = ['Detroit','Ann Arbor', 'Pittsburgh','Mars', 'New York']
#1.2. creat another List for the Population for every City
population = [680000,116732, 30366, 14023, 850000]
#1.3. set or creat another List as States
states = ['MI', 'MI', 'PA', 'PA', 'NY']

#2. ZIP or add all of list in one list
city_tuple = zip(cityName, population, states)

