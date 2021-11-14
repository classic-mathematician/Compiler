import ast
import json

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

cnt = 1

for quad in QUADS:
    print(cnt, quad)
    cnt += 1
