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


reserved = {
    'if' : 'IF_K',
    'then' : 'THEN_K',
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
t_OR = r'\|'
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


lexer = lex.lex()


import  ply.yacc as yacc


#creation of quad motor object
qm = QuadMotor()
vm = VirtualMemory()
FUNC_DIR = FunctionDirectory()
last_seen_func = "base"
last_type_seen = "base"



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


def p_program(p):
    '''PROGRAM : PROGRAM_K ID neural_program_id SEMICOLON BLOCK'''
    print("correct syntax")


def p_neural_program_id(p):
    '''neural_program_id : EMPTY'''
    global last_seen_func
    last_seen_func = p[-1]

    FUNC_DIR.program_name = p[-1]
    FUNC_DIR.declare_function(p[-1], "program_type", "g_scope",)


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
    '''VAR_LIST : ID VAR_LIST2'''


def p_var_list2(p):
    '''VAR_LIST2 : COMMA ID VAR_LIST2
                 | EMPTY'''
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









def p_type(p):
    '''TYPE : INT_K NEURAL_TYPE
            | FLOAT_K NEURAL_TYPE
            | STRING_K NEURAL_TYPE'''
    global last_type_seen
    last_type_seen = p[1]



def p_neural_type(p):
    '''NEURAL_TYPE : EMPTY'''

def p_proc_block(p):
    '''PROC_BLOCK : PROC_DECL'''

def p_proc_decl(p):
    '''PROC_DECL : PROC_DECL_RETURN
                 | PROC_DECL_VOID
                 | EMPTY'''


def p_proc_decl_void(p):
    '''PROC_DECL_VOID : FUNCTION_K VOID_K ID neural_proc_void_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART PROC_BODY BLOCKEND PROC_DECL'''


def p_neural_proc_void_id(p):
    '''neural_proc_void_id : EMPTY'''
    global last_seen_func
    global last_type_seen
    last_seen_func = p[-1]
    last_type_seen = p[-2]
    FUNC_DIR.declare_function(last_seen_func, last_type_seen, "l_scope")



def p_proc_decl_return(p):
    '''PROC_DECL_RETURN : FUNCTION_K TYPE ID neural_proc_return_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART PROC_BODY RETURN BLOCKEND PROC_DECL'''


def p_neural_proc_return_id(p):
    '''neural_proc_return_id : EMPTY'''
    global last_seen_func
    last_seen_func = p[-1]
    FUNC_DIR.declare_function(last_seen_func, last_type_seen, "l_scope")
    FUNC_DIR.functions[FUNC_DIR.program_name]['var_table'][0].append(p[-1])
    FUNC_DIR.functions[FUNC_DIR.program_name]['var_table'][1].append(last_type_seen)


def p_neural_param_decl(p):
    '''neural_param_decl : EMPTY'''

def p_param_decl(p):
    '''PARAM_DECL : TYPE ID neuro PARAM_DECL_R
                  | EMPTY'''
    #reset of virtual memory
    vm.reset()


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

def p_proc_body_r(p):
    '''PROC_BODY_R : PROC_BODY
                   | EMPTY'''

def p_statement(p):
    '''STATEMENT : ASSIGN SEMICOLON
                 | FUNC_CALL SEMICOLON
                 | READ SEMICOLON
                 | WRITE SEMICOLON
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
            | FOR_LOOP'''

def p_while_loop(p):
    '''WHILE_LOOP : WHILE_K LPAREN H_EXPRESSION RPAREN BLOCKSTART STATEMENT_R BLOCKEND'''

def p_for_loop(p):
    '''FOR_LOOP : FOR_K ID EQUALS INT TO_K INT DO_K BLOCKSTART STATEMENT_R BLOCKEND'''

def p_decision(p):
    '''DECISION : IF_K LPAREN H_EXPRESSION RPAREN EXP_RESULT_NEURAL BLOCKSTART STATEMENT_R BLOCKEND DECISION_ALT DECISION_END_NEURAL'''

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

def p_decision_end_neural(p):
    '''DECISION_END_NEURAL : EMPTY'''
    dest = qm.jumps_stack.pop()
    qm.QUADS[dest-1][3] = qm.quad_counter

def p_decision_alt(p):
    '''DECISION_ALT : ELSE
                    | EMPTY'''

def p_else(p):
    '''ELSE : ELSE_K BLOCKSTART STATEMENT_R BLOCKEND'''


def p_assign(p):
    '''ASSIGN : VAR ASSIGN_VAR_N EQUALS EQUALS_NEURAL H_EXPRESSION ASSI_H_EXP_NEURAL'''

def p_assi_h_exp_neural(p):
    '''ASSI_H_EXP_NEURAL : EMPTY'''
    global temporal_counter
    if qm.operand_stack:

        right_operand = qm.operand_stack.pop()
        right_type = qm.types_stack.pop()
        left_operand = qm.operand_stack.pop()
        left_type = qm.types_stack.pop()

        result_type = semantic_cube[left_type]['='][right_type]

        if result_type != 'e':
            result = 't' + str(temporal_counter)
            # temporal_counter += 1
            qm.generate_quad('=', right_operand, '_', left_operand)
            qm.operand_stack.append(result)
            qm.types_stack.append(result_type)

        else:
            error_msg = "Assignation type mismatch '{}' '{}' isn't valid".format(left_type, operator, right_type)
            raise Exception(error_msg)

def p_equals_neural(p):
    '''EQUALS_NEURAL : EMPTY'''
    qm.poper.append(p[-1])

def p_assing_var_n(p):
    '''ASSIGN_VAR_N : EMPTY'''
    qm.operand_stack.append(p[-1])

    # getting type
    index = FUNC_DIR.functions[last_seen_func]['var_table'][0].index(p[-1])
    type = FUNC_DIR.functions[last_seen_func]['var_table'][1][index]
    qm.types_stack.append(type)


def p_var(p):
    '''VAR : ID
           | ARRAY'''
    p[0] = p[1]

def p_array(p):
    '''ARRAY : ID LBRACE INT RBRACE'''

def p_func_call(p):
    '''FUNC_CALL : ID LPAREN ARG_LIST RPAREN'''

def p_arg_list(p):
    '''ARG_LIST : VAR ARG_LIST_R
                | CONSTANT ARG_LIST_R
                | ARG_LIST_R'''

def p_arglist_r(p):
    '''ARG_LIST_R : COMMA ARG_LIST
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
    '''WRITE_LIST : H_EXPRESSION WRITE_LIST_R
                  | CONSTANT CONSTANT_WRITE_N WRITE_LIST_R'''

def p_constant_write_n(p):
    '''CONSTANT_WRITE_N : EMPTY'''
    qm.operand_stack.append(p[-1])

def p_write_list_r(p):
    '''WRITE_LIST_R : WRITE_NEURAL COMMA WRITE_LIST
                    | WRITE_NEURAL EMPTY'''

def p_write_neural(p):
    '''WRITE_NEURAL : EMPTY'''
    result = qm.operand_stack.pop()
    qm.generate_quad('write', '_', '_', result)




def p_return(p):
    '''RETURN : RETURN_K LPAREN H_EXPRESSION RPAREN SEMICOLON'''


def p_expression(p):
    '''EXPRESSION : TERM NEURAL_EXPRESSION EXPRESSION_R'''

#4
temporal_counter = 1
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

#5
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

#2a
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
              | LPAREN H_EXPRESSION RPAREN'''

#1
def p_neural_id_fac(p):
    '''NEURAL_ID_FAC : EMPTY'''
    if (p[-1] in FUNC_DIR.functions[last_seen_func]['var_table'][0]):

        qm.operand_stack.append(p[-1])
        index = FUNC_DIR.functions[last_seen_func]['var_table'][0].index(p[-1])
        type = FUNC_DIR.functions[last_seen_func]['var_table'][1][index]
        qm.types_stack.append(type)

    else:
        error_msg = "Variable '{}' used but hast been declared in the currect scope".format(p[-1])
        raise Exception(error_msg)



def p_neural_id_cnt_fact(p):
    '''NEURAL_CNT_FACT : EMPTY'''




def p_s_expression(p):
    '''S_EXPRESSION : EXPRESSION
                    | EXPRESSION GT EXPRESSION
                    | EXPRESSION LT EXPRESSION
                    | EXPRESSION GTE EXPRESSION
                    | EXPRESSION LTE EXPRESSION
                    | EXPRESSION DOUBLEEQUAL EXPRESSION'''


def p_h_expression(p):
    '''H_EXPRESSION : S_EXPRESSION H_EXPRESSION_R'''


def p_h_expression_r(p):
    '''H_EXPRESSION_R : OR H_EXPRESSION
                      | AND H_EXPRESSION
                      | EMPTY'''


def p_principal_block(p):
    '''PRINCIPAL_BLOCK : MAIN_K LPAREN RPAREN BLOCKSTART PRINCIPAL_BODY BLOCKEND'''


def p_principal_body(p):
    '''PRINCIPAL_BODY : STATEMENT PRINCIPAL_BODY_R
                      | EMPTY'''


def p_principal_body_r(p):
    '''PRINCIPAL_BODY_R : PRINCIPAL_BODY'''

def p_empty(p):
    '''EMPTY : '''

parser = yacc.yacc()

input_file_path = "test.txt"

s = ""
with open(input_file_path) as f:
    lines = f.readlines()
    for l in lines:
        s += l[:-1]
    print(">> Parsing " + input_file_path + "...")


lexer.input(s)
parser.parse(s)

#print(FUNC_DIR.functions)
print(qm.QUADS)
#print(qm.types_stack)
