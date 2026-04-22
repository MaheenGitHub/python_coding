my_set = {"curly" , 2 , 2 , 4.5 , True}


my_set.add("new element")
print("adding one eemnt at a time: ", my_set)
print(len(my_set))

my_set.remove("new element")
print("removing one eemnt at a time: ", my_set)

# my_set.remove("what")     # Errror
print("error while removing unvailable elemnt: ", my_set)

my_set.discard("what")
print("no erro while discarding unvailable elemnt: ", my_set)

my_set.clear()
print("clear() set: " , my_set)

my_set.add((1,2,3))
print("adding tuple (any mutable) to list: ", my_set)

# my_set.add([4,5,6])       # Error
print("erorr ehile adding list to the set bzc list are mutable" )