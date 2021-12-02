# Jennie Lin, Assignment 10.1: Your Own Custom Class
# This program will replicate what a microwave does, you can input a food and the type of food it is, as well as the time as arguments.
# Then you can call a method to microwave the food and then another function to check whether the food is undercooked based on the type

class Microwave:
    def __init__(self,timer = 0, food = None, type = None): # sets the default timer to 0 and the food and type to be None
        self.__timer = timer 
        self.__food = food
        self.__type = type

    def setTimer(self,timer): # replaces the timer with a new timer number
        self.__timer = timer

    def getTimer(self):
        return(f"The time you inputted is {self.__timer}.") # returns the current timer

    def setFood(self,food,type):  # replaces the food and type with a new food and type 
        self.__food = food
        self.__type = type

    def getFood(self):  # returns the current food and type 
        return(f"The food you inputted is {self.__food} and it is {self.__type}")

    def checking(self): # checks to see if inputted arguments are valid
        if self.__timer != 0 and self.__food != None and self.__type == "leftovers": #if all conditions are met, will return true
            return True
        elif self.__timer != 0 and self.__food != None and self.__type == "dairy":
            return True
        elif self.__timer != 0 and self.__food != None and self.__type == "popcorn":
            return True
        elif(self.__food == None or self.__type == None): # if the variables for food and type are set to None that means the microwave is empty
            print("This microwave is currently empty put in the food and it's type.")
            return False
        elif (self.__timer == 0): # if the timer is 0 then the user hasnt inputted a time
            print("You didn't put in a time.")
            return False
        else: # if the type isn't a valid food type, returns error message and False 
            print("Sorry this microwave can't handle the weird food you put in, I can only microwave leftovers, dairy, or popcorn. If you microwave the food, I will explode")
            return False

    def beginMicrowave(self): # "microwaves" the food
        for i in range(self.__timer + 1): # countsdown like a microwave does
            print(f"{self.__timer - i}...")
        print("Done! Thank this venerable microwave!!!") 
        return ("you can use checkIfEdible() to see if the food is edible") # prompts the user to call another function if they wish

    def checkIfEdible(self): # checks whether the food is edible (cooked)
        # these are the conditions for each type of food to make sure it's not undercooked
        if (self.__type ==  "leftovers" and self.__timer > 90) or (self.__type ==  "dairy" and self.__timer > 30) or (self.__type ==  "popcorn" and self.__timer > 180): 
            return (f"{self.__food} is at least not undercooked")
        else: # if the timer is under the time set for each type, it returns a string that says the food is undercooked
            return (f"{self.__food} is undercooked")



def main(): # testing the class and methods
    whatsInside = Microwave(91,"rice","dairy") #inital timer and food put into the microwave
    whatsInside.setFood("caramel popcorn","popcorn") # change the food inside the microwave to something else, changing the type in turn
    whatsInside.setTimer(181) # changes the timer 
    checking = whatsInside.checking() #checks whether the the arguments are valid
    if checking == True: 
        testing = whatsInside.beginMicrowave() # checks the microwaving method
        print(testing)
        testFood =  whatsInside.checkIfEdible() # checks whether the microwaved food is edible
        print(testFood)
        print(whatsInside.getFood()) # gets what food and type was microwaved
        print(whatsInside.getTimer()) # gets what time was used

if __name__ == "__main__":
    main()
    
