# dictionaries are an incrediblely helpful data structure

# we define a dictionary with curly braces
example_dictionary = {}

# we define with a dictionary entry with a 'key'
example_dictionary["Turtles"] = 4

# we can get a value out of a dictionary by accessing the key 
print(example_dictionary["Turtles"])

# we can make anything as the value to a key. Even another dictionary!
example_dictionary["Whale"] = ["down","up","over"]

#finally, we can access all keys or values
example_dictionary.keys()
example_dictionary.values()

#or, we can iterate over both
for key,value in example_dictionary.items(): #this gives us both the key and the value
    print(f"{key},{value}")


#lastly, we can check if something is in a dictionary by checking
if "Turles" in example_dictionary.keys():
    print('Turtles is there is there!')

if "Fish" in example_dictionary.keys():
    print("Fish is there is there!")