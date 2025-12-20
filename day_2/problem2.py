import input

def sum_invalid_ids(min, max):
    """
    Calculates the sum of all integers in the range [min, max] that exhibit a repeating digit pattern.

    A number is considered to have a repeating pattern if it can be partitioned into 
    two or more identical integer segments (e.g., 1212 is a repetition of '12').

    Args:
        min (int): The starting value of the range (inclusive).
        max (int): The ending value of the range (inclusive).

    Returns:
        int: The sum of all numbers within the range that satisfy the repeating pattern criteria.
    """

    sum = 0

    for i in range(min, max + 1):
        no_of_digits = len(str(i)) 

        partitions = get_possible_partitions(no_of_digits)

        for partition in partitions:
            numbers = split_number(i, partition)

            if is_sequence_repeating(numbers):
                print(i)
                sum += i
                break
            
    return sum

def get_possible_partitions(no_of_digits):
    """
    Identifies all possible segment lengths that can evenly divide a number of a given length.

    This function finds all divisors of the total number of digits, which represent the 
    possible sizes for repeating blocks.

    Args:
        no_of_digits (int): The total number of digits in the integer being analyzed.

    Returns:
        list[int]: A list of integers representing the valid lengths for partitioning.
    """

    partitions = []

    for i in range(1, no_of_digits + 1):
        if no_of_digits % i == 0:
            partitions.append(i)

    return partitions

def split_number(number, parts):
    """
    Recursively partitions an integer into a specific number of equal-length segments.

    Args:
        number (int): The integer to be split.
        parts (int): The number of segments to divide the integer into.

    Returns:
        list[int]: A list of integers representing the segments. Returns an empty 
            list if the number of digits cannot be evenly divided by 'parts'.

    Example:
        split_number(1212, 2) -> [12, 12]
    """

    no_of_digits = len(str(number))

    if no_of_digits < parts or no_of_digits % parts != 0:
        # Cant partition
        return []

    if parts == 1:
        return [number]

    splitter = 10 ** (no_of_digits // parts)

    if parts > 2:
        first_half = split_number(number // splitter, parts - 1)
    else:
        first_half = [number // splitter]

    second_half = [number % splitter]

    return first_half + second_half

def is_sequence_repeating(numbers):
    """
    Validates if a list of numbers consists of at least two identical elements.

    The sequence is considered repeating only if all elements in the list are 
    exactly the same and there is more than one element present.

    Args:
        numbers (list[int]): A list of integer segments to check for uniformity.

    Returns:
        bool: True if the sequence is repeating, False otherwise.

    Example:
        is_sequence_repeating([1, 2, 3, 4]) -> False
        is_sequence_repeating([2, 2, 2, 2]) -> True
        is_sequence_repeating([2, 2, 2, 1]) -> False

        is_sequence_repeating([12, 12, 12]) -> True

        is_sequence_repeating([121, 121]) -> True

        is_sequence_repeating([121]) -> False
        is_sequence_repeating([]) -> False
    """

    if len(numbers) == 1 or len(numbers) == 0:
        return False
    
    hashset = set(numbers)
    return len(hashset) == 1

if __name__ == "__main__":
    print("Solving problem2 ...")

    # print(split_number(5, 5))

    # print(get_possible_partitions(9))
    
    input_list = input.parse_input("day_2/input.txt")

    # input_list = [(11, 22), (95, 115), (998, 1012), (1188511880, 1188511890), (222220, 222224), (1698522, 1698528), (446443, 446449), (38593856, 38593862), (565653, 565659), (824824821, 824824827), (2121212118, 2121212124)]

    #input_list = [(95, 115)]

    result = 0

    for input in input_list:
        result += sum_invalid_ids(input[0], input[1])
        
    print(result)