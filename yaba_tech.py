import numbers

def prime_numbers(numbers):
    
    prime =[] 

for numbers in numbers:

    if number > 1:

        is_prime = True

         
for i in range(2, num):

    if num % i == 0:

         is_prime = False
#         break
    if is_prime:
   
        primes.append(num)

return primes


print(prime_numbers([5, 9, 3, 6, 2]))


def replace_negatives(numbers):
    esi = []

    for num in numbers:
        if num < 0:
            esi.append(0)
        else:
             esi.append(num)

    return esi


print(replace_negatives([5, -9, 3, -6, 2, -11]))


def move_all_zeros_to_the_end(numbers):

    my_result = []

    for number in numbers:

     if number > 0:
            my_result.append(0)
    else:
            my_result.append(number)

    return my_result

print(move_all_zeros_to_the_end([5, 0, 3, 0, 2, 0]))

 
def duplicate_eelements(numbers):


