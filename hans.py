import math
code = """
AAAMMMMMAAAAAAAAAAAAXPAAAPGP prints lol
""" # example code

value = 0 # the value itself
storage = [] # the value storage
lexed = []
for char in code:
    lexed.append(char) # the lexer
    
for instr in lexed:
    if instr == "A":
        value = (value + 1) % 256 # 1+
    elif instr == "S":
        value = (value - 1) % 256 #-1
    elif instr == "P":
        print(chr(value), end="") # prints the corresponding ASCII character
    elif instr == "N":
        print("")  # prints a line break
    elif instr == "R":
        value = 0 # resets the value
    elif instr == "I":
        value = ord(input("> ")[0]) # accepts input from the user
    elif instr == "D":
        print(value) # prints the value
    elif instr == "O":
        print(storage) # prints the storage
    elif instr == "M":
        value = (value * 2) % 256 # multiplies the value
    elif instr == "H":
        value = (value / 2) % 256 # halves the value
        value = math.ceil(value) # rounds it
    elif instr == "X":
        storage.append(value) # stores the value
    elif instr == "G":
        if storage:
            value = storage.pop() # takes a value from storage
    elif instr == "C":
        storage.clear() # clears the storage
        # i never actually used this one