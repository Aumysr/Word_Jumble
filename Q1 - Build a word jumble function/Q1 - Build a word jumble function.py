def transform_string(input_string, n):
    transformed_string = ""
    
   
    for char in input_string:
        if char.isalpha():
            char_code = ord(char.lower())
            
            shifted_code = (char_code - 97 + n) % 26 + 97
            
            transformed_string += chr(shifted_code)
        
        elif char.isdigit() or char.isspace():
            transformed_string += char
    
    return transformed_string

input_string = "'test 123!', 0"
n = 3

result = transform_string(input_string, n)
print(result)

