def parse_input(file_name):
    input_list = []
    with open(file_name, "r") as file:
        for line in file:
            input = line.strip()
            
            input_list.append(input)
    
    return input_list

if __name__ == "__main__":
    print("Parsing input...")
    
    result = parse_input("input.txt")