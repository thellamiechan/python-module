# letters = ['a','b','c']
# print(letters[0])
# print(letters[1])
# print(letters[2])

#loops help us perform a task multiple times
#2 types of loops

#While loops
# count = 0
# while 5 > count:
#     print('hello')
#     count = count + 1

# name = input("what is your name?" )
# while name != "Ashley":
#     print("I don't know you")
#     name = input("What is the new name?" )


#For loops

# letters = ['a','b','c']
# for letter in letters:  #letter = 'a', then letter = 'b', then letter = 'c'
#     print(letter)

# for number in range(0,10): #range produces a range of integers
#     print (number)

# students = [
#     ["cindy", "emily", "eve"]
#     ["julie", "maddy", "andrea"]
#     ["jenny", "sarah", "yara"]
# ]
# for student in students:
#     print(student)
#     for name in student:
#         print(name)

# count = 0
# while 5 > count:
#     print(f"hello, the number is {count}")
#     count += 1

# Exercises While loop

# Q1
# number = input("give me a number:  ")
# sum = 0
# while number:
#     sum = sum + int(number)
#     number = input("give me a number:  ")
# print(sum)   

# Q2
# count = input("give me a number:  ")
# while count:
#     number = range(1, int(count), 2)
#     for n in number:
#         print(n)
#     count = input("give me a number:  ")
    
# Q3
# count = input("give me a number:  ")
# i=1
# while i in range(1,int(count),2):
#    print(i,end=" ")
#    i=i+2    

# large_number = int(input("enter a number: "))# by oriane
# while (large_number > 0):
#     if large_number % 2 != 0:
#         print(large_number)
# large_number = large_number -1


# Q4
# secret_number = 8
# while(user_query != secret number):
#     user_query = int(input("Guess the number:  "))
#     if user_query > secret_number:
#         print("Too high...")
#     else user_query < secret_number:
#         print('Too low...')
    # user_query = int(input("Guess the number:  "))
#    
# print("You guessed it!!")


# selected_number = 8
# while True:
#     user_number = int(input("Guess a number: "))

#     if user_number < selected_number:
#         print("Too low...")
#     elif user_number > selected_number:
#         print("Too high...")
#     else:
#         print("Congratulations! You guessed the correct number.")
#      break


#Exercises For Loops

# Q1
# user_input = int(input("Enter a number: "))
# for i in range(1,11):
#     result = user_input * i
#     print(f"{user_input} x {i} = {result}")

# Q2
# user_input = int(input("Enter a number: "))
# sum = 0
# for i in range(user_input):
#     sum += i
# print(sum)

# Q3
# my_list = [4, 5, 6, 7, 8]
# sum = 0
# for x in my_list:
#     sum += x
# print(sum)

# Q4
# lyrics = [["Monica", "in my life"],
#           ["Erica", "by my side"],
#           ["Rita's", "all I need"],
#           ["Tina's", "what I see"],
#           ["Sandra", "in the sun"],
#           ["Mary", "having fun"],
#           ["Jessica", "here I am"]]

# result = ""

# for item in lyrics:
#     line = "A little bit of " + item[0] + " " + item[1] + ";"
#     result += line

# result += "A little bit of you makes me your man (ah!)*trumpet solo*"

# print(result)

#exercises nested loops

#Q1
groceries = [ ["Baby Spinach", 2.78], ["Hot Chocolate", 3.70], ["BBQ Shapes", 9.00], ["Bread", 2.10], ["Carrots", 0.56], ["Oranges", 3.08]]
sum = 0
for food in groceries:
    x = int(input("Enter the amount for " + food[0] + "  "))
    sum += (x * food[1])
# print("Your total is: $" + str(sum)) 

#Q2 by Cinzia
number = 84
repeat = 'yes'
while repeat != 'no':
    guess = int(input("Guess a number:  "))
    while number != guess:
        if guess < number:
            print("Too low, try again")
        else:
            print("Too high, try again")
        guess = int(input("Make another guess:  ")) 
    print("you got it right!!")   
    repeat = input("Do you want to play again? Type 'no' to exit")
   
    



