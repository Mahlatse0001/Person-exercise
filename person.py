class Person:
    def __init__(self,name,age,gender,interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        print("Hello, my name is" , self.name , "and I am" , self.age , "years old. My interests are" , self.interests[0] + "," , self.interests[1] , "and" , self.interests[2] + ".")

person = Person('Ryan',str(30),'male',['being a hardarse','agile', 'ssd hard drives'] )
person.hello()