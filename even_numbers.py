def output_even_number(numbers):
    
    for index in range(1, numbers + 1):
        if index % 2 == 0:
            print(index) 
    return ""

result = output_even_number(20)
print(result)

