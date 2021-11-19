from toolsE import *


def p_array(p):
    '''ARRAY : ID ARR_ID_NP DIM'''

last_arr_id = None
def p_arr_id_np(p):
    '''ARR_ID_NP : EMPTY'''
    global last_arr_id
    last_arr_id = p[-1]
    FUNC_DIR.functions[last_seen_func]['var_table'][0].append(p[-1])
    FUNC_DIR.functions[last_seen_func]['var_table'][1].append(last_type_seen)
    FUNC_DIR.functions[last_seen_func]['var_table'][3][p[-1]] = 'array'
    ll = LinkedList()
    tn = Node()
    tn.DIM = 1
    tn.R = 1
    ll.head = tn
    FUNC_DIR.functions[last_seen_func]['var_table'][4][p[-1]] = ll

arr_size = []
def p_dim(p):
    '''DIM : LBRACE INT LIM_NP RBRACE DIM_R'''
    p[0] = p[-2]
    FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id].tail().next = None
    temp = self.head
    while (temp):
        print (temp.DIM)
        temp = temp.next



def p_lim_np(p):
    '''LIM_NP : EMPTY'''
    global last_arr_id
    global arr_size
    arr_size.append(p[-1])
    FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id].tail().limS = p[-1]
    FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id].tail().R *= (p[-1] + 1 )

def p_dim_r(p):
    '''DIM_R : PRE_DIM DIM
             | EMPTY'''

def p_pre_dim(p):
    '''PRE_DIM : EMPTY'''
    global last_arr_id
    FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id].tail().DIM += 1
    tn = Node()
    tn.R = FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id].tail().R
    FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id].tail().next = tn
