# custom object string output 

class book():
    def __init__(self,title,author,year):
        self.title = title
        self.author = author 
        self.year = year
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
p1 = book("The Great Gatsby","F. Scott Fitzgerald ",1925)
print(p1)
