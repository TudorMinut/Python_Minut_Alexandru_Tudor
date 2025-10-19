def count_set_bits(number):
    return bin(number).count('1')

try:
    num_input = int(input("Enter a number to count its '1' bits: "))
    bits = count_set_bits(num_input)
    print(f"The number {num_input} (binary: {bin(num_input)}) has {bits} bit(s) with value '1'.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")