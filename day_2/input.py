def parse_input(file_name):
    """
    Parses the input file containing comma-separated ranges.

    Args:
        file_name (str): The path to the input file.

    Returns:
        list: A list of tuples where each tuple contains two integers (min, max) representing a range.

    Example:
        If the file content is "1-5,8-10", the function returns:
        [(1, 5), (8, 10)]
    """
    with open(file_name, "r") as file:    
        input_string = file.read()
        
        range_list = input_string.split(",")
        
        input_list = []
        
        for range in range_list:
            min, max = range.split("-")
            
            input_list.append((int(min), int(max)))
            
        return input_list
            

if __name__ == "__main__":
    print("Parsing input...")
    # result = parse_input("day_2/input.txt")
    # print(result)