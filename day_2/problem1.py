import input

def find_invalid_ids(min, max):
    print(min, max)
    # todo: Add logic
    return 0

if __name__ == "__main__":
    print("Solving problem1 ...")
    
    input_list = input.parse_input("day_2/input.txt")
    
    result = 0
    
    for input in input_list:
        result += find_invalid_ids(input[0], input[1])
        
    print(result)
        
        

    