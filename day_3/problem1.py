import input_module

def find_top_2_elements(input_list):
    (first, second) = (input_list[0], input_list[1])

    for i in range(2, len(input_list)):
        if is_ordering_invalid(first, second):
            first = second
            second = input_list[i]
        elif input_list[i] > second:
            if second > first:
                first = second
            second = input_list[i]
        elif input_list[i] > first:
            first = second
            second = input_list[i]

    return (first, second)

def is_ordering_invalid(first, second):
    return first < second

if __name__ == "__main__":
    print("Solving problem1...")

    input_list = input_module.parse_input("day_3/input.txt")

    # input_list = [[8, 2, 8, 1, 9, 3, 2, 2]]
    # input_list = [[1,2,3,4,5,6,7,8]]

    # input_list = [[9,8,7,6,5,4,3,2,1]]

    # input_list = [[1,2,5,1,1]]

    total_joltage = 0
    for bank in input_list:
        (first, second) = find_top_2_elements(bank)
        joltage = first * 10 + second
        total_joltage += joltage
    
    print(total_joltage)
    