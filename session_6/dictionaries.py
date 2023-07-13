# for element in student_phonebook:   #will give you keys only ( iterate all the value pairs) 
    # print(element, student_phonebook[element])        #<===unless you add 


# for example in student_phonebook:
# a,b = [1,2]
# print(a)
# print(b)

    # Lists 
# numbers = [1,2,3]
# numbers[0]
# Dictionary
# Keys are unique
# Values can be any data type
# Keys can only be immutable data types 
# Immutable - Strings, integers, floats, booleans
# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Pauline":444
#     }
# print(student_phonebook)
# del student_phonebook["Tracey"]
# student_phonebook["Cindy"] = 555
# print(student_phonebook)
# print(student_phonebook["Asli"])
# student_phonebook["Yara"] = 555
# print(student_phonebook)
# print(type(student_phonebook))

# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Pauline":444
#     }

# Iterate all the values in a dictionary
# for value in student_phonebook.values():
#     print(value)

# Iterate all the key-value pairs
# for key in student_phonebook:
#     print(key, student_phonebook[key])

# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)

# for key,value in student_phonebook.items():
#     print(key,value)


#Exercises
#Q1
# groceries = {"Baby Spinach": 2.78,"Hot Chocolate": 3.70,"Crackers": 2.10,"Coffee": 9.00,"Carrots": 0.56,"Oranges": 3.08}
# sum = 0
# for key, value in groceries.items():
#     x = int(input("Enter the amount for " + key + "  "))
#     sum += (x * value)
# print(f"Your grocery total is " + str(sum))

#Q2
import csv

# def check_colour_counts(filename):
#     colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}
#     with open(file = filename) as color_data:
#         reader = csv.reader(color_data)
#         for colour_row in color_data:
#             for key, value in colour_counts.items():
#                 if key.casefold() in colour_row.casefold():
#                     colour_counts[key] += 1
#     return colour_counts

# print(check_colour_counts("../session_5/PlusCSVExamples-main/colours_865.csv"))
#Q3
# with open(file = "../session_5/PlusCSVExamples-main/colours_20_simple.csv") as color_data:
#     reader = csv.reader(color_data)
#     new_dictionary = dict()
#     for line in color_data:
#         splitline = line.split(",")
#        # print(splitline[2].rstrip() + ", " + splitline[1] + ", " + splitline[0])
#         key = splitline[1]
#         value = splitline[2].rstrip()
#         new_dictionary[key]=value
#         # new_dictionary.setdefault(keys[i],value[i])
#         # add key then value to the new_dictionary
#         # for i in range(len(keys)):
#     for key,value in new_dictionary.items():
#         print(key, value)

#Q4
with open(file = "../session_5/PlusCSVExamples-main/colours_20_simple.csv") as color_data:
    reader = csv.reader(color_data)
    new_dictionary = dict()
    for line in color_data:
        splitline = line.split(",")
       # print(splitline[2].rstrip() + ", " + splitline[1] + ", " + splitline[0])
        key = splitline[1]
        value = splitline[2].rstrip(), splitline[0]
        new_dictionary[key]=value
        # new_dictionary.setdefault(keys[i],value[i])
        # add key then value to the new_dictionary
        # for i in range(len(keys)):
    for key,value in new_dictionary.items():
        print(key, value)
