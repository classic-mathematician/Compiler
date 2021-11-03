class FunctionDirectory(object):

    def __init__(self):
        self.functions = {}


    def declare_function(self, id, type, scope):
        self.functions[id] = {"scope" : scope, "type" : type, "id" : id}
        self.functions[id]['var_table'] = [[],[],[]]
        self.functions[id]['paramorder'] = []



    def add_var_table(self, id, var_table):
        self.functions[id]["var_table"]



class VirtualMemory(object):

    def __init__(self):
        self.global_variables = [[1000], [3000], [6000]]
        self.local_variables = [[10000], [13000], [16000]]
        self.temporal_variables = [[20000], [23000], [26000]]
        self.constants = 30000


    
