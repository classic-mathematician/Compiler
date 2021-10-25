class FunctionDirectory(object):

    def __init__(self):
        self.program_name = None
        self.functions = {"program" : {}}


    def declare_function(self, func_name, scope, vars, param_seq, address_s, size):
        self.functions[func_name] = {"scope" : scope, "vars" : vars, "param_seq" : param_seq, "address_s" : address_s, "size", size}
