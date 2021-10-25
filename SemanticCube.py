semantic_cube = {}


semantic_cube["int"] = {
    #operators
    "+" :  {"int" : "int", "float" : "float", "string" : "err"},
    "-" :  {"int" : "int", "float" : "float", "string" : "err"},
    "*" :  {"int" : "int", "float" : "float", "string" : "err"},
    "/" :  {"int" : "int", "float" : "float", "string" : "err"},


    #assignator
    "=" :  {"int" : "int", "float" : "e", "string" : "e"},


    #comparators
    "==" :  {"int" : "int", "float" : "e", "string" : "err"} ,
    ">" :  {"int" : "int", "float" : "int", "string" : "err"},
    "<" :  {"int" : "int", "float" : "int", "string" : "err"},
    ">=" :  {"int" : "int", "float" : "int", "string" : "err"},
    "<=" :  {"int" : "int", "float" : "int", "string" : "err"},
    "&&" :  {"int" : "int", "float" : "int", "string" : "err"},
    "|" :  {"int" : "int", "float" : "int", "string" : "err"},
}

Semantic_cube["float"] = {
    #operators
    #string is not supported
    "+" : {"int" : "float", "float" : "float", "string" : "err"},
    "-" : {"int" : "float", "float" : "float", "string" : "err"},
    "*" : {"int" : "float", "float" : "float", "string" : "err"},
    "/" : {"int" : "float", "float" : "float", "string" : "err"},


    #assignator
    "=" :  {"int" : "float", "float" : "float", "string" : "err"} ,


    #comparators
    "==" : {"int" : "err", "float" : "int", "string" : "err"},
    ">" : {"int" : "int", "float" : "int", "string" : "err"},
    "<" : {"int" : "int", "float" : "int", "string" : "err"},
    ">=" : {"int" : "int", "float" : "int", "string" : "err"},
    "<=" : {"int" : "int", "float" : "int", "string" : "err"},
    "&&" : {"int" : "int", "float" : "int", "string" : "err"} ,
    "|" : {"int" : "int", "float" : "int", "string" : "err"} ,
}


Semantic_cube["string"] = {


    #assignator
    "=" :  {"int" : "err", "float" : "err", "string" : "string"} ,

    #comparators
    "==" : {"int" : "err", "float" : "err", "string" : "int"},
    ">" : {"int" : "err", "float" : "err", "string" : "int"},
    "<" : {"int" : "err", "float" : "err", "string" : "int"},
    ">=" : {"int" : "err", "float" : "err", "string" : "int"},
    "<=" : {"int" : "err", "float" : "err", "string" : "int"},
    "&&": {"int" : "int", "float" : "err", "string" : "int"},
    "|" : {"int" : "int", "float" : "err", "string" : "int"},
}
