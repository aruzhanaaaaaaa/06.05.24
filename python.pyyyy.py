#attr - атрибут
#class  A :
    #attr = 'Helo world'
    #def hello(self):
        #print(self.attr)


#сlass  A :
   ## attr = 'Helo world'
    #def hello(self):
        #print(self.attr)

#obj1 = A()
#hello = obj1.hello()
#print(hello)


#class Person:
    #def __init__(self,name,age):
        #self.name = name
        #self.age = age


    #def my_method(self):
        #print("Менің атым "+ self.name)
#p1 = Person("Dauren",18)
#p1.my_method()


#class Person:
    #def __init__(self,name,age):
        #self.name = name
       # self.age = age


    #def my_method(self):
        #print("Менің атым "+ self.name, "жасым " ,self.age, "де")
#p1 = Person("Dauren",18)
#p1.my_method()


class Person:
    def __init__(self, name, age, surname):
        self.name = name
        self.age = age
        self.surname = surname

    def my_method(self):
        print("Менің атым " + self.name, "жасым ", self.age, "және тегім ", self.surname, "де")

p1 = Person("Аружан", 18, "Исалдаева")
p1.my_method()



class Person:
    def __init__(self, name, age, surname=""):
        self.name = name
        self.age = age
        self.surname=surname

        
    def my_method(self):
        if self.surname:
            print("Менің атым "+ self.name, self.surname ,"жасым ", self.age, )
            
        else:
            print("Менің атым "+ self.name,"жасым " ,self.age, "де " )
       

p1 = Person("Аружан",18,"Исалдаева")
p1.my_method()
p1 = Person("Аружан",18,"")
p1.my_method


class Car:
    def _init_(self,marc,subname,age):
        self.marc = marc
        self.subname = subname
        self.age = age

    def my(self):
        print("Марка "+ self.marka, self.subname , self.age)

p1 = Car("Tayota", "Camry" , 2024)
p1.my()
