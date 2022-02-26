# for i in range(1,251):
#     if i % 2 == 0 and i < 251:
#         print(i)
# sa patrasta

# a = [2,3,"Hello",45,"World"] 
# b = ["Hello", "Game",14,2,78,"Armenia",2]
# list1 = [] 
# for i in a:
#     if i not in b:
#         list1.append(i)
# print(list1)
# sa patrasta

# from collections import Counter
# text = "My friend wants to go to Madagaskar to work"
# list1 = []
# y = text.split()
# for i in y:
#     list1.append(i)
# z = max(list1, key=len)
# print(z)
# print(max(list1,key=list1.count))



# 2.Write a Python function to 
# calculate surface volume and area of 
# a cylinder(Գլան).
# V=πr^2h and A=2πrh+2πr^2 :
# import math
# def glan(r,h):
#     return r^2*h
# r = float(input("Enter r-----" ))
# h = float(input("Enter h ---------"))
# V = math.pi*r**2*h
# A = 2*math.pi*r*h + 2*math.pi*r**2
# print(V,A)
# print(math.pi)