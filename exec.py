import ast
import json
from virtualMachine import *

#Reading of the function directory

file = open("obj.txt", "r")

contents = file.read()
FUNC_DIR = ast.literal_eval(contents)

file.close()

#reading the table of constants

file = open("constants.txt", "r")

contents = file.read()
CNT_TABLE_DIR = ast.literal_eval(contents)

file.close()
CNT_TABLE = CNT_TABLE_DIR['temporal']

file = open("quads.txt", "r")

contents = file.read()
QUADS_DIR = ast.literal_eval(contents)

file.close()
QUADS = QUADS_DIR['temporal']



program_name = next(iter(FUNC_DIR))
print(program_name)


# Creation of memory
virtual_machine = VirtualMachine()
virtual_machine.func_dir = FUNC_DIR


# assignation of global memory
vars = FUNC_DIR[program_name]['var_table'][2]


for var in vars:
    if (var >= 1000) and (var <= 2999):
        virtual_machine.global_memory.integers[0].append(var)
        virtual_machine.global_memory.integers[1].append(None)


    if (var >= 3000) and (var <= 5999):
        virtual_machine.global_memory.floats[0].append(var)
        virtual_machine.global_memory.floats[1].append(None)


    if (var >= 6000) and (var <= 9999):
        virtual_machine.global_memory.strings[0].append(var)
        virtual_machine.global_memory.strings[1].append(None)


temp = CNT_TABLE[0]
CNT_TABLE[0] = CNT_TABLE[1]
CNT_TABLE[1] = temp


virtual_machine.global_memory.name = "global"
virtual_machine.global_memory.print_memory()
virtual_machine.quads = QUADS
virtual_machine.print_quads()
virtual_machine.constants = CNT_TABLE
virtual_machine.print_constants()
print(virtual_machine.global_memory.integers)
print(FUNC_DIR)



virtual_machine.run()








#
