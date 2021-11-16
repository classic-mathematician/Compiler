class VirtualMachine(object):
    def __init__(self):
        self.IP = 1
        self.quads = []
        self.constants = []
        self.global_memory = Memory()
        self.local_memory = []
        self.temporal_memory = [Memory()]


    def print_quads(self):
        cnt = 1

        for quad in self.quads:
            print(cnt, quad)
            cnt += 1


    def print_constants(self):
        print(self.constants)


    def act(self):
        quad = self.quads[self.IP]
        action = quad[0]

        if action == 'ERA':
            self.local_memory.append(Memory())
            self.temporal_memory.append(Memory())

        if action == 'ENDFunc':
            self.local_memory.pop()
            self.temporal_memory.pop()


        if action == '=':
            left_operand = int(quad[1])
            right_operand = int(quad[3])
            #                        place to assign        thing to assign
            allocate_in_memory(self, right_operand, find_in_memory(self, left_operand))



        if action == '+':
            pass




    def find_in_memory(self, virtual_address):
        #global integers
        if (virtual_address >= 1000) and (virtual_address <= 2999):
            index = self.global_memory.integers[0].index(virtual_address)
            return self.global_memory.integers[1][index]
        #global floats
        if (virtual_address >= 3000) and (virtual_address <= 5999):
            index = self.global_memory.floats[0].index(virtual_address)
            return self.global_memory.floats[1][index]
        #global strings
        if (virtual_address >= 6000) and (virtual_address <= 9999):
            index = self.global_memory.strings[0].index(virtual_address)
            return self.global_memory.strings[1][index]
        # local integers
        if (virtual_address >= 10000) and (virtual_address <= 12999):
            index = self.local_memory[-1].integers[0].index(virtual_address)
            return self.local_memory[-1].integers[1][index]
        # local floats
        if (virtual_address >= 13000) and (virtual_address <= 15999):
            index = self.local_memory[-1].floats[0].index(virtual_address)
            return self.local_memory[-1].floats[1][index]
        # local stringse
        if (virtual_address >= 16000) and (virtual_address <= 19999):
            index = self.local_memory[-1].strings[0].index(virtual_address)
            return self.local_memory[-1].strings[1][index]
        # temporal integers
        if (virtual_address >= 20000) and (virtual_address <= 22999):
            index = self.temporal_memory[-1].integers[0].index(virtual_address)
            return self.temporal_memory[-1].integers[1][index]
        # temporal floats
        if (virtual_address >= 23000) and (virtual_address <= 25999):
            index = self.temporal_memory[-1].floats[0].index(virtual_address)
            return self.temporal_memory[-1].floats[1][index]
        # temporal strings
        if (virtual_address >= 26000) and (virtual_address <= 29999):
            index = self.temporal_memory[-1].strings[0].index(virtual_address)
            return self.temporal_memory[-1].strings[1][index]
        # constants
        if (virtual_address >= 30000) and (virtual_address <= 32999):
            index = self.constants[0].index(virtual_address)
            return self.constants[1][index]

    def allocate_in_memory(self, virtual_address, item):
        #global integers
        if (virtual_address >= 1000) and (virtual_address <= 2999):
            index = self.global_memory.integers[0].index(virtual_address)
            self.global_memory.integers[1][index] = item
        #global floats
        if (virtual_address >= 3000) and (virtual_address <= 5999):
            index = self.global_memory.floats[0].index(virtual_address)
            self.global_memory.floats[1][index] = item
        #global strings
        if (virtual_address >= 6000) and (virtual_address <= 9999):
            index = self.global_memory.strings[0].index(virtual_address)
            self.global_memory.strings[1][index] = item
        # local integers
        if (virtual_address >= 10000) and (virtual_address <= 12999):
            index = self.local_memory[-1].integers[0].index(virtual_address)
            self.local_memory[-1].integers[1][index] = item
        # local floats
        if (virtual_address >= 13000) and (virtual_address <= 15999):
            index = self.local_memory[-1].floats[0].index(virtual_address)
            self.local_memory[-1].floats[1][index] = item
        # local stringse
        if (virtual_address >= 16000) and (virtual_address <= 19999):
            index = self.local_memory[-1].strings[0].index(virtual_address)
            self.local_memory[-1].strings[1][index] = item
        # temporal integers
        if (virtual_address >= 20000) and (virtual_address <= 22999):
            index = self.temporal_memory[-1].integers[0].index(virtual_address)
            self.temporal_memory[-1].integers[1][index] = item
        # temporal floats
        if (virtual_address >= 23000) and (virtual_address <= 25999):
            index = self.temporal_memory[-1].floats[0].index(virtual_address)
            self.temporal_memory[-1].floats[1][index] = item
        # temporal strings
        if (virtual_address >= 26000) and (virtual_address <= 29999):
            index = self.temporal_memory[-1].strings[0].index(virtual_address)
            self.temporal_memory[-1].strings[1][index] = item
        # constants
        if (virtual_address >= 30000) and (virtual_address <= 32999):
            index = self.constants[0].index(virtual_address)
            self.constants[1][index] = item



class Memory(object):
    def __init__(self):
        self.integers = [[],[]]
        self.floats = [[],[]]
        self.strings = [[],[]]
        self.name = "unnamed"


    def print_memory(self):
        print("Memory Map", self.name)
        print("Integer memory: ", self.integers)
        print("Float memory: ", self.floats)
        print("String memory: ", self.strings)
