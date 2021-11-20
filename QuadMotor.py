
#  a = f; -> = a f

class QuadMotor(object):
    def __init__(self):
        self.QUADS = []
        self.poper = []
        self.operand_stack = []
        self.types_stack = []
        self.jumps_stack = []
        self.dim_stack = []
        self.quad_counter = 1


    def generate_quad(self, operator, left_operand, right_operand, result):
        quad = [operator, left_operand, right_operand, result]
        self.QUADS.append(quad)
        self.quad_counter += 1


    def print_quads(self):
        for (i, item) in enumerate(self.QUADS, start=1):
            print(i, item)
