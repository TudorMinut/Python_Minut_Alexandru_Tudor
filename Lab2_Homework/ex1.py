import math

def find_gcd_of_list_loop(numbers):
    if not numbers:
        return None
    
    result = numbers[0]
    
    for i in range(1, len(numbers)):
        result = math.gcd(result, numbers[i])
        
    return result

try:
    input_str = input("Enter multiple numbers separated by space: ")
    number_list = [int(num) for num in input_str.split()]
    
    if len(number_list) < 2:
        print("Please enter at least two numbers.")
    else:
        result = find_gcd_of_list_loop(number_list)
        print(f"The Greatest Common Divisor is: {result}")

except ValueError:
    print("Invalid input. Please enter only integers separated by space.")
