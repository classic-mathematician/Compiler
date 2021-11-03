semantic_cube = {}


semantic_cube["int"] = {
    #operators
    "+" :  {"int" : "int", "float" : "float", "string" : "e"},
    "-" :  {"int" : "int", "float" : "float", "string" : "e"},
    "*" :  {"int" : "int", "float" : "float", "string" : "e"},
    "/" :  {"int" : "int", "float" : "float", "string" : "e"},


    #assignator
    "=" :  {"int" : "int", "float" : "e", "string" : "e"},


    #comparators
    "==" :  {"int" : "int", "float" : "e", "string" : "e"} ,
    ">" :  {"int" : "int", "float" : "int", "string" : "e"},
    "<" :  {"int" : "int", "float" : "int", "string" : "e"},
    ">=" :  {"int" : "int", "float" : "int", "string" : "e"},
    "<=" :  {"int" : "int", "float" : "int", "string" : "e"},
    "&&" :  {"int" : "int", "float" : "int", "string" : "e"},
    "|" :  {"int" : "int", "float" : "int", "string" : "e"},
}

semantic_cube["float"] = {
    #operators
    #string is not supported
    "+" : {"int" : "float", "float" : "float", "string" : "e"},
    "-" : {"int" : "float", "float" : "float", "string" : "e"},
    "*" : {"int" : "float", "float" : "float", "string" : "e"},
    "/" : {"int" : "float", "float" : "float", "string" : "e"},


    #assignator
    "=" :  {"int" : "float", "float" : "float", "string" : "e"} ,


    #comparators
    "==" : {"int" : "e", "float" : "int", "string" : "e"},
    ">" : {"int" : "int", "float" : "int", "string" : "e"},
    "<" : {"int" : "int", "float" : "int", "string" : "e"},
    ">=" : {"int" : "int", "float" : "int", "string" : "e"},
    "<=" : {"int" : "int", "float" : "int", "string" : "e"},
    "&&" : {"int" : "int", "float" : "int", "string" : "e"} ,
    "|" : {"int" : "int", "float" : "int", "string" : "e"} ,
}


semantic_cube["string"] = {


    #assignator
    "=" :  {"int" : "e", "float" : "e", "string" : "string"} ,

    #comparators
    "==" : {"int" : "e", "float" : "e", "string" : "int"},
    ">" : {"int" : "e", "float" : "e", "string" : "int"},
    "<" : {"int" : "e", "float" : "e", "string" : "int"},
    ">=" : {"int" : "e", "float" : "e", "string" : "int"},
    "<=" : {"int" : "e", "float" : "e", "string" : "int"},
    "&&": {"int" : "int", "float" : "e", "string" : "int"},
    "|" : {"int" : "int", "float" : "e", "string" : "int"},
}
