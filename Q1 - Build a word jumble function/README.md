Create the funstion that expects a string and an interger n is between 1 and 1000 
It will transform each character of the input string using the following instructions:

# if it is a letter of the alphabet (a,b,c ... z) shift it to the right in the alphabet by n letters, if you reach z return to a and continue, however many times is required

# if it is a number (1,2,3 ... ) or a space leave it the same

# if it is any other character remove it from the string

_______________________________________________________________________________________________________________________________________________

HOW To :

# Repeat over each character in the input string 
    for char in input_string:
# Use isalpha () method to check if all the character in a string are alphabetic characters
        if char.isalpha():
# Convert the character to its corresponding ASCII value and store it in the variable char_code
            char_code = ord(char.lower())
            
# Shift the character to the right by n positions
            shifted_code = (char_code - 97 + n) % 26 + 97
            
# Append the transformed character to the result string
            transformed_string += chr(shifted_code)

# Check if the character is a number or a space
        elif char.isdigit() or char.isspace():
            transformed_string += char
    
# Return transformed_string

# Run the code 
    There are several ways to run Python code in VSCode:

    -Press F5 to run the code in the integrated terminal.
    -Right-click in the editor and select "Run Python File in Terminal."
    -Use the VSCode command palette (Ctrl + Shift + P) and type "Python: Run Python File in Terminal."
    -Use the VSCode menu: Run -> Run Without Debugging or Run -> Run Python File in Terminal.
    -The output of your Python program will be displayed in the integrated terminal.

