import input

def sum_invalid_ids(min, max):
    """
    Calculates the sum of numbers in a given range [min, max] that have duplicate first and second halves of their digits.

    Args:
        min (int): The starting number of the range.
        max (int): The ending number of the range.

    Returns:
        int: The sum of all numbers satisfying the condition.
        
    Example:
        sum_invalid_ids(10, 15) -> 11 (only 11 satisfies) -> returns 11
        sum_invalid_ids(998, 1012) -> 1001 (only 1001 satisfies) -> returns 1001, 999 is valid
    """
    sum = 0

    for i in range(min, max + 1):
        if is_digits_duplicate(i):
            sum += i
              
    return sum

def is_digits_duplicate(number):
    """
    Checks if a number has an even number of digits and the first half of the digits equals the second half.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the condition is met, False otherwise.
        
    Example:
        is_digits_duplicate(1212) -> True
        is_digits_duplicate(1234) -> False
        is_digits_duplicate(121) -> False (odd number of digits)
    """
    no_of_digits = len(str(number))

    if no_of_digits % 2 != 0:
        return False
    
    splitter = 10 ** (no_of_digits / 2)

    first_half = number // splitter
    second_half = number % splitter

    return first_half == second_half
    
if __name__ == "__main__":
    print("Solving problem1 ...")
    
    input_list = input.parse_input("day_2/input.txt")

    result = 0

    for input in input_list:
        result += sum_invalid_ids(input[0], input[1])
        
    print(result)
        
        

    