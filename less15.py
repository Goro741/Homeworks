# 1. New List
# Albert Zaqaryan Lesson 15
# Create new list which have 6 different data types.
# For example: str, int
#  mylist = ["a", 256, "Barev", 25.5, 25874, "Armenia"]


# 2. Mac
# Albert Zaqaryan Lesson 15
# Create new list which have data notebooks and you want check if  
# the data have Mac?
# For example: my_list =[“Hp”,“Asus”,“Dell”,“Mac”,”Lenovo”] 
# output: True

# my_list = ["Hp", "Asus", "Dell", "Mac","Lenovo"]
# for i in my_list:
#     if i =="Mac":
#          print("True")
          
# 3. Password
# Albert Zaqaryan Lesson 15
# Create python program which will check if your password is strong 
# or no. if Len your password is great than 8 and if your password have  
# 2 numbers and 2 of the following special characters ('!', '@', '#', '$', '%', 
# '&', '*') Sample Input: Python@$World11
# Sample Output: Strong

# chars = ("@","#","$","%")
# while True:
#     password = input("enter the password------").title()
#     tver = 0
#     chars1 = 0
#     if len(password) < 8:
#       print("your password is weak")
#       continue
#     for i in password:
#         if i.isdigit():
#             tver += 1
#         elif i in chars:
#             chars1 += 1
#     if tver < 2:
#         print("Input 2 numbers")
#     if chars1 < 2:
#         print("Input 2 chars")
#         continue
#     else:
#         print("You password is strong")
#         break               

# 4. Link Finder
# Albert Zaqaryan Lesson 15
# Create python program where you want to findid in link if link have 
# id print id.
# Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU 
# Sample Output: RWW2aUSwvU

# link = "https://www.youtube.com/watch?v=sqGYGA0AAEo"
# print(link[(link.index("=")+1):])        

# 5. Sign in
# Albert Zaqaryan Lesson 15
# Create python program where you want to check if input word is 
# palindrome or no .if yes print Open otherwise Trash
# Sample Input: RACECAR  
# Sample Output: Open 
# text = input("enter the word-----")
# if text == text[:: -1]:
#     print("true")
# else:
#     print("trash")    


# 6. String-to-List
# Albert Zaqaryan Lesson 15
# Create python program to convert string to a list.

# 6. String-to-List
# Albert Zaqaryan Lesson 15
# Create python program to convert string to a list.
# text = "Armenia"
# print([text])

# 7. Even Numbers
# Albert Zaqaryan Lesson 15
# Create python program which will show all even numbers in your 
# string. Note: you have input where have 5 numbers:
# Sample Input: 12 21 15 19 8
# Sample Output: 12 8

# number = input("enter the number------")
# number = number.split(" ")
# for i in number:
#     if int(i) % 2 == 0:
#         print(i)

# 8. Odd
# Albert Zaqaryan Lesson 15
# Write a Python program to select the odd items of a list. And delete 
# even items
# mylist = [25, 36, 17, 13, 25, 99, 24]
# odd_number = [] 
# for i in mylist:
#     if i % 2 != 0:
#         odd_number.append(i)
# print(odd_number)

# 9. Secret Santa
# Albert Zaqaryan Lesson 15
# Your group have 5 people and each of them can  
# take one name and when take this name is delete 
# from this list.And he can not take his name: 
# mylist = ["Rafo", "Narine", "Karine","Armen","Syuzi","Karen"]
# for i in range(len(mylist)):
#     print(mylist[i], "----", mylist[(i +1) % (len(mylist))])        
        
# 10. Duplicate
# Albert Zaqaryan Lesson 15
# Create a python program which delete all  
# duplicate items in list.
# mylist = [1, "Armenia",25,"Barev", 25, 1]
# print(list(set(mylist)))