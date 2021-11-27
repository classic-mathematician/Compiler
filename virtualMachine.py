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
        self.first_eq = False
        self.gosub_stack = []
        self.gosub_ip_stack = []




    def run(self):
        while(self.IP <= len(self.quads)):

            self.act()


    def print_quads(self):
        cnt = 1

        for quad in self.quads:
            print(cnt, quad)
            cnt += 1


    def print_constants(self):
        print(self.constants)


    def act(self):
        quad = self.quads[self.IP - 1]
        print(self.IP, quad)

        action = quad[0]


        if action == 'ERA':
            func_name = quad[2]
            self.func_stack.append(func_name)
            self.local_memory.append(Memory())
            self.temporal_memory.append(Memory())

            for address in self.func_dir[func_name]['var_table'][2]:
                self.register(address)

            self.IP += 1

        elif action == 'ENDFunc':
            self.local_memory.pop()
            self.temporal_memory.pop()
            self.func_stack.pop()



            self.IP = self.gosub_ip_stack.pop()


        elif action == 'write':
            print(self.find_in_memory(int(quad[3])))

            self.IP += 1


        elif action == 'GOSUB':
            type = self.func_dir[quad[1]]['type']

            if (type != 'void'):


                #saves the quad that is next of a function that returns something
                self.gosub_ip_stack.append(self.IP+1)



                next_quad = self.quads[self.IP]


                #goes to the quad of the function
                self.IP = int(quad[2])

                virtual_address = int(next_quad[3])
                self.gosub_stack.append(virtual_address)

            else:


                self.gosub_ip_stack.append(self.IP + 1 )



                self.IP = int(quad[2])


        elif action == 'PARAMETER':



            thing_to_store = self.find_in_memory(int(quad[1]))

            if thing_to_store == None:
                index = self.local_memory[-2].integers[0].index(int(quad[1]))
                thing_to_store = self.local_memory[-2].integers[1][index]


            index_to_store = int(quad[2])

            self.allocate_in_memory(self.func_dir[self.func_stack[-1]]['var_table'][2][index_to_store], thing_to_store)
            self.IP += 1


        elif action == 'RETURN':
            ret_val = self.find_in_memory(int(quad[1]))
            loc_to_store = self.gosub_stack.pop()
            self.allocate_in_memory(loc_to_store, ret_val)

            self.IP = self.gosub_ip_stack.pop()

        elif action == 'GOTO_MAIN':
            self.IP = int(quad[3])


        elif action == 'GOTO':
            self.IP = int(quad[3])


        elif action == 'GOTOF':
            cond = self.find_in_memory(int(quad[1]))

            if (cond > 0):
                self.IP += 1
            else:
                self.IP = int(quad[3])

        elif action == 'GOTOT':
            cond = self.find_in_memory(int(quad[1]))
            print(cond)

            if (cond > 0):
                self.IP = int(quad[3])
            else:
                self.IP += 1


        elif action == 'VERIFY':
            self.first_eq = True

            left_operand = int(quad[1])
            self.register(left_operand)

            right_operand = int(quad[2])
            self.register(right_operand)



            if (self.find_in_memory(left_operand) >= right_operand):
                error_msg = "Index out of bounds, {} exceeds size {}".format(self.find_in_memory(left_operand), right_operand)
                raise Exception(error_msg)

            self.IP += 1


        elif action == '=':
            left_operand = int(quad[1])
            right_operand = int(quad[3])

            self.register(left_operand)
            self.register(right_operand)

            #si el cuádruplo anterior no es un GOSUB
            if (self.quads[self.IP-2][0] != 'GOSUB' ):


                '''
                if self.first_eq == True:

                    #getting the real address
                    found = False
                    count = 1
                    address = 404
                    while(found == False):
                        if (self.quads[self.IP-count][1] == right_operand):
                            found = True
                            address = self.quads[self.IP - count][3]
                        count += 1

                    inside_memory = self.find_in_memory(address)
                    self.register(inside_memory)
                                                #address
                    self.allocate_in_memory(inside_memory, self.find_in_memory(left_operand))
                    self.first_eq = False


                else:'''
                    #                        place to assign        thing to assign
                self.allocate_in_memory(right_operand, self.find_in_memory(left_operand))



            self.IP += 1

        elif action == '+':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)

            #2D ARRAY
            if (self.quads[self.IP-4][0] == 'VERIFY' and self.quads[self.IP-5][0] == 'VERIFY'):
                # se suma la dirección base con lo demás
                result = first_operand + self.find_in_memory(second_operand)
                self.allocate_in_memory(third_operand, result)

            #1D ARRAY
            elif (self.quads[self.IP-2][0] == 'VERIFY' and self.quads[self.IP-3][0] != 'VERIFY'):
                result = first_operand + self.find_in_memory(second_operand)
                self.allocate_in_memory(third_operand, result)

                #modification of next quad
                base_dir = self.quads[self.IP-1][1]

                index_to_mod = 0
                if base_dir == self.quads[self.IP][3]:
                    index_to_mod = 3

                else:
                    index_to_mod = 1

                self.quads[self.IP][index_to_mod] = str(result)
                print("current quad", self.quads[self.IP][3])




            else:
                result = self.find_in_memory(first_operand) + self.find_in_memory(second_operand)
                self.allocate_in_memory(third_operand, result)

            self.IP += 1


        elif action == '-':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)

            result = self.find_in_memory(first_operand) - self.find_in_memory(second_operand)
            self.allocate_in_memory(third_operand, result)
            self.IP += 1


        elif action == '*':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)


            if (self.quads[self.IP-2][0] == 'VERIFY' and self.quads[self.IP-3][0] == 'VERIFY'):
                # se suma la dirección base con lo demás
                result = self.find_in_memory(first_operand) * second_operand
                self.allocate_in_memory(third_operand, result)

            else:


                result = self.find_in_memory(first_operand) * self.find_in_memory(second_operand)
                self.allocate_in_memory(third_operand, result)
            self.IP += 1


        elif action == '/':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)

            result = self.find_in_memory(first_operand) / self.find_in_memory(second_operand)
            self.allocate_in_memory(third_operand, result)
            self.IP += 1


        elif action == '>':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)
            self.IP += 1




            result = self.find_in_memory(first_operand) > self.find_in_memory(second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            self.allocate_in_memory(third_operand, result)

        elif action == '||':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)
            self.IP += 1



            result = self.find_in_memory(first_operand) or self.find_in_memory(second_operand)

            if result > 0:
                result = 1

            else:
                result = -1

            self.allocate_in_memory(third_operand, result)


        elif action == '&&':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)
            self.IP += 1



            result = self.find_in_memory(first_operand) and self.find_in_memory(second_operand)

            if result > 0:
                result = 1

            else:
                result = -1

            self.allocate_in_memory(third_operand, result)


        elif action == '<':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)




            result = self.find_in_memory(first_operand) < self.find_in_memory(second_operand)


            if result == True:
                result = 1

            else:
                result = -1

            self.allocate_in_memory(third_operand, result)
            self.IP += 1



        elif action == '>=':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)




            result = self.find_in_memory(first_operand) >= self.find_in_memory(second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            self.allocate_in_memory(third_operand, result)
            self.IP += 1



        elif action == '<=':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)

            result = self.find_in_memory(first_operand) <= self.find_in_memory(second_operand)

            if result == True:
                result = 1

            else:
                result = -1

            self.allocate_in_memory(third_operand, result)
            self.IP += 1



        elif action == '==':
            first_operand = int(quad[1])
            second_operand = int(quad[2])
            third_operand = int(quad[3])

            self.register(first_operand)
            self.register(second_operand)
            self.register(third_operand)


            result = (self.find_in_memory(first_operand) == self.find_in_memory(second_operand))

            if result == True:
                result = 1

            else:
                result = -1

            self.allocate_in_memory(third_operand, result)


            self.IP += 1



    #registers addresses that arent already inside the memory
    def register(self, virtual_address):

        # global integers
        if (virtual_address >= 1000) and (virtual_address <= 2999):

            #if not found, register it
            if virtual_address not in self.global_memory.integers[0]:
                self.global_memory.integers[0].append(virtual_address)
                self.global_memory.integers[1].append(None)

        # global floats
        elif (virtual_address >= 3000) and (virtual_address <= 5999):
            if virtual_address not in self.global_memory.floats[0]:

                #if not found, register it
                self.global_memory.floats[0].append(virtual_address)
                self.global_memory.floats[1].append(None)

        # global strings
        elif (virtual_address >= 6000) and (virtual_address <= 9999):
            if virtual_address not in self.global_memory.strings[0]:
                self.global_memory.strings[0].append(virtual_address)
                self.global_memory.strings[1].append(None)



        # local integers
        elif (virtual_address >= 10000) and (virtual_address <= 12999):

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



    # returns the content associated to an address
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
        elif (virtual_address >= 30000) and (virtual_address <= 39999):
            index = self.constants[0].index(virtual_address)
            return self.constants[1][index]


    #stores a desired item in an specific address
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
        elif (virtual_address >= 30000) and (virtual_address <= 39999):
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
