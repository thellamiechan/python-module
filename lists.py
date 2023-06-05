#Lists - store multiple data points, take diferent data types, are index based (starts at 0)

# digits = [1,2,3,4,5] #string, float, int, etc
# # # print(list_name)
# # # print(type(list_name))
# # print(digits[4])
# # print(digits[-2]) #counts from back of list

# #slicing a section of the list
# # print(digits[0:4]) #start (inclusive): end index (exclusive) means +1
# # print(digits[3:5])
# print(digits[0:5:1]) #the final number means how many to skip 
# print(len(digits))  #prints length of list (5) how many elements


# digits = [1,2,3,4,5]
# print(digits)
# digits.append(6)
# print(digits)
# popped_element = digits.pop(0)
# print(popped_element)

# digits[1] = 90
# print(digits)

#nested lists
# letters = ['a', 'b', 'c', 'd', ["Emily", "Julie" ]]
# print(letters[4][1]) #get the internal list, then get the second element in nested element

# if 'a' in letters: #check if 'a' exists in list
#     print('It is in the list')

    #Exercises

# foods = ['orange', 'apple', 'banana', 'strawberry', 'grape', ['carrot', 'cauliflower', 'pumpkin'], 'passionfruit', 'mango', 'kiwifruit']

# print(foods[0])
# print(foods[2])
# print(foods[-1])
# print("first three items in list")
# print(foods[0:3])
# print(foods[-3:])
# print(foods[5][2])

# names = [ ["Monica", "in my life"],    ["Erica", "by my side"],    ["Rita's", "all I need"],    ["Tina's", "what I see"],    ["Sandra", "in the sun"],    ["Mary", "having fun"],    ["Jessica", "here I am"]]
# print("a little bit of", names[0][0], names[0][1])
# print("a little bit of", names[1][0], names[1][1])
# print("a little bit of", names[2][0], names[2][1])
# print("a little bit of", names[3][0], names[3][1])
# print("a little bit of", names[4][0], names[4][1])
# print("a little bit of", names[5][0], names[5][1])
# print("a little bit of", names[6][0], names[6][1])
# print("a little bit of you makes me your man (ah!)")
# print('*trumpet solo*')

# abc = input("Please give me three names: ")
# x= abc.split()
# print(x)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []


# abc = print([a,b,c])
a.extend(b)
print(a)
a.extend(c)
print(a)