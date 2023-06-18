#function an activity that is natural as a purpose for a person or thing

#input(), len(), int(), print()

# name = input("what is your name?")
# age = input("how old are you?")
# if age >= 18:
#     print("Welcome")
# else:
#     print("you cannot enter")

    #task separation
# def #defines keyword

# def ask_user_name():
#     name = input("what is your name?")
# return name

# def ask_user_age():
#     age = input("how old are you?")
#     if age >= 18:
#         print("Welcome")
#     else:
#         print("you cannot enter")

# parameters

# total = 0 #global
# def add(number, number2):  #parameters is 2 number created, and number2 created
# #     result = number + number2
#     return number + number2 #this 

# answer = add(2,3)
# print(answer)
# #print(result) wont work because result in a local variable
# print(total)

#exercises
#Q1
def get_integer(user_input):
    user_input = int(input("Could I please have an integer?: "))
    print(f"So your integer is {user_input}? Thanks!")
    return user_input
# ask = get_integer()


#Q2    
def celcius_convert(degrees_f):
    celcius = (5/9)*(degrees_f-32)
    return float(celcius)

def get_temp():
    user_input = int(input("May I have the temerature in Farenheit?: "))
    return user_input
    
# temp = celcius_convert(get_temp())
# print(temp)

#Q3
def odd_numb():
    int_odd = int(input("Could I please have an integer?: "))
    if int_odd % 2 == 1:
        return True
    else:
        return False

# print(odd_numb())

#Q4
def cost_all(unit_cost, num_unit):
    total = (float(unit_cost) * float(num_unit))
    print("$" ,total)
    return str(total)

cost_all(25.01, 4)