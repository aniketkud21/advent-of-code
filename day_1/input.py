def parse_input(file_name):
    """
    Reads a text file line by line and returns the stripped content 
    as a list of strings.

    Args:
        file_name (str): The name or path of the file to be read.
                         E.g., "data/input.txt"

    Returns:
        list[str]: A list where each element is a stripped line from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Examples:
        Assuming a file named 'moves.txt' exists with the following content:
        
        R29
        R41
          L8
        
        >>> parse_input('moves.txt')
        ['R29', 'R41', 'L8']
        
        Assuming a file named 'empty.txt' exists with only blank lines:
        
        >>> parse_input('empty.txt')
        []
    """
    
    input_list = []
    with open(file_name, "r") as file:
        for line in file:
            input = line.strip()
            
            input_list.append(input)
    
    return input_list

if __name__ == "__main__":
    print("Parsing input...")
    
    result = parse_input("input.txt")