class FunctionDirectory(object):

    def __init__(self):
        self.functions = {}
        self.program_name = "program"


    def declare_function(self, id, type, scope):
        self.functions[id] = {"scope" : scope, "type" : type, "id" : id}
        self.functions[id]['var_table'] = [[],[],[]]
        self.functions[id]['paramorder'] = []


    def add_var_table(self, id, var_table):
        self.functions[id]["var_table"]



class VirtualMemory(object):

    def __init__(self):
        self.global_variables = [1000, 3000, 6000]
        self.local_variables = [10000, 13000, 16000]
        self.temporal_variables = [20000, 23000, 26000]
        self.constants = [30000, 33000, 36000]


    def reset(self):
        self.global_variables = [1000, 3000, 6000]
        self.local_variables = [10000, 13000, 16000]
        self.temporal_variables = [20000, 23000, 26000]


    def add(self, scope, type):
        if (scope == 'g_scope'):
            if (type == 'int'):
                virtual_address = self.global_variables[0]
                self.global_variables[0] += 1
                return virtual_address

            elif (type == 'float'):
                virtual_address = self.global_variables[1]
                self.global_variables[1] += 1
                return virtual_address

            else:
                virtual_address = self.global_variables[2]
                self.global_variables[2] += 1
                return virtual_address

        if (scope == 'l_scope'):
            if (type == 'int'):
                virtual_address = self.local_variables[0]
                self.local_variables[0] += 1
                return virtual_address

            elif (type == 'float'):
                virtual_address = self.local_variables[1]
                self.local_variables[1] += 1
                return virtual_address

            else:
                virtual_address = self.local_variables[2]
                self.local_variables[2] += 1
                return virtual_address


        if (scope == 't_scope'):
            if (type == 'int'):
                virtual_address = self.temporal_variables[0]
                self.temporal_variables[0] += 1
                return virtual_address

            elif (type == 'float'):
                virtual_address = self.temporal_variables[1]
                self.temporal_variables[1] += 1
                return virtual_address

            else:
                virtual_address = self.temporal_variables[2]
                self.temporal_variables[2] += 1
                return virtual_address

        if (scope == 'c_scope'):
            if (type == 'int'):
                virtual_address = self.constants[0]
                self.constants[0] += 1
                return virtual_address

            elif (type == 'float'):
                virtual_address = self.constants[1]
                self.constants[1] += 1
                return virtual_address

            else:
                virtual_address = self.constants[2]
                self.constants[2] += 1
                return virtual_address
