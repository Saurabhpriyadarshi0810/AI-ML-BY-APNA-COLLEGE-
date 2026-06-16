class Book:
    author =""
    title= ""
    review = []
    

    def __init__ (self ,  name , title  , review ):
        self.author = name 
        self.title = title
        self.review = [review]
        

    def add_review(self, review):
        self.review.append(review)
        self.count+=1
        print(f"reiview added : {review}")

    def display(self):
        
        print(self.review)

    def count_review(self):
        
        print(f"there are {len(self.review)} reviews")


b=Book("Ruskin Bond"  , "Atomic habit  " , "good book")
b.add_review("nice book")
b.count_review()
b.display()