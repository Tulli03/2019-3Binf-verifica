class Book:
    def __init__(self,title,author,publisher,year,pages,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.isbn = isbn
        self.is_bulky = pages > 500   
         

    def is_valuable(self,this_year):
        if this_year > self.year + 20 or this_year < self.year + 1:
            return True 
        else:
            return False
                
                
