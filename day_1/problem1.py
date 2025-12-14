import input
import sys

def rotate(current_pos, rotation):
    direction = rotation[0]
    distance = int(rotation[1:])
    
    if direction == "L":
        return (current_pos + 100 - distance) % 100
    else:
        return (current_pos + distance) % 100  
    
def logic(start_pos, count, input):
    if len(input) == 0:
        return count
    
    rotation = input[0]
    new_pos = rotate(start_pos, rotation)
    
    if new_pos == 0:
        count = count + 1
    
    return logic(new_pos, count, input[1:])
    
if __name__ == "__main__":
    input = input.parse_input("input.txt")
    
    # defined in problem
    current_pos = 50
    count = 0
    
    for rotation in input:
        current_pos = rotate(current_pos, rotation)
        
        if current_pos == 0:
            count += 1
            
    print(count)

    # print(logic(start_pos, count, input))
    
    
    
    
    
