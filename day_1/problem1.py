import input, utils
    
def logic(start_pos, count, input):
    """
    Recursive solution to compute the password.

    Note:
        For this solution need to increase recursion limit
        
        Default recursion limit is 1000
        sys.getrecursionlimit()
        1000
    """
    if len(input) == 0:
        return count
    
    rotation = input[0]
    new_pos = rotate(start_pos, rotation)
    
    if new_pos == 0:
        count = count + 1
    
    return logic(new_pos, count, input[1:])
    
if __name__ == "__main__":
    # todo: Make this dynamic based on from where i am executing the program
    input = input.parse_input("day_1/input.txt")
    
    # defined in problem
    current_pos = 50
    count = 0
    
    for rotation in input:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        current_pos = utils.rotate(current_pos, direction, distance)
        
        if current_pos == 0:
            count += 1
            
    print(count)