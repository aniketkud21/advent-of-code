import input
from math import floor

def rotate(current_pos, direction, distance):    
    """
    Computes new position of dial based on the direction of rotation and distance to be rotated.

    The dial is assumed to have 100 positions (0 to 99). The movement wraps around.

    Args:
        current_pos (int): The current position of the dial (0-99).
        direction (str): The direction of rotation, "L" for left (counter-clockwise) 
                         or "R" for right (clockwise).
        distance (int): The distance (number of positions) to rotate the dial.

    Returns:
        int: The new position of the dial after the rotation (0-99).

    Examples:
        # --- Right (Clockwise) Rotation Examples ---
        # Basic movement: 10 + 20 = 30
        >>> rotate(10, "R", 20)
        30
        
        # Wrapping around (10 + 95 = 105; 105 % 100 = 5)
        >>> rotate(10, "R", 95)
        5
        
        # Moving exactly a full circle (10 + 100 = 110; 110 % 100 = 10)
        >>> rotate(10, "R", 100)
        10

        # --- Left (Counter-Clockwise) Rotation Examples ---
        # Basic movement: 30 - 10 = 20
        # Formula: (30 + 100 - 10) % 100 = 120 % 100 = 20
        >>> rotate(30, "L", 10)
        20
        
        # Wrapping around (5 - 10 = -5; Formula: (5 + 100 - 10) % 100 = 95 % 100 = 95)
        >>> rotate(5, "L", 10)
        95
        
        # Starting from 0 and moving left (0 - 1 = -1; Formula: (0 + 100 - 1) % 100 = 99)
        >>> rotate(0, "L", 1)
        99
    """
    
    if direction == "L":
        return (current_pos + 100 - distance) % 100
    else:
        return (current_pos + distance) % 100 
    
def calculate_full_rotations(start_pos, direction, distance):
    """
    Calculates the number of times the dial position wraps around its cycle 
    (from 99 to 0, or 0 to 99) during a rotation.

    The dial is assumed to have 100 positions (0 to 99). This function 
    determines the number of full 100-position intervals crossed.

    Args:
        start_pos (int): The starting position of the dial (0-99).
        direction (str): The direction of rotation, "L" for left (counter-clockwise) 
                         or "R" for right (clockwise).
        distance (int): The distance (number of positions) to rotate the dial.

    Returns:
        int: The number of full 100-position cycles completed during the rotation.

    Examples:
        # --- Right (Clockwise) Rotation Examples (Wraps from 99 to 0) ---
        
        # Start at 10, move 80. Total distance 90. No wrap.
        >>> calculate_full_rotations(10, "R", 80)
        0
        
        # Start at 10, move 90. One full wrap (10 -> 99 -> 0 -> 10).
        >>> calculate_full_rotations(10, "R", 90)
        1
        
        # Start at 50, move 250. Two full wraps (crosses the 0 mark three times, 
        # but two full rotations are completed).
        >>> calculate_full_rotations(50, "R", 250)
        3 

        # --- Left (Counter-Clockwise) Rotation Examples (Wraps from 0 to 99) ---
        
        # Start at 80, move 20. Total distance 80 -> 60. No wrap.
        >>> calculate_full_rotations(80, "L", 20)
        0
        
        # Start at 80, move 100. One full wrap.
        >>> calculate_full_rotations(80, "L", 100)
        1
        
        # Start at 5, move 15. Wraps once (5 -> 0 -> 99 -> 90).
        >>> calculate_full_rotations(5, "L", 15)
        1

        # Edge case: Start at 0, move 1 (0 -> 99). Should be 0 wraps.
        >>> calculate_full_rotations(0, "L", 1)
        0
        
        # Edge case: Start at 0, move 100. One full wrap.
        >>> calculate_full_rotations(0, "L", 100)
        1
    """
    
    if direction == "L":
        result = floor((distance - start_pos + 100) / 100)
        if start_pos == 0:
            return result - 1
        
        return result
    else:
        return floor((start_pos + distance) / 100)
    
if __name__ == "__main__":
    print(calculate_full_rotations(50, "R", 1000))
    print(calculate_full_rotations(0, "L", 5))