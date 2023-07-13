class Dog:
    # state/attributes
    # name = "Jett"
    # age = 4
    # breed = "pug"

def __init__(self, dog_name, dog_age, dog_breed):
    self.name = dog_name
    self.age = dog_age
    self.breed = dog_breed
    self.weight = dog_weight
    
    def eat(self):          #refers to itself
        print("nom nom") 
        self.weight += 0.5 

    # def talk(self):
    #     print("bark bark")          

    # dog1 = Dog("jett", 4, "pug")   #instantiate
    # dog2 = Dog("Ninja", 13, "dutch-shepard")
    dog3 = Dog()