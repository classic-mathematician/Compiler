
#  a = f; -> = a f


# objeto Quad Motor, posee lista de cuádruplos, pila popper, pila de operandos, pila de tipos, pila de saltos, pila de dimensiones y el contador de los cuádruplos

class QuadMotor(object):
    def __init__(self):
        self.QUADS = []
        self.poper = []
        self.operand_stack = []
        self.types_stack = []
        self.jumps_stack = []
        self.dim_stack = []
        self.quad_counter = 1



    #función para generar cuádruplos que agrega el cuádruplo generado y suma uno al contador
    def generate_quad(self, operator, left_operand, right_operand, result):
        quad = [operator, left_operand, right_operand, result]
        self.QUADS.append(quad)
        self.quad_counter += 1


    #función para imprimir todos los cuádruplos numerados
    def print_quads(self):
        for (i, item) in enumerate(self.QUADS, start=1):
            print(i, item)
