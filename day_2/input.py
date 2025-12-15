def parse_input(file_name):
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