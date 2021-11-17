class VirtualMachine(object):
    def __init__(self):
        self.IP = 1
        self.quads = []
        self.constants = []
        self.global_memory = Memory()
        self.local_memory = []
        self.temporal_memory = [Memory()]
        self.func_dir = None
        self.func_stack = []


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
            func_name = quad[2]
            self.func_stack.append(func_name)
            self.local_memory.append(Memory())
            self.temporal_memory.append(Memory())

            for address in self.func_dir[func_name]['var_table'][2]:
                register(self, address)

            self.IP += 1

        elif action == 'ENDFunc':
            self.local_memory.pop()
            self.temporal_memory.pop()
            self.func_stack.pop()
            self.IP += 1

        elif action == 'GOSUB':
            self.IP = int(quad[2])


        elif action == 'PARAMETER':
            thing_to_store = find_in_memory(self, int(quad[1]))
            index_to_store = int(quad[2])

            allocate_in_memory(self, self.func_dir[self.func_stack[-1]]['var_table'][2][index_to_store], thing_to_store)


        elif action == 'GOTO':
            self.IP = int(quad[3])


        elif action == 'GOTOF':
            cond = find_in_memory(self, int(quad[1]))

            if (cond > 0):
                self.IP += 1
            else:
                self.IP = int(quad[3])


        elif action == '=':
            left_operand = int(quad[1])
            right_operand = int(quad[3])

            register(self, left_operand)
            register(self, right_operand)

            #                        place to assign        thing to assign
            allocate_in_memory(self, right_operand, find_in_memory(self, left_operand))


        elif action == '+':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)

            result = find_in_memory(self, first_operand) + find_in_memory(self, second_operand)
            allocate_in_memory(self, third_operand, result)


        elif action == '-':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)

            result = find_in_memory(self, first_operand) - find_in_memory(self, second_operand)
            allocate_in_memory(self, third_operand, result)


        elif action == '*':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)

            result = find_in_memory(self, first_operand) * find_in_memory(self, second_operand)
            allocate_in_memory(self, third_operand, result)


        elif action == '/':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)

            result = find_in_memory(self, first_operand) / find_in_memory(self, second_operand)
            allocate_in_memory(self, third_operand, result)


        elif action == '>':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)




            result = find_in_memory(self, first_operand) > find_in_memory(self, second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            allocate_in_memory(self, third_operand, result)



        elif action == '<':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)




            result = find_in_memory(self, first_operand) < find_in_memory(self, second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            allocate_in_memory(self, third_operand, result)



        elif action == '>=':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)




            result = find_in_memory(self, first_operand) >= find_in_memory(self, second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            allocate_in_memory(self, third_operand, result)



        elif action == '<=':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)




            result = find_in_memory(self, first_operand) <= find_in_memory(self, second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            allocate_in_memory(self, third_operand, result)



        elif action == '==':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            register(self, first_operand)
            register(self, second_operand)
            register(self, third_operand)




            result = find_in_memory(self, first_operand) == find_in_memory(self, second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            allocate_in_memory(self, third_operand, result)




    def register(self, virtual_address):
        # local integers
        if (virtual_address >= 10000) and (virtual_address <= 12999):

            #if not found, register it
            if virtual_address not in self.local_memory[-1].integers[0]:
                self.local_memory[-1].integers[0].append(virtual_address)
                self.local_memory[-1].integers[1].append(None)

        # local floats
        elif (virtual_address >= 13000) and (virtual_address <= 15999):
            if virtual_address not in self.local_memory[-1].floats[0]:


                #if not found, register it
                self.local_memory[-1].floats[0].append(virtual_address)
                self.local_memory[-1].floats[1].append(None)

        # local strings
        elif (virtual_address >= 16000) and (virtual_address <= 19999):
            if virtual_address not in self.local_memory[-1].strings[0]:


                #if not found, register it
                self.local_memory[-1].strings[0].append(virtual_address)
                self.local_memory[-1].strings[1].append(None)

        # temporal integers
        elif (virtual_address >= 20000) and (virtual_address <= 22999):
            if virtual_address not in self.temporal_memory[-1].integers[0]:


                #if not found, register it
                self.temporal_memory[-1].integers[0].append(virtual_address)
                self.temporal_memory[-1].integers[1].append(None)

        # temporal floats
        elif (virtual_address >= 23000) and (virtual_address <= 25999):
            if virtual_address not in self.temporal_memory[-1].floats[0]:


                #if not found, register it
                self.temporal_memory[-1].floats[0].append(virtual_address)
                self.temporal_memory[-1].floats[1].append(None)
        # temporal strings
        elif (virtual_address >= 26000) and (virtual_address <= 29999):
            if virtual_address not in self.temporal_memory[-1].strings[0]:

                #if not found, register it
                self.temporal_memory[-1].strings[0].append(virtual_address)
                self.temporal_memory[-1].strings[1].append(None)




    def find_in_memory(self, virtual_address):

        #global integers
        if (virtual_address >= 1000) and (virtual_address <= 2999):
            index = self.global_memory.integers[0].index(virtual_address)
            return self.global_memory.integers[1][index]
        #global floats
        elif (virtual_address >= 3000) and (virtual_address <= 5999):
            index = self.global_memory.floats[0].index(virtual_address)
            return self.global_memory.floats[1][index]
        #global strings
        elif (virtual_address >= 6000) and (virtual_address <= 9999):
            index = self.global_memory.strings[0].index(virtual_address)
            return self.global_memory.strings[1][index]
        # local integers
        elif (virtual_address >= 10000) and (virtual_address <= 12999):
            index = self.local_memory[-1].integers[0].index(virtual_address)
            return self.local_memory[-1].integers[1][index]
        # local floats
        elif (virtual_address >= 13000) and (virtual_address <= 15999):
            index = self.local_memory[-1].floats[0].index(virtual_address)
            return self.local_memory[-1].floats[1][index]
        # local stringse
        elif (virtual_address >= 16000) and (virtual_address <= 19999):
            index = self.local_memory[-1].strings[0].index(virtual_address)
            return self.local_memory[-1].strings[1][index]
        # temporal integers
        elif (virtual_address >= 20000) and (virtual_address <= 22999):
            index = self.temporal_memory[-1].integers[0].index(virtual_address)
            return self.temporal_memory[-1].integers[1][index]
        # temporal floats
        elif (virtual_address >= 23000) and (virtual_address <= 25999):
            index = self.temporal_memory[-1].floats[0].index(virtual_address)
            return self.temporal_memory[-1].floats[1][index]
        # temporal strings
        elif (virtual_address >= 26000) and (virtual_address <= 29999):
            index = self.temporal_memory[-1].strings[0].index(virtual_address)
            return self.temporal_memory[-1].strings[1][index]
        # constants
        elif (virtual_address >= 30000) and (virtual_address <= 32999):
            index = self.constants[0].index(virtual_address)
            return self.constants[1][index]



    def allocate_in_memory(self, virtual_address, item):
        #global integers
        if (virtual_address >= 1000) and (virtual_address <= 2999):
            index = self.global_memory.integers[0].index(virtual_address)
            self.global_memory.integers[1][index] = item
        #global floats
        elif (virtual_address >= 3000) and (virtual_address <= 5999):
            index = self.global_memory.floats[0].index(virtual_address)
            self.global_memory.floats[1][index] = item
        #global strings
        elif (virtual_address >= 6000) and (virtual_address <= 9999):
            index = self.global_memory.strings[0].index(virtual_address)
            self.global_memory.strings[1][index] = item
        # local integers
        elif (virtual_address >= 10000) and (virtual_address <= 12999):
            index = self.local_memory[-1].integers[0].index(virtual_address)
            self.local_memory[-1].integers[1][index] = item
        # local floats
        elif (virtual_address >= 13000) and (virtual_address <= 15999):
            index = self.local_memory[-1].floats[0].index(virtual_address)
            self.local_memory[-1].floats[1][index] = item
        # local stringse
        elif (virtual_address >= 16000) and (virtual_address <= 19999):
            index = self.local_memory[-1].strings[0].index(virtual_address)
            self.local_memory[-1].strings[1][index] = item
        # temporal integers
        elif (virtual_address >= 20000) and (virtual_address <= 22999):
            index = self.temporal_memory[-1].integers[0].index(virtual_address)
            self.temporal_memory[-1].integers[1][index] = item
        # temporal floats
        elif (virtual_address >= 23000) and (virtual_address <= 25999):
            index = self.temporal_memory[-1].floats[0].index(virtual_address)
            self.temporal_memory[-1].floats[1][index] = item
        # temporal strings
        elif (virtual_address >= 26000) and (virtual_address <= 29999):
            index = self.temporal_memory[-1].strings[0].index(virtual_address)
            self.temporal_memory[-1].strings[1][index] = item
        # constants
        elif (virtual_address >= 30000) and (virtual_address <= 32999):
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
