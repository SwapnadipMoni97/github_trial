def is_divisible_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0

# Example usage
number = int(input("Enter a number: "))
if is_divisible_by_3_and_5(number):
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")