class Student :
    __name = "" 
    __roll_no = 0
    __marks = 0 

    def __init__ (self , name , rollno , marks ):
        self.__marks = marks
        self.__name = name 
        self.__roll_no = rollno

    def set_name (self, name ):
        if name == "":
            print("invalid input !")
        else :
            self.__name = name 

    def set_rollno (self, rollno ):
        if rollno < 1 or rollno > 100 :
            print("invalid input !")
        else:
            self.__roll_no = rollno 

    def set_marks (self,marks ):
        if marks < 0 :
             print("invalid input !")
        else:
            self.__marks = marks


    def get_name(self):
        print(self.__name)

    def get_marks(self):
        print(self.__marks)
    def get_rollno(self):
        print(self.__roll_no)

s = Student("vaishnavi" , 42 ,  75)

s.set_marks(100)
s.set_name("Saurabh")
s.set_rollno(34)

s.get_name()
s.get_rollno()
s.get_marks()