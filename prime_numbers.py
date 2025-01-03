
def find_primes(to_find_to,another_parameter):
    primes = [2]
    for number in range(2,to_find_to):
        is_prime = True
        #loop through all numbers below it, and see if any of them are divisible
        for divisor in primes: #test loop
            if number % divisor == 0: # if the number is evenly divisable
                is_prime = False
        if is_prime:
            primes.append(number)
    return primes

primes = "Yes Please!"
list_of_primes = find_primes(1000,"hi")

print(list_of_primes)

print(primes)


integer = 7

while integer < 10:
    integer = integer + 1
    print(integer)


more_than_20 = False
while more_than_20 == False:
    print(integer)
    integer = integer + 1
    if integer >= 20:
        more_than_20 = True


my_other_list = [1,2,3,45,56]
loop_done = False
counter = 0
while loop_done != True:
    if counter == len(my_other_list) -1:
        loop_done = True
    print(my_other_list[counter])
    counter += 1 #counter = counter + 1