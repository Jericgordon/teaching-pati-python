# variables 
    #types
    #duck typing -
var1 = 2 #integer
var4 = 2.2 #float
var2 = "hello" #string
var3 = "a" # character
my_other_variable = True

var5 = "6"
var5 = int(var5)

print(var1 == var3)

# lists

my_list = [1,2,3,4.2,"UnitedHealthcare","hello"] # 

list_of_numbers = [5,7,2,3,5]

#arithmatic

print("Modulo Example")
print(5 % 2)

# if



# for / for each loop
for item in list_of_numbers:
    if (item % 2) == 0:
        print(item)
    else:
        print("not even")

for number in range(len(list_of_numbers)):
    list_of_numbers[number] = list_of_numbers[number] + 1

print(list_of_numbers)

my_number = list_of_numbers.pop()
print(list_of_numbers)
print(my_number)



# while loop

#dictionaries 

