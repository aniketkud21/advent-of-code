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

        range_list = input_string.split("\n")

        result = [[int(char) for char in item] for item in range_list]

        return result
            

if __name__ == "__main__":
    print("Parsing input...")
    result = parse_input("day_3/input.txt")
    print(result)