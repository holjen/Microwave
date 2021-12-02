# Microwave
This class is called Microwave. It is used to replicate a simple microwave. It can take in 3 arguments, food, which is the name of the food. Type, which is the type of food that the food argument is. The microwave class only takes in 3 types of food: leftovers, diary, and popcorn. Timer, which is the amount of time that the food will be microwaved.

self.__timer is the amount of time that the food is being microwaved
self.__food is the name of the food that is being microwaved
self.__type is the type of food that is being microwaved

Methods:

setTimer takes in 2 arguments: self and timer
self doesn’t need to be put in when calling the method
timer is the new time you want the food to be microwaved
It doesn’t return anything

getTimer takes in 1 argument: self
self doesn’t need to be put in when calling the method
It returns a string stating the time that is inputted into the microwave

setFood takes in 3 arguments: self, food, and type
self doesn’t need to be put in when calling the method
food is the new food you want to be microwaved
type is the type of the food you inputted
It doesn’t return anything

getFood takes in 1 arguments: self
self doesn’t need to be put in when calling the method
It returns a string stating the food you inputted and what type it is

checking takes in 1 argument: self
self doesn’t need to be put in when calling the method
It either returns True or False
If it returns False, it will print an error message before returning False

beginMicrowave takes in 1 argument: self
self doesn’t need to be put in when calling the method
It returns a string stating that you can use checkifEdible() to see if the food is edible

beginMicrowave takes in 1 argument: self
self doesn’t need to be put in when calling the method
It returns a string stating that the food is either not undercooked or is undercooked


Demo Program:
The demo program tests all the methods within the class. It starts with an initial timer, food, and type. All 3 arguments are then changed after using the two set methods. I then called the checking method and if it was true I would run the beginMicrowave() method and the checkIfEdible() method then print the results. I then printed what the 3 arguments were using the two get methods.

There are no special instructions needed to run the program, you can simply just press play
