class vehicle :
    brand = ""
    model =""

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class bike(vehicle):
    engine = "00cc"
    
    def __init__(self , brand , model , engine ):
        self.brand =brand
        self.model = model
        self.engine = engine

    def display(self):
        print(f"the bike is of {self.brand} brand and {self.model} is  the model and the engine of {self.engine}")

class car(vehicle):
    seat = 0
    
    def __init__(self , brand , model , seat ):
        self.brand =brand
        self.model = model
        self.seat = seat

    def display(self):
        print(f"the car is of {self.brand} brand and {self.model}  is  the model and is {self.seat} seater car")


b = bike("honda" ,"CB200x" ,"220cc")
b.display()

c = car("renault " , "triber" , 7)
c.display()