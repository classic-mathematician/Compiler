#autor: Sergio Eduardo Vega Guzmán
#fecha: Noviembre 30 2021




import ply.lex as lex
import re
import codecs
import os
import sys
from QuadMotor import *
from SemanticCube import *
from tools import *

#virtual memory

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



#declaración de tokens
tokens = [

    #WORDS
    'ID',

    # OPERATORS
    'PLUS' ,        # +
    'MINUS' ,       # -
    'TIMES',     # *
    'DIVIDE',       # /

    #ASSIGNATOR
    'EQUALS',       # =
    'SEMICOLON',    # ;

    #TYPES
    'INT',
    'FLOAT',
    'STRING',

     # COMPARATORS
    'LT',           # <
    'GT',           # >
    'LTE',          # <=
    'GTE',          # >=
    'DOUBLEEQUAL',  # ==
    'AND',          # &&
    'OR' ,          # |


    #BRACKETS
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # [
    'RBRACE',       # ]
    'BLOCKSTART',   # {
    'BLOCKEND',     # }
    'COLON',        # :
    'COMMA',        # ,

    'COMMENT',      # %%

]



# declaración de palabras reservadas
reserved = {
    'if' : 'IF_K',
    'else' : 'ELSE_K',
    'while' : 'WHILE_K',
    'do' : 'DO_K',
    'for' : 'FOR_K',
    'return' : 'RETURN_K',
    'write' : 'WRITE_K',
    'to' : 'TO_K',
    'function' : 'FUNCTION_K',
    'void' : 'VOID_K',
    'vars' : 'VARS_K',
    'program' : 'PROGRAM_K',
    'main' : 'MAIN_K',
    'read' : 'READ_K',
    'int' : 'INT_K',
    'float' : 'FLOAT_K',
    'string' : 'STRING_K',
}


#addition of reserved words
tokens += list(reserved.values())


#regular expressions
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_BLOCKSTART = r'\{'
t_BLOCKEND = r'\}'
t_EQUALS = r'\='
t_SEMICOLON = r'\;'
t_GT = r'\>'
t_LT = r'\<'
t_LTE = r'\<\='
t_GTE = r'\>\='
t_DOUBLEEQUAL = r'\=\='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_COMMENT = r'\%\%.*'
t_ignore  = ' \t'
t_COLON = r'\:'
t_COMMA = R'\,'


def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
     r'"(?:[^"\\]|\\.)*"'
     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Invalid character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


#inizialización del lexer
lexer = lex.lex()


#importación de ply (herramienta para lex y pars)
import  ply.yacc as yacc


#creation de objetos pertinentes QuadMotor (organizador de quads y sus operaciones) VirtualMemory (organizador y repartidor de direcciones virtuales)
qm = QuadMotor()
vm = VirtualMemory()

#creación de objeto tipo FunctionDirectory (organizador de todo lo relacionado con el directorio de funciones, más especificación en el archivo tools.py)
FUNC_DIR = FunctionDirectory()

#tabla de constantes, index 0 es el valor numérico, index 1 es la dirección virtual
CNT_TABLE = [[],[]]
last_seen_func = "base"
function_stack = []
last_type_seen = "base"
first_func = False


