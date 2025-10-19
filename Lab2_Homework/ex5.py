def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

try:
    num_input = int(input("Enter a number to check if it's a palindrome: "))

    if is_palindrome(num_input):
        print(f"The number {num_input} is a palindrome.")
    else:
        print(f"The number {num_input} is not a palindrome.")
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")