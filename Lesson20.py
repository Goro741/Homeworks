# 1. DicT
# You have two list convert it in dictionary and add 
# in (mydict.txt) and show result:
# import json
# first = ["Anie","Jesie","Ben"]
# second = [1,2,3]
# mydict ={}
# for j, i in zip(first, second):
#     mydict.setdefault(j,i)

# with open ("Gor.json", "w") as file:
#     json.dump(mydict, file)

# 2. JsOn
# Create json file and save them lyrics (song) 
# and print in cm d word this song
# import json
# lyrics1= "So, so you think you can tell\nHeaven from hell\nBlue skies from pain\nCan you tell a green field\nFrom a cold steel rail?\nA smile from a veil?\nDo you think you can tell?"
# with open("Lyrics.json","w") as file:
#     json.dump(lyrics1, file)
    
    
            



# 3. FuncTiOn
# Write a   python program which have one input an 
# integer, representing the s u m of all the multiples of 
# 3 and 5 below the given input. and save this result 
# in json file.
# for example:
# input 10 (3, 5, 6 and 9) 
# output:23
# import json
# number = int(input("Enter the number--------"))
# res = 0
# list1 =[]
# for i in range(1, number):
#     if i % 3 == 0 or i % 5 == 0:
#         res += i
#         list1.append(i)
# # print(res)
# with open ("New.json", "w") as file:
#     json.dump(res,file)   

# 4. VOweLs
# Write a program that takes in a string a s  input, 
# counts and outputs the number of vowels.
# And add result in json file.
# for example: 
# input: test 
# output: 1 
     
# import json
# text = input("Enter the text--------")
# res =0
# list1 =[]
# for i in text:
#     if i == "a" or i == "e" or i == "i" or i == "o":
#         res += 1
#         list1.append(i)
# print(list1,res)
# with open ("New.json","w") as file:
#     json.dump(res,file)       


# 5. TexT
# You have text.txt file and contains such text: 
# Another pause and more eying and siding around 
# each other
# You ca n create one dict where you have. 
# ‘’another’’:1
# ‘’and’’:2
# import json
# with open("Another.txt","w") as file:
#     file.write("Another pause and more eying and siding around each other")
# f = open("Another.txt","rt")    
# x = f.read()
# y = x.split()    
# list1 =[]
# bar_qanak1 = 0
# bar_qanak2 = 0
# bar = []
# list2 = []
# list3 = []
# mydict = {}
# for i in y:
#     list1.append(i)
#     if i == "and":
#         bar_qanak1 += 1
#         bar.append(i)
#     if i == "Another":
#         bar_qanak2 += 1
#         bar.append(i)    
# list2.append(bar_qanak2)
# list2.append(bar_qanak1)
# print(list2)
# print(bar)
# for j,z in zip(bar,list2):
#     mydict.setdefault(j,z)
# print(mydict)    
# with open("New.json","w") as file:
#     json.dump(mydict,file)

# 6. NEw LisT
# Write a python function which get a new list 
# from a given list, consisting of the first 
# repeating elements.
# my_list = [“a”,”b”,”a”,”c”,”b”] 
# output “a”,”b”,”c”
# my_list = ["a","b","a","c","b"]
# y = set(my_list)
# list1 = []
# for i in y:
#     list1.append(i)
# print(list1)    
