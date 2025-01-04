import random as r # we can import modules using other name. Some modules by convention are imported as something else
import random 
# importing thing from the internet is really helpful! Python comes with several default modules.
# things like the math module are pretty useful


#we can use random for several operations

#we can shuffle
sorted_numbers = [1,2,3,4,5]
random.shuffle(sorted_numbers)

#pick a random number
random_number = random.randint(1,10) # inclusive

#choose a randomom things from a list
colors = ["blue","red","green","purple"]
random_color = random.choice(colors)

