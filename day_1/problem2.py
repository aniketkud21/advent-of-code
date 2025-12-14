import input, utils
    
if __name__ == "__main__":
    input = input.parse_input("day_1/input.txt")
    
    # defined in problem
    current_pos = 50
    count = 0
    
    for rotation in input:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        # Only this doesnt work because, lets say
        # current_pos = 50, rotation L60 -> new_pos = 90 
        # ans = 1, but from the solution it would be 0
        # no_of_full_rotations = floor(distance / 100)
        
        no_of_full_rotations = utils.calculate_full_rotations(current_pos, direction, distance)
        
        count += no_of_full_rotations
        
        current_pos = utils.rotate(current_pos, direction, distance)
            
    print(count)