precedence = (
    ('right', 'EQUALS'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'))


def p_error(p): # Error rule for syntax errors
    print(">> Syntax error in input!")
    print(">> Unexpected token:", p)
    exit()



#columna vertebral de la gramática, regla que engloba todo
def p_program(p):
    '''PROGRAM : PROGRAM_K ID neural_program_id SEMICOLON BLOCK'''
    print("correct syntax")

program_name = "nada"


# punto neurálgico que se encarga de guardar el nombre del programa y añadirlo al directorio de funciones
def p_neural_program_id(p):
    '''neural_program_id : EMPTY'''
    global last_seen_func
    global function_stack
    global program_name

    last_seen_func = p[-1]
    program_name = p[-1]
    function_stack.append(p[-1])

    FUNC_DIR.program_name = p[-1]
    FUNC_DIR.declare_function(p[-1], "program_type", "g_scope",)


# división principal de la columba vertebral, bloque de variables principales, bloque de procedimientos y función "main"
def p_block(p):
    '''BLOCK : VAR_BLOCK PROC_BLOCK PRINCIPAL_BLOCK'''

def p_var_block(p):
    '''VAR_BLOCK : VARS_K BLOCKSTART VAR_DECL BLOCKEND'''

def p_var_decl(p):
    '''VAR_DECL : TYPE COLON VAR_LIST SEMICOLON VAR_DECL_R'''

def p_var_decl_r(p):
    '''VAR_DECL_R : VAR_DECL
                  | EMPTY'''

def p_var_list(p):
    '''VAR_LIST : VAR VAR_LIST2'''


#punto neurálgico, almacenaje de variables con sus tipos en el directorio de funciones sí y solo si la función que las declara existe
def p_var_list2(p):
    '''VAR_LIST2 : COMMA VAR VAR_LIST2
                 | EMPTY'''

    if last_seen_func != 'base':
        if (p[-1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):
            error_msg = "Variable '{}' has already been declared in the currect scope".format(p[-1])
            raise Exception(error_msg)
        else:
            if (p[-1] != None):

                FUNC_DIR.functions[last_seen_func]['var_table'][0].append(p[-1])
                FUNC_DIR.functions[last_seen_func]['var_table'][1].append(last_type_seen)
                FUNC_DIR.functions[last_seen_func]['paramorder'].append(last_type_seen)


                #virtual memory allocation
                scope = FUNC_DIR.functions[last_seen_func]['scope']
                virtual_address = vm.add(scope, last_type_seen)
                FUNC_DIR.functions[last_seen_func]['var_table'][2].append(virtual_address)






#detección de tipos, registra el último tipo visto en una variable global last_type_seen
def p_type(p):
    '''TYPE : INT_K NEURAL_TYPE
            | FLOAT_K NEURAL_TYPE
            | STRING_K NEURAL_TYPE'''
    global last_type_seen
    last_type_seen = p[1]
    p[0] = 1



def p_neural_type(p):
    '''NEURAL_TYPE : EMPTY'''

def p_proc_block(p):
    '''PROC_BLOCK : PROC_DECL'''

def p_proc_decl(p):
    '''PROC_DECL : PROC_DECL_RETURN
                 | PROC_DECL_VOID
                 | EMPTY'''



#regla para la declaración de funciones de tipo void
def p_proc_decl_void(p):
    '''PROC_DECL_VOID : FUNCTION_K VOID_K ID neural_proc_void_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART FN_VARBLOCK PROC_BODY BLOCKEND POST_FUNC PROC_DECL'''


#creación de primer cuádrulo en caso de que sea la primer función en ser declarada, registro de última función vista y agregación de la función al directorio de funciones con su respectivo tipo y scope.
def p_neural_proc_void_id(p):
    '''neural_proc_void_id : EMPTY'''
    global first_func
    global last_seen_func
    global last_type_seen
    if (first_func == False):
        qm.generate_quad('GOTO_MAIN', '_', '_', '_')
        first_func = True
    last_seen_func = p[-1]
    last_type_seen = p[-2]
    FUNC_DIR.declare_function(last_seen_func, last_type_seen, "l_scope")


#regla para la declaración de funciones que regresan valor
def p_proc_decl_return(p):
    '''PROC_DECL_RETURN : FUNCTION_K TYPE ID neural_proc_return_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART FN_VARBLOCK PROC_BODY BLOCKEND POST_FUNC PROC_DECL'''



# punto neurálgico para cuando cualquier función termina, creación de cuádruplo endfunc y reseteo de las direcciones del asignador
def p_post_func(p):
    '''POST_FUNC : EMPTY'''
    qm.generate_quad('ENDFunc', '_', '_', '_')
    global temporal_counter
    temporal_counter = 1
    vm.reset()


# punto neurálgico similar a la función void, en caso de ser la primer función, crea el cuádruplo goto main. Agregación de dicha función al directorio de funciones junto con sus respectivos atributos.
def p_neural_proc_return_id(p):
    '''neural_proc_return_id : EMPTY'''
    global first_func
    if (first_func == False):
        qm.generate_quad('GOTO_MAIN', '_', '_', '_')
        first_func = True
    global last_seen_func
    last_seen_func = p[-1]

    FUNC_DIR.declare_function(last_seen_func, last_type_seen, "l_scope")
    FUNC_DIR.functions[FUNC_DIR.program_name]['var_table'][0].append(p[-1])
    FUNC_DIR.functions[FUNC_DIR.program_name]['var_table'][1].append(last_type_seen)
    virtual_add = vm.add("g_scope", last_type_seen)
    FUNC_DIR.functions[FUNC_DIR.program_name]['var_table'][2].append(virtual_add)



def p_neural_param_decl(p):
    '''neural_param_decl : EMPTY'''

def p_param_decl(p):
    '''PARAM_DECL : TYPE VAR neuro PARAM_DECL_R
                  | EMPTY'''
    #reset of virtual memory



#registro de variables, con la condición de que estas no haya sido declaradas anteriormente en el mismo scope, se les asigna una dirección virtual
def p_neuro(p):
    '''neuro : EMPTY'''
    if last_seen_func != 'base':
        if (p[-1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):
            error_msg = "Variable '{}' has already been declared in the currect scope".format(p[-1])
            raise Exception(error_msg)
        else:
            FUNC_DIR.functions[last_seen_func]['var_table'][0].append(p[-1])
            FUNC_DIR.functions[last_seen_func]['var_table'][1].append(last_type_seen)
            FUNC_DIR.functions[last_seen_func]['paramorder'].append(last_type_seen)

            #virtual memory allocation
            scope = FUNC_DIR.functions[last_seen_func]['scope']
            virtual_address = vm.add(scope, last_type_seen)
            FUNC_DIR.functions[last_seen_func]['var_table'][2].append(virtual_address)


def p_param_decl_r(p):
    '''PARAM_DECL_R : COMMA PARAM_DECL
                    | EMPTY'''

def p_proc_body(p):
    '''PROC_BODY : STATEMENT PROC_BODY_R'''


#conteo de tamaño para poder utilizarlo en el Era
def p_fn_varblock(p):
    '''FN_VARBLOCK : VARS_K BLOCKSTART LS_VARDECL BLOCKEND'''

    #couting of local variables
    work_space_size = len(FUNC_DIR.functions[last_seen_func]['var_table'][0])
    FUNC_DIR.functions[last_seen_func]['size'] = work_space_size
    FUNC_DIR.functions[last_seen_func]['start_address'] = qm.quad_counter



def p_ls_vardecl(p):
    '''LS_VARDECL : TYPE COLON FNVAR_LS SEMICOLON LS_VARDECL_R'''


def p_ls_vardecl_r(p):
    '''LS_VARDECL_R : LS_VARDECL
                    | EMPTY'''


def p_fnvar_ls(p):
    '''FNVAR_LS : VAR FNVAR_LS2'''


#punto neurálgico con la misma funcionalidad que todos los relacionados con la declaración de variables, se registran si no han sido declaradas anteriormente.
def p_fnvar_ls2(p):
    '''FNVAR_LS2 : COMMA FNVAR_LS
                 | EMPTY'''
    if last_seen_func != 'base':

        if (p[-1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):
            error_msg = "Variable '{}' has already been declared in the currect scope".format(p[-1])
            raise Exception(error_msg)
        else:
            if (p[-1] != None):

                FUNC_DIR.functions[last_seen_func]['var_table'][0].append(p[-1])
                FUNC_DIR.functions[last_seen_func]['var_table'][1].append(last_type_seen)


                #virtual memory allocation
                scope = FUNC_DIR.functions[last_seen_func]['scope']
                virtual_address = vm.add(scope, last_type_seen)
                FUNC_DIR.functions[last_seen_func]['var_table'][2].append(virtual_address)


def p_proc_body_r(p):
    '''PROC_BODY_R : PROC_BODY
                   | EMPTY'''


def p_statement(p):
    '''STATEMENT : ASSIGN SEMICOLON
                 | ASSIGN1 SEMICOLON
                 | FUNC_CALL SEMICOLON
                 | READ SEMICOLON
                 | WRITE SEMICOLON
                 | RETURN
                 | FLOW
                '''


def p_statement_r(p):
    '''STATEMENT_R : STATEMENT STATEMENT_R
                   | EMPTY'''


def p_flow(p):
    '''FLOW : DECISION
            | LOOP'''


def p_loop(p):
    '''LOOP : WHILE_LOOP
            | DO_WHILE_LOOP SEMICOLON
            | FOR_LOOP'''


def p_do_while_loop(p):
    '''DO_WHILE_LOOP : DO_K DW_PREV_NEURAL BLOCKSTART STATEMENT_R BLOCKEND WHILE_K LPAREN H_EXPRESSION RPAREN DW_END_NEURAL'''


#agregación a la pila de saltos, el contador actual de los cuádruplos
def p_dw_prev_neural(p):
    '''DW_PREV_NEURAL : EMPTY'''
    qm.jumps_stack.append(qm.quad_counter)



#punto neurálgico del do while, se extraen los respectivos valores delas pilas del objeto quadMotor y se crea el cuádruplo GOTOT, se evidencía el uso de la lógica entera, puesto que si el tipo del ret no es int, no se procede.
def p_dw_end_neural(p):
    '''DW_END_NEURAL : EMPTY'''
    ret = qm.jumps_stack.pop()
    cond = qm.operand_stack.pop()
    cond_type = qm.types_stack.pop()
    if (cond_type == 'int'):
        qm.generate_quad('GOTOT', cond, '_', ret)
    else:
        error_msg = "Type mismatch '{}' type isnt valid for a conditional statement".format(exp_type)
        raise Exception(error_msg)

def p_while_loop(p):
    '''WHILE_LOOP : WHILE_K WHILE_PREV_NEURAL LPAREN H_EXPRESSION RPAREN WHILE_POST_NEURAL BLOCKSTART STATEMENT_R BLOCKEND WHILE_END_NEURAL'''

#1 punto neurálgico, se agrega a la pila de tipos el contador de cuádruplos
def p_while_prev_neural(p):
    '''WHILE_PREV_NEURAL : EMPTY'''
    qm.jumps_stack.append(qm.quad_counter)

#2 punto neurálgico para el while, se hace exactamente lo mismo que para el do while, con la diferencia de que para el while se genera un cuádruplo distinto, GOTOF
def p_while_post_neural(p):
    '''WHILE_POST_NEURAL : EMPTY'''
    exp_type = qm.types_stack.pop()
    if (exp_type == 'int'):
        result = qm.operand_stack.pop()
        qm.generate_quad('GOTOF', result, '_', '_')
        qm.jumps_stack.append(qm.quad_counter - 1)

    else:
        error_msg = "Type mismatch '{}' type isnt valid for a conditional statement".format(exp_type)
        raise Exception(error_msg)

# Punto neurálgico final, se genera el cuádruplo GOTO para cuando no se cumple la condición.
def p_while_end_neural(p):
    '''WHILE_END_NEURAL : EMPTY'''
    end = qm.jumps_stack.pop()
    ret = qm.jumps_stack.pop()
    qm.generate_quad('GOTO', '_', '_', ret)
    qm.QUADS[end-1][3] = qm.quad_counter




def p_for_loop(p):
    '''FOR_LOOP : FOR_K ID EQUALS INT TO_K INT DO_K BLOCKSTART STATEMENT_R BLOCKEND'''

def p_decision(p):
    '''DECISION : IF_K LPAREN H_EXPRESSION RPAREN EXP_RESULT_NEURAL BLOCKSTART STATEMENT_R BLOCKEND DECISION_ALT DECISION_END_NEURAL'''


#punto neurálgico para las expresiones de los condicionales, si el tipo no es entero no se prodece. Se genera un GOTOF en caso de operar como se espera y se agrega el contador de cuádruplos - 1 a la pila de saltos.
def p_exp_result_neural(p):
    '''EXP_RESULT_NEURAL : EMPTY'''
    exp_type = qm.types_stack.pop()
    if (exp_type == 'int'):
        result = qm.operand_stack.pop()
        qm.generate_quad('GOTOF', result, '_', '_')
        qm.jumps_stack.append(qm.quad_counter - 1)

    else:
        error_msg = "Type mismatch '{}' type isnt valid for a conditional statement".format(exp_type)
        raise Exception(error_msg)


#se asigna el destino sacándolo de la pila de tipos, y se modifica la última parte del cuádruplo asignándole el contador actual de cuádruplos
def p_decision_end_neural(p):
    '''DECISION_END_NEURAL : EMPTY'''
    dest = qm.jumps_stack.pop()
    qm.QUADS[dest-1][3] = qm.quad_counter

def p_decision_alt(p):
    '''DECISION_ALT : ELSE
                    | EMPTY'''

def p_else(p):
    '''ELSE : ELSE_NEURAL ELSE_K BLOCKSTART STATEMENT_R BLOCKEND'''


#se genera el cuádruplo para el Else de las condicionales, un goto y nuevamente se modifica un cuádruplo existente con el índice false - 1
def p_else_neural(p):
    '''ELSE_NEURAL : EMPTY'''
    qm.generate_quad('GOTO', '_', '_', '_')
    false = qm.jumps_stack.pop()
    qm.jumps_stack.append(qm.quad_counter - 1)
    qm.QUADS[false-1][3] = qm.quad_counter



def p_right_assign(p):
    '''RIGHT_ASSIGN : H_EXPRESSION
                    | FUNC_CALL
                    | ARR_AC1'''



r_flag = False


#punto neurálgico para el accesso de los arrays, se valida que la cantidad de expresiones en su stack no supere las dimensiones permitidas por el lenguaje: R2 y
#se generan los cuádruplos correspondientes para calcular el desplazamiento
def p_arr_ac1(p):
    '''ARR_AC1 : ID ARR_ID_NP1 DIM_AC'''
    p[0] = p[1]
    global r_flag
    r_flag = True


    virtual_address = 0
    if (p[1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):

        index = FUNC_DIR.functions[last_seen_func]['var_table'][0].index(p[1])
        #getting its virtual address
        virtual_address = FUNC_DIR.functions[last_seen_func]['var_table'][2][index]


    elif (p[1] in FUNC_DIR.functions[program_name]['var_table'][0]):
        index = FUNC_DIR.functions[program_name]['var_table'][0].index(p[1])
        #getting its virtual address
        virtual_address = FUNC_DIR.functions[program_name]['var_table'][2][index]


    else:
        error_msg = "{} hast been declared in the current program".format(p[1])
        raise Exception(error_msg)


    global exp_stack



    if (len(exp_stack) > 2):
        error_msg = "Arrays over 2D arent allowed in this p-language"
        raise Exception(error_msg)




    if (len(exp_stack) == 1):
        dim_size = FUNC_DIR.functions[last_seen_func]['var_table'][4][p[1]][0]
        qm.generate_quad('VERIFY', exp_stack[0], dim_size, p[1])
        type = qm.types_stack.pop()

        # Se hace la fórmula c-style para 1 dimensión
        temporal = vm.add('t_scope', type)
        qm.generate_quad('+', virtual_address, exp_stack[0], temporal)
        qm.operand_stack.append(exp_stack[0])


    elif (len(exp_stack) == 2):
        dim_size = FUNC_DIR.functions[last_seen_func]['var_table'][4][p[1]][0]
        qm.generate_quad('VERIFY', exp_stack[0], dim_size, p[1])
        type = qm.types_stack.pop()

        dim_size2 = FUNC_DIR.functions[last_seen_func]['var_table'][4][p[1]][1]
        qm.generate_quad('VERIFY', exp_stack[1], dim_size2, p[1])
        type = qm.types_stack.pop()

        temporal = vm.add('t_scope', type)
        qm.generate_quad('*', exp_stack[0], dim_size2, temporal)
        qm.operand_stack.append(exp_stack[0])

        temporal1 = vm.add('t_scope', type)
        qm.generate_quad('+', temporal, exp_stack[1], temporal1)
        qm.operand_stack.append(exp_stack[1])

        temporal2 = vm.add('t_scope', type)
        qm.generate_quad('+', virtual_address, temporal1, temporal2)
        qm.operand_stack.append(exp_stack[0])


    else:
        error_msg = "Dimensions that are distinct from R1 or R2 arent supported"
        raise Exception(error_msg)


    exp_stack = []





def p_assign(p):
    '''ASSIGN : VAR ASSIGN_VAR_N EQUALS EQUALS_NEURAL RIGHT_ASSIGN ASSI_H_EXP_NEURAL'''


def p_assign1(p):
    '''ASSIGN1 : ARR_AC ASSIGN_VAR_N EQUALS EQUALS_NEURAL RIGHT_ASSIGN ASSI_H_EXP_NEURAL'''



def p_n(p):
    '''N : EMPTY'''

# generación del cuádruplo de asignación que precede a las funciones que regresan valor
def p_assi_h_exp_neural(p):
    '''ASSI_H_EXP_NEURAL : EMPTY'''
    global temporal_counter
    if qm.operand_stack:


        if (len(qm.operand_stack) > 2):
            qm.operand_stack.pop()
            qm.operand_stack.reverse()


        right_operand = qm.operand_stack.pop()
        right_type = qm.types_stack.pop()
        left_operand = qm.operand_stack.pop()
        left_type = qm.types_stack.pop()


        result_type = semantic_cube[left_type]['='][right_type]

        if result_type != 'e':
            result = 't' + str(temporal_counter)
            # temporal_counter += 1



            global r_flag
            if r_flag == True:
                qm.generate_quad('=', left_operand, '_', right_operand)
            else:
                qm.generate_quad('=', right_operand, '_', left_operand)
            r_flag = False


        else:
            error_msg = "Assignation type mismatch {} {} {} isn't valid".format(left_type, '=', right_type)
            raise Exception(error_msg)

# agregación de operador al popper
def p_equals_neural(p):
    '''EQUALS_NEURAL : EMPTY'''
    qm.poper.append(p[-1])


# asignacipón de variables, metiéndolas al stack de operadores
def p_assing_var_n(p):
    '''ASSIGN_VAR_N : EMPTY'''
    # getting type
    if (p[-1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):
        index = FUNC_DIR.functions[last_seen_func]['var_table'][0].index(p[-1])
        operand = FUNC_DIR.functions[last_seen_func]['var_table'][2][index]
        qm.operand_stack.append(operand)
        type = FUNC_DIR.functions[last_seen_func]['var_table'][1][index]
        qm.types_stack.append(type)


    elif (p[-1] in FUNC_DIR.functions[program_name]['var_table'][0]):
        index = FUNC_DIR.functions[program_name]['var_table'][0].index(p[-1])
        operand = FUNC_DIR.functions[program_name]['var_table'][2][index]
        qm.operand_stack.append(operand)
        type = FUNC_DIR.functions[program_name]['var_table'][1][index]
        qm.types_stack.append(type)

    else:
        error_msg = "array variable {} hasnt been declared in the current scope and nor in the global scope".format(p[-1])
        raise Exception(error_msg)

#array access para al lado izquierdo, es decir,para su asignación. por izquierdo me refiero a qué lado están del igual        p[x] = var (izquierdo) o var = p[x] (derecho)
def p_arr_ac(p):
    '''ARR_AC : ID ARR_ID_NP1 DIM_AC'''
    p[0] = p[1]


    virtual_address = 0
    if (p[1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):

        index = FUNC_DIR.functions[last_seen_func]['var_table'][0].index(p[1])
        #getting its virtual address
        virtual_address = FUNC_DIR.functions[last_seen_func]['var_table'][2][index]


    elif (p[1] in FUNC_DIR.functions[program_name]['var_table'][0]):
        index = FUNC_DIR.functions[program_name]['var_table'][0].index(p[1])
        #getting its virtual address
        virtual_address = FUNC_DIR.functions[program_name]['var_table'][2][index]


    else:
        error_msg = "{} hast been declared in the current program".format(p[1])
        raise Exception(error_msg)


    global exp_stack



    if (len(exp_stack) > 2):
        error_msg = "Arrays over 2D arent allowed in this p-language"
        raise Exception(error_msg)




    if (len(exp_stack) == 1):
        dim_size = FUNC_DIR.functions[last_seen_func]['var_table'][4][p[1]][0]
        qm.generate_quad('VERIFY', exp_stack[0], dim_size, p[1])
        type = qm.types_stack.pop()

        # Se hace la fórmula c-style para 1 dimensión
        temporal = vm.add('t_scope', type)
        qm.generate_quad('+', virtual_address, exp_stack[0], temporal)
        qm.operand_stack.pop()

    elif (len(exp_stack) == 2):
        dim_size = FUNC_DIR.functions[last_seen_func]['var_table'][4][p[1]][0]
        qm.generate_quad('VERIFY', exp_stack[0], dim_size, p[1])
        type = qm.types_stack.pop()

        dim_size2 = FUNC_DIR.functions[last_seen_func]['var_table'][4][p[1]][1]
        qm.generate_quad('VERIFY', exp_stack[1], dim_size2, p[1])
        type = qm.types_stack.pop()

        temporal = vm.add('t_scope', type)
        qm.generate_quad('*', exp_stack[0], dim_size2, temporal)
        qm.operand_stack.append(exp_stack[0])

        temporal1 = vm.add('t_scope', type)
        qm.generate_quad('+', temporal, exp_stack[1], temporal1)
        qm.operand_stack.append(exp_stack[1])

        temporal2 = vm.add('t_scope', type)
        qm.generate_quad('+', virtual_address, temporal1, temporal2)
        qm.operand_stack.append(exp_stack[0])


    else:
        error_msg = "Dimensions that are distinct from R1 or R2 arent supported"
        raise Exception(error_msg)


    exp_stack = []


#punto neurálgico que valida si la variable que se quiere accesar es de tipo array en primer lugar, después se agrega al stack de operandos y la pila de tipos
def p_arr_id_np1(p):
    '''ARR_ID_NP1 : EMPTY'''
    if (FUNC_DIR.functions[last_seen_func]['var_table'][3][p[-1]] != 'array'):
        error_msg = "{} var isnt array".format(p[-1])
        raise Exception(error_msg)


    if (p[-1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):


        index = FUNC_DIR.functions[last_seen_func]['var_table'][0].index(p[-1])
        #getting its virtual address
        operand = FUNC_DIR.functions[last_seen_func]['var_table'][2][index]
        #getting the type
        type = FUNC_DIR.functions[program_name]['var_table'][1][index]

        qm.operand_stack.append(operand)
        qm.types_stack.append(type)

    elif (p[-1] in FUNC_DIR.functions[program_name]['var_table'][0]):
        index = FUNC_DIR.functions[program_name]['var_table'][0].index(p[-1])
        #getting its virtual address
        operand = FUNC_DIR.functions[program_name]['var_table'][2][index]
        #getting the type
        type = FUNC_DIR.functions[program_name]['var_table'][1][index]

        qm.operand_stack.append(operand)
        qm.types_stack.append(type)

    else:
        error_msg = "{} hast been declared in the current program".format(p[-1])
        raise Exception(error_msg)


def p_dim_ac(p):
    '''DIM_AC : LBRACE H_EXPRESSION DIM_AC_PREV RBRACE DIM_AC_R'''


dimensions = 0
exp_stack = []

# punto neurálgico para empezar con el conteo de dimensiones
def p_dim_ac_prev(p):
    '''DIM_AC_PREV : EMPTY'''
    global dimensions
    global exp_stack
    dimensions += 1
    exp_stack.append(qm.operand_stack.pop())




def p_dim_ac_r(p):
    '''DIM_AC_R : DIM_AC
                | EMPTY'''

def p_var(p):
    '''VAR : ID
           | ARRAY'''
    p[0] = p[1]


from toolsE import *



#nueva validación de dimensiones para que no se excedan las permitidas y se agrega la dirección virtual calculada de acuerdo a su tamaño
def p_array(p):
    '''ARRAY : ID ARR_ID_NP DIM'''
    global program_name
    global dims
    global arr_size
    dims = 0
    size = 0



    if (len(arr_size) > 2):
        error_msg = "Dimensions over R2 arent currently supported"
        raise Exception(error_msg)


    if (arr_size[0] <= 0):
        error_msg = "Dimensions under R0 arent currently supported"
        raise Exception(error_msg)

    size = 1
    for item in arr_size:
        size = size * item


    scope = 'undef'
    if (last_seen_func == program_name):
        scope = 'g_scope'
    else:
        scope = 'l_scope'




    virtual_address = vm.add_arr(scope, last_type_seen, size)

    FUNC_DIR.functions[last_seen_func]['var_table'][2].append(virtual_address)
    arr_size = []

last_arr_id = None

# punto neurálgico, se agrega ala tabla de variables el nombre del array, su tipo, su tipo array y sus dimensiones inicializadas
def p_arr_id_np(p):
    '''ARR_ID_NP : EMPTY'''
    global last_arr_id
    last_arr_id = p[-1]
    FUNC_DIR.functions[last_seen_func]['var_table'][0].append(p[-1])
    FUNC_DIR.functions[last_seen_func]['var_table'][1].append(last_type_seen)
    FUNC_DIR.functions[last_seen_func]['var_table'][3][p[-1]] = 'array'
    FUNC_DIR.functions[last_seen_func]['var_table'][4][p[-1]] = [0, 0]

arr_size = []
def p_dim(p):
    '''DIM : LBRACE INT LIM_NP RBRACE DIM_R'''
    p[0] = p[-2]


# punto neurálgico, se completan las dimensiones oficiales de los arreglos que anteriormente solo habían sido inicializados
dims = 0
def p_lim_np(p):
    '''LIM_NP : EMPTY'''
    global last_arr_id
    global arr_size
    global dims
    arr_size.append(p[-1])
    FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id][dims] = p[-1]
    print(FUNC_DIR.functions[last_seen_func]['var_table'][4][last_arr_id])
    dims += 1

def p_dim_r(p):
    '''DIM_R : DIM
             | EMPTY'''




def p_func_call(p):
    '''FUNC_CALL : ID PRE_VERIFY LPAREN EXP_LIST POST_VERIFY RPAREN'''
    global last_call_seen
    last_call_seen = None



#verificación de los parámetros para las llamadas a función para que estos no excedan el número solicitado para dicha firma. creación de cuádruplo gosub dirigido a la dirección virtual de inicio
# si la función no es de tipo void, se hace el "parche guadalupano"
def p_post_verify(p):
    '''POST_VERIFY : EMPTY'''
    global param_counter

    if (param_counter -1 != len(FUNC_DIR.functions[p[-4]]['paramorder'])):
        error_msg = "Amount mismatch {} arguments were expected, {} were given".format(len(FUNC_DIR.functions[p[-4]]['paramorder']), param_counter -1)
        raise Exception(error_msg)
    else:
        param_counter = 0
        start_address = FUNC_DIR.functions[p[-4]]['start_address']
        qm.generate_quad('GOSUB', p[-4], start_address, '_')

        if FUNC_DIR.functions[p[-4]]['type'] != 'void':

            index = FUNC_DIR.functions[program_name]['var_table'][0].index(p[-4])
            type = FUNC_DIR.functions[program_name]['var_table'][1][index]
            result = FUNC_DIR.functions[program_name]['var_table'][2][index]
            temporal = vm.add('t_scope', type)
            qm.generate_quad('=', result, '_', temporal)
            qm.operand_stack.append(temporal)



param_counter = 0
last_call_seen = None


# creación de cuádruplo ERA en caso de que la función exista, se le agrega a dicho cuádruplo el tamaño de la función
def p_pre_verify(p):
    '''PRE_VERIFY : EMPTY'''
    global param_counter
    global last_call_seen

    last_call_seen = p[-1]
    type = FUNC_DIR.functions[p[-1]]['type']

    if (p[-1] not in FUNC_DIR.functions):
        error_msg = "Function {} doesnt exist".format(p[-1])
        raise Exception(error_msg)

    #elif (type != 'void'):
    #    error_msg = "Error, trying to invoke a non-void type function -{}- without linking it to a recieving variable".format(p[-1])
    #    raise Exception(error_msg)

    else:
        size = FUNC_DIR.functions[p[-1]]['size']
        qm.generate_quad('ERA', size, p[-1], '_')
        param_counter = 1


def p_exp_list(p):
    '''EXP_LIST : H_EXPRESSION EXP_NEURAL EXP_LIST_2'''


# punto neurálgico de expresiones para la asignación paramétrica, se extrae el paraámetro y el índice de dicho parámetro para poder verificarlo en la máquina virtual
# también se valida que los argumentos sean del tipo solicitado y que se presenten en el orden especificado
def p_exp_neural(p):
    '''EXP_NEURAL : EMPTY'''
    global param_counter
    global last_seen_func


    if last_call_seen != None:
        arg = qm.operand_stack.pop()
        arg_type = qm.types_stack.pop()
        if (arg_type == FUNC_DIR.functions[last_seen_func]['paramorder'][param_counter - 1]):
            qm.generate_quad('PARAMETER', arg, param_counter-1, '_')
            param_counter += 1

        else:
            error_msg = "Argument '{}' doesnt match the function p-signature".format(arg_type)
            raise Exception(error_msg)

    else:

        arg = qm.operand_stack.pop()
        arg_type = qm.types_stack.pop()
        if (arg_type == FUNC_DIR.functions[last_seen_func]['paramorder'][param_counter - 1]):
            qm.generate_quad('PARAMETER', arg, param_counter-1, '_')
            param_counter += 1

        else:
            error_msg = "Argument '{}' doesnt match the function p-signature".format(arg_type)
            raise Exception(error_msg)


def p_exp_list_2(p):
    '''EXP_LIST_2 : COMMA EXP_LIST
                  | EMPTY'''


def p_constant(p):
    '''CONSTANT : INT
                | FLOAT
                | STRING'''
    p[0] = p[1]


def p_read(p):
    '''READ : READ_K LPAREN ID_LIST RPAREN'''

def p_id_list(p):
    '''ID_LIST : ID READ_NEURAL ID_LIST_R'''

def p_read_neural(p):
    '''READ_NEURAL : EMPTY'''
    qm.generate_quad('read', '_', '_', p[-1])


def p_id_list_r(p):
    '''ID_LIST_R : COMMA ID_LIST
                 | EMPTY'''

def p_write(p):
    '''WRITE : WRITE_K LPAREN WRITE_LIST RPAREN'''

def p_write_list(p):
    '''WRITE_LIST : RIGHT_ASSIGN WRITE_LIST_R
                  | CONSTANT CONSTANT_WRITE_N WRITE_LIST_R'''

#agregación de constante a la tabla de constantes
def p_constant_write_n(p):
    '''CONSTANT_WRITE_N : EMPTY'''
    index = CNT_TABLE[0].index(p[-1])
    operand = CNT_TABLE[1][index]

    qm.operand_stack.append(operand)

def p_write_list_r(p):
    '''WRITE_LIST_R : WRITE_NEURAL COMMA WRITE_LIST
                    | WRITE_NEURAL EMPTY'''


# punto neurálgico para la escritura, se genera el cuádruplo write con el respectivo valor a escribir (dirección virtual)
def p_write_neural(p):
    '''WRITE_NEURAL : EMPTY'''
    result = qm.operand_stack.pop()
    qm.types_stack.pop()
    qm.generate_quad('write', '_', '_', result)


# punto neurálgico, generación de cuádruplo return al final de dicha expresión gramatical
def p_return(p):
    '''RETURN : RETURN_K LPAREN H_EXPRESSION RPAREN SEMICOLON'''
    qm.generate_quad('RETURN', qm.operand_stack.pop(), '_', '_')


def p_expression(p):
    '''EXPRESSION : TERM NEURAL_EXPRESSION EXPRESSION_R'''

#4
temporal_counter = 1


#punto neurálgico para el manejo de sumas, uso de cubo semántico para validar la congruencia de tipos y agregación de los operandos a las pilas
def p_neural_expression(p):
    '''NEURAL_EXPRESSION : EMPTY'''
    global temporal_counter
    if qm.poper:
        if qm.poper[-1] in ['+', '-']:
            right_operand = qm.operand_stack.pop()
            right_type = qm.types_stack.pop()

            left_operand = qm.operand_stack.pop()
            left_type = qm.types_stack.pop()

            operator = qm.poper.pop()
            result_type = semantic_cube[left_type][operator][right_type]

            if result_type != 'e':
                result = 't' + str(temporal_counter)
                temporal_counter += 1
                result = vm.add("t_scope", result_type)
                qm.generate_quad(operator, left_operand, right_operand, result)
                qm.operand_stack.append(result)
                qm.types_stack.append(result_type)

            else:
                error_msg = "Type mismatch '{}' '{}' '{}' isn't valid".format(left_type, operator, right_type)
                raise Exception(error_msg)




def p_expression_r(p):
    '''EXPRESSION_R : PLUS NEURAL_PLUS EXPRESSION
                    | MINUS NEURAL_MINUS EXPRESSION
                    | EMPTY'''


# agregación de operadores
#3a
def p_neural_plus(p):
    '''NEURAL_PLUS : EMPTY'''
    qm.poper.append(p[-1])


#3b
def p_neural_minus(p):
    '''NEURAL_MINUS : EMPTY'''
    qm.poper.append(p[-1])


def p_term(p):
    '''TERM : FACTOR NEURAL_TERM TERM_R'''

#5 lo mismo que para la sumas y restas, manejo de operandos y validación con el oráculo, cubo semántico
def p_neural_term(p):
    '''NEURAL_TERM : EMPTY'''
    global temporal_counter
    if qm.poper:

        if qm.poper[-1] in ['*', '/']:
            right_operand = qm.operand_stack.pop()
            right_type = qm.types_stack.pop()

            left_operand = qm.operand_stack.pop()
            left_type = qm.types_stack.pop()

            operator = qm.poper.pop()
            result_type = semantic_cube[left_type][operator][right_type]
            if result_type != 'e':
                result = 't' + str(temporal_counter)
                temporal_counter += 1
                result = vm.add("t_scope", result_type)
                qm.generate_quad(operator, left_operand, right_operand, result)
                qm.operand_stack.append(result)
                qm.types_stack.append(result_type)

            else:
                error_msg = "Type mismatch '{}' '{}' '{}' isn't valid".format(left_type, operator, right_type)
                raise Exception(error_msg)



def p_term_r(p):
    '''TERM_R : TIMES NEURAL_TIMES TERM
              | DIVIDE NEURAL_DIVIDE TERM
              | EMPTY'''

#2a agregación de operadores a la fila de operadores
def p_neural_times(p):
    '''NEURAL_TIMES : EMPTY'''
    qm.poper.append(p[-1])

#2b
def p_neural_divide(p):
    '''NEURAL_DIVIDE : EMPTY'''
    qm.poper.append(p[-1])


def p_factor_(p):
    '''FACTOR : ID NEURAL_ID_FAC
              | CONSTANT NEURAL_CNT_FACT
              | MINUS CONSTANT NEURAL_CNT_FACT
              | LPAREN H_EXPRESSION RPAREN'''

#1 lo mismo que con las sumas, se valida que exista la variable y si sí, se agrega a su respectiva pila para ser procesada tiempo después
def p_neural_id_fac(p):
    '''NEURAL_ID_FAC : EMPTY'''
    local = False
    if (p[-1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):

        index = FUNC_DIR.functions[last_seen_func]['var_table'][0].index(p[-1])
        operand = FUNC_DIR.functions[last_seen_func]['var_table'][2][index]
        type = FUNC_DIR.functions[last_seen_func]['var_table'][1][index]
        qm.operand_stack.append(operand)
        qm.types_stack.append(type)

    elif (p[-1] in FUNC_DIR.functions[program_name]['var_table'][0]):
        index = FUNC_DIR.functions[program_name]['var_table'][0].index(p[-1])
        operand = FUNC_DIR.functions[program_name]['var_table'][2][index]
        type = FUNC_DIR.functions[program_name]['var_table'][1][index]
        qm.operand_stack.append(operand)
        qm.types_stack.append(type)

    else:
        error_msg = "Variable '{}' used but hast been declared in the currect scope".format(p[-1])
        raise Exception(error_msg)


# validación del tipo de variables que son para agregar su tipo a la pila de tipos
def p_neural_cnt_fact(p):
    '''NEURAL_CNT_FACT : EMPTY'''
    type = "unassigned"

    if (isinstance(p[-1], int)):
        qm.types_stack.append('int')
        type = 'int'

    if (isinstance(p[-1], float)):
        qm.types_stack.append('float')
        type = 'float'

    if (isinstance(p[-1], str)):
        qm.types_stack.append('string')
        type = 'string'

    if (p[-1] not in CNT_TABLE[0]):

        CNT_TABLE[0].append(p[-1])
        virtual_address = vm.add('c_scope', type)
        CNT_TABLE[1].append(virtual_address)

    index = CNT_TABLE[0].index(p[-1])
    operand = CNT_TABLE[1][index]

    qm.operand_stack.append(operand)

def p_s_expression(p):
    '''S_EXPRESSION : EXPRESSION S_EXPRESSION_R'''


#punto neurálgico igual que con los demás operadores, se validan los operandos con el oráculo y si se aceptan se agregan a sus respectivas pilas
def p_neural_exp(p):
    '''NEURAL_EXP : EMPTY'''

    global temporal_counter
    if qm.poper:
        if qm.poper[-1] in ['>', '<', '>=', '<=', '==', '&&', '||']:
            right_operand = qm.operand_stack.pop()
            right_type = qm.types_stack.pop()

            left_operand = qm.operand_stack.pop()
            left_type = qm.types_stack.pop()

            operator = qm.poper.pop()
            result_type = semantic_cube[left_type][operator][right_type]
            if result_type != 'e':
                result = 't' + str(temporal_counter)
                temporal_counter += 1
                result = vm.add("t_scope", result_type)
                qm.generate_quad(operator, left_operand, right_operand, result)
                qm.operand_stack.append(result)
                qm.types_stack.append(result_type)

            else:
                error_msg = "Type mismatch '{}' '{}' '{}' isn't valid".format(left_type, operator, right_type)
                raise Exception(error_msg)

def p_s_expression_r(p):
    '''S_EXPRESSION_R : CONDI NEURAL_CONDI EXPRESSION NEURAL_EXP
                      | EMPTY'''


def p_neural_condi(p):
    '''NEURAL_CONDI : EMPTY'''

    qm.poper.append(p[-1])



def p_condi(p):
    '''CONDI : GT
             | LT
             | LTE
             | GTE
             | DOUBLEEQUAL
             | AND
             | OR'''

    p[0] = p[1]





def p_h_expression(p):
    '''H_EXPRESSION : S_EXPRESSION H_EXPRESSION_R'''


def p_h_expression_r(p):
    '''H_EXPRESSION_R : OR H_EXPRESSION
                      | AND H_EXPRESSION
                      | EMPTY'''


def p_principal_block(p):
    '''PRINCIPAL_BLOCK : MAIN_K MAIN_NEURAL LPAREN RPAREN BLOCKSTART PRINCIPAL_BODY BLOCKEND'''


#punto neurálgico main que indica dónde está el main para poder saltar a él
def p_main_neural(p):
    '''MAIN_NEURAL : EMPTY'''
    global last_seen_func
    global first_func
    if (first_func == True):
        qm.QUADS[0][3] = qm.quad_counter
    last_seen_func = program_name



def p_principal_body(p):
    '''PRINCIPAL_BODY : STATEMENT PRINCIPAL_BODY_R
                      | EMPTY'''


def p_o(p):
    '''O : EMPTY'''
    print("aaaaaaaaaaa")

def p_principal_body_r(p):
    '''PRINCIPAL_BODY_R : PRINCIPAL_BODY'''

def p_empty(p):
    '''EMPTY : '''

parser = yacc.yacc()

input_file_path = "testarr.txt"

s = ""
with open(input_file_path) as f:
    lines = f.readlines()
    for l in lines:
        s += l[:-1]
    print(">> Parsing " + input_file_path + "...")


lexer.input(s)
parser.parse(s)


print(FUNC_DIR.functions)

print(CNT_TABLE)

count = 1

for item in qm.QUADS:
    print(count, item)
    count += 1


# creation of obj file with the funciton directory
import json


with open('obj.txt', 'w') as file:
     file.write(json.dumps(FUNC_DIR.functions))


# creation of the file containing the table of constants

print(CNT_TABLE)

temp_dict = {"temporal" : CNT_TABLE}

with open('constants.txt', 'w') as file:
     file.write(json.dumps(temp_dict))


#creation of the file containing the quadruples


temp_dict = {"temporal" : qm.QUADS}
with open('quads.txt', 'w') as file:
     file.write(json.dumps(temp_dict))




# una disculpa por alternar entre inglés y español, pero durante el desarrolo escribía comentarios en inglés por costrumbre.







#
