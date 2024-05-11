# this is about the Class, superclass and Sub class

#1. we set one class as book:
class Book():
    #1.1 define  init with self, name of book and the Author:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    #1.2 define Str methode 
    def __str__(self):
        return '{}, by {}'.format(self.title, self.author)
    
#test the book:
myBook = Book('the Odysse', 'Homer')
print(myBook)