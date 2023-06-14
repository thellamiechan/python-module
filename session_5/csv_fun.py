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

population = []

with open(file="2016_pilbara.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        population.append(line)

# print(population)

# for age_group in population:
#     print(f"{age_group[0]} * {age_group[1]}")

with open(file="population.csv", mode="w") as csv_file:
    csv_writer = csv.writer(csv_file,delimiter="-")

    for age_group in population:
        # age_group,frequency = age_group
        # print(age_group)
        # print(type(age_group))
        # print(frequency)
        # print(type(frequency))
        csv_writer.writerow([age_group[0], age_group[1]])
