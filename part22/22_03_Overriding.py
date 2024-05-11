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
#2. we can change the 2 sub-class to e e-books and papaer books:
#Notice : inside of() we must set our main Class. >>> here is Book
class PaperBook(Book):
    # we define  the methode init 
    # 2.2 we must our main Class (here Book) join with init >>> IT IS NOT SELF !!!
    def __init__(self, title, author, numPages):
        Book.__init__(self, title, author)
        # we set self for Number of pages
        self.numPages = numPages
#3. like another sub class for Paperpage we will create another for the e-book:
class eBook(Book):
    # we define  the methode init 
    # 2.2 we must our main Class (here Book) join with init >>> IT IS NOT SELF !!!
    def __init__(self,title,  author, size):
        Book.__init__(self, title, author)
        # we set self for size of Books
        self.size = size

#test the book:
myBook = PaperBook('the Odysse', 'Homer', 500)
print(myBook)
print(myBook.numPages)



