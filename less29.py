# 1. CALCuLATOr

# class Calculator:
#     def __init__ (self,x,y):
#         self.x = x
#         self.y = y

#     def gumar(self):
#         return self.x + self.y

#     def hanum(self):
#         return self.x - self.y

#     def bazmapatkum(self):
#         return self.x * self.y

#     def bajanum(self):
#         return self.x / self.y

# num1 = int(input("Enter number of x------"))
# num2 = int(input("Enter number of y------"))
# res1 = Calculator(num1,num2)
# print(res1.gumar())
# print(res1.hanum())
# print(res1.bazmapatkum())
# print(res1.bajanum())               

# 2.Create a class for Car and Person

# class Car:
#     def __init__ (self, model, date):
#         self.model = model
#         self.date = date
    
#     def mersedes(self):
#         return self.model, self.date

#     def toyota(self):
#         return self.model, self.date

       
# n = Car("Toyota",2014)
# c = Car("Mersedes",2022)
# print(c.mersedes())
# print(n.toyota())        

# class Person:
#     def __init__ (self, anun, azganun, job):
#         self.azganun = azganun
#         self.anun = anun
#         self.job = job

#     def proffesion(self):
#         return self.azganun, self.anun, self.job

# n = Person("Armen","Sargsyan", "doctor") 
# print(n.proffesion())   

# class Exchange:
#     def __init__ (self,USD):
#         self.USD = USD

#     def euro(self):
#         return self.USD * 0.91

#     def AMD(self):
#         return self.USD * 510

#     def rubl(self):
#         return self.USD *180

# dolar = float(input("Enter the dollar------"))
# x =Exchange(dolar)
# print(x.euro())
# print(x.AMD())
# print(x.rubl())