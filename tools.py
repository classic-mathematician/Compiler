class FunctionDirectory(object):

    def __init__(self):
        self.functions = {}


    def declare_function(self, id, type, scope):
        self.functions[id] = {"scope" : scope, "type" : type, "id" : id}
        self.functions[id]['var_table'] = [[],[]]


    def add_var_table(self, id, var_table):
        self.functions[id]["var_table"]
