class libeary():
    def __init__(self, listofbooks): # this is called constructor by this we can directly write into class
        self.books = listofbooks   #this will store book in it as list
    def display_available_books(self):   #this is defined (method) function
        print("the present in the libeary are:  ") 
        for book in self.books: #this will print books in list
            print("*" + book)
    def barrow_book(self,bookname): #this barrow book function
        if bookname in self.books: #this will if book is available or not
            print(f"You have been issued {bookname} ,please keep it safe and return it after 30 days ") 
            self.books.remove(bookname)  #this will remove which we have chosen
            return True   #if it will return true then only it will work for student class
        else:    
            print("the book is not available and you have to wait till the book will be returned") 
            return False     
    def return_book(self,bookname): # this function is to return book
        self.books.append(bookname) # append function is used to add that book back in the list
        print("thanks for returing the book, we hope that you have enjoyed the book")
class student():   # this is student class
    def reqbook(self): # student can only 2 things 1 borroe book and return boo
        self.book = input("enter the book that you want to borrow")
        return self.book    # this part is little bit confusing
    def retbook(self):  
        self.book =input("enter the book that you want to return")
        return self.book
if __name__ =="__main__":   # this was if we want to import code and we don,t want to use code below this 
    student =student() # this object of student class taking nothing
    centrallibeary = libeary(["dbms", "python", "django", "algorithms"]) # this will automatically set values in class libeary
    #centrallibeary.display_available_books()
    # let make menu using infinite while loop
    while(True):
        msg =''' === welcome to the RSCOE libeary ===                
        1 -list of books
        2 -if you want to barrow book
        3 -if you want to return the book
        4 -if you want to quit the libeary'''
        print(msg)
        a =int(input("Please enter your choice "))
        if a==1 :
            centrallibeary.display_available_books()
        elif a == 2:
             centrallibeary.barrow_book(student.reqbook()) # this confusing
        elif a == 3 :
           centrallibeary.return_book(student.retbook()) # this confusing
        elif a == 4 :
            print("Thanks for using RSCOE Libeary")
            exit()
        else :
            print("invalid choice, please choose correct option !!!")
            
            
    