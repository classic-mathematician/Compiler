class FunctionDirectory(object):

    def __init__(self):
        self.functions = {}
        self.program_name = "program"


    def declare_function(self, id, type, scope):
        self.functions[id] = {"scope" : scope, "type" : type, "id" : id}
        self.functions[id]['var_table'] = [[],[],[],{}, {}]
        self.functions[id]['paramorder'] = []


    def add_var_table(self, id, var_table):
        self.functions[id]["var_table"]

#virtual memory map

# global variables 1000-9999
    # 1000-2999 int
    # 3000- 5999 float
    # 6000 - 9999 strings
# local variables 10,000 - 19,9999
    # 10,000 - 12,999 int
    # 13,000 - 15,999 float
    # 16,000 - 19,999 string
# temporal variables 20,000 - 29,999
    # 20,000 - 22,999 int
    # 23,000 - 25999 float
    # 26,000 - 29999 stringe
# constantes 30,000 - 34,999
    # 30,000 - 32,999 int
    # 33,000 - 35999 float
    # 36,000 - 39999 stringe




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



    def add_arr(self, scope, type, size):
        if (scope == 'g_scope'):
            if (type == 'int'):
                virtual_address = self.global_variables[0]
                self.global_variables[0] += size
                return virtual_address

            elif (type == 'float'):
                virtual_address = self.global_variables[1]
                self.global_variables[1] += size
                return virtual_address

            else:
                virtual_address = self.global_variables[2]
                self.global_variables[2] += size
                return virtual_address

        if (scope == 'l_scope'):
            if (type == 'int'):
                virtual_address = self.local_variables[0]
                self.local_variables[0] += size
                return virtual_address

            elif (type == 'float'):
                virtual_address = self.local_variables[1]
                self.local_variables[1] += size
                return virtual_address

            else:
                virtual_address = self.local_variables[2]
                self.local_variables[2] += size
                return virtual_address


        if (scope == 't_scope'):
            if (type == 'int'):
                virtual_address = self.temporal_variables[0]
                self.temporal_variables[0] += size
                return virtual_address

            elif (type == 'float'):
                virtual_address = self.temporal_variables[1]
                self.temporal_variables[1] += size
                return virtual_address

            else:
                virtual_address = self.temporal_variables[2]
                self.temporal_variables[2] += size
                return virtual_address








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
