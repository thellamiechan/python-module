# open(file="dogs_are_awesome.csv", mode="r", encoding ="utf-8") #these are the same (can use mode to change to Write)
# open(file = "dogs_are_awesome.csv")                             #because the last two are almost always givn

import csv
# with open(file="dogs_are_awesome.csv", mode="r", encoding ="utf-8") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)

# nested_list [['I', 'think', 'dogs', 'are,', 'awesome!']
# ['My,', "dog's", 'name', 'is,', 'Jett!']
# []
# ['I', 'love', 'him!']]
# with open(file="hello.csv", mode="w") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow(["Hello","Hi"])

# with open(file="2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

# population = []

# with open(file="2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         population.append(line)

# print(population)

# for age_group in population:
#     print(f"{age_group[0]} * {age_group[1]}")

# with open(file="population.csv", mode="w") as csv_file:
#     csv_writer = csv.writer(csv_file,delimiter="-")

    # for age_group in population:
        # age_group,frequency = age_group
        # print(age_group)
        # print(type(age_group))
        # print(frequency)
        # print(type(frequency))
        # csv_writer.writerow([age_group[0], age_group[1]])

        #Exercises

# with open(file = "PlusCSVExamples-main/colours_20_simple.csv") as color_data:
#     reader = csv.reader(color_data)
     
#     for line in color_data:
#         splitline = line.split(",")
#         print(splitline[0] + " " + splitline[1] + " " + splitline[2])

# with open(file = "PlusCSVExamples-main/colours_20_simple.csv") as color_data:
#     reader = csv.reader(color_data)
#     for line in color_data:
#         splitline = line.split(",")
#         print(splitline[2].rstrip() + ", " + splitline[1] + ", " + splitline[0])


# print(colours_to_test)

# def check_colour_count(filename):
#     colours_to_test = [["red",0],["green",0],["blue",0],["yellow",0]]
#     with open(file = filename) as color_data:
#         reader = csv.reader(color_data)
#         for colour_row in color_data:
#             for colour in colours_to_test:
#                 if colour[0].casefold() in colour_row.casefold():
#                     colour[1] += 1
# #     return colours_to_test

# print(check_colour_count("PlusCSVExamples-main/colours_20_simple.csv"))
# print(check_colour_count("PlusCSVExamples-main/colours_865.csv"))

a_list = []
with open(file = "PlusCSVExamples-main/galaxies.csv") as velocity:
    reader = csv.reader(velocity)
    for row in (velocity):
        splitrow = row.split(',')
        a_list.append(int(splitrow[1].rstrip()))
    minne = min(a_list)    
    maxie = max(a_list) 

print(f"The smallest velocity is the first {minne} and the largest velocity is the last {maxie}")

    
    


