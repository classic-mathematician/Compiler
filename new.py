import ply.lex as lex
import re
import codecs
import os
import sys
from QuadMotor import *



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

def p_type(p):
    '''TYPE : INT_K
            | FLOAT_K
            | STRING_K'''

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

def p_proc_decl_return(p):
    '''PROC_DECL_RETURN : FUNCTION_K TYPE ID neural_proc_return_id LPAREN PARAM_DECL RPAREN neural_param_decl BLOCKSTART PROC_BODY RETURN BLOCKEND PROC_DECL'''

def p_neural_proc_return_id(p):
    '''neural_proc_return_id : EMPTY'''

def p_neural_param_decl(p):
    '''neural_param_decl : EMPTY'''

def p_param_decl(p):
    '''PARAM_DECL : TYPE ID PARAM_DECL_R
                  | EMPTY'''

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
    '''DECISION : IF_K LPAREN H_EXPRESSION RPAREN BLOCKSTART STATEMENT_R BLOCKEND DECISION_ALT'''

def p_decision_alt(p):
    '''DECISION_ALT : ELSE_K DECISION
                    | BLOCKSTART STATEMENT_R BLOCKEND
                    | EMPTY'''

def p_statement_r(p):
    '''STATEMENT_R : STATEMENT STATEMENT_R
                   | EMPTY'''

def p_assign(p):
    '''ASSIGN : VAR EQUALS H_EXPRESSION'''

def p_var(p):
    '''VAR : ID
           | ARRAY'''

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

def p_read(p):
    '''READ : READ_K ID_LIST'''

def p_id_list(p):
    '''ID_LIST : ID ID_LIST_R'''

def p_id_list_r(p):
    '''ID_LIST_R : COMMA ID_LIST
                 | EMPTY'''

def p_write(p):
    '''WRITE : WRITE_K WRITE_LIST'''

def p_write_list(p):
    '''WRITE_LIST : H_EXPRESSION WRITE_LIST_R'''

def p_write_list_r(p):
    '''WRITE_LIST_R : COMMA H_EXPRESSION
                    | EMPTY'''

def p_return(p):
    '''RETURN : RETURN_K LPAREN H_EXPRESSION RPAREN SEMICOLON'''


def p_expression(p):
    '''EXPRESSION : TERM NEURAL_EXPRESSION EXPRESSION_R'''

#4
def p_neural_expression(p):
    '''NEURAL_EXPRESSION : EMPTY'''
    if qm.poper[0] in "+-":
        right_operand = qm.operand_stack.pop()
        left_operand = qm.operand_stack.pop()
        operator = qm.poper.pop()


def p_expression_r(p):
    '''EXPRESSION_R : PLUS NEURAL_PLUS EXPRESSION
                    | MINUS NEURAL_MINUS EXPRESSION
                    | EMPTY'''

#3a
def p_neural_plus(p):
    '''NEURAL_PLUS : EMPTY'''
    qm..append(p[-1])

#3b
def p_neural_minus(p):
    '''NEURAL_MINUS : EMPTY'''
    qm.poper.append(p[-1])


def p_term(p):
    '''TERM : FACTOR NEURAL_TERM TERM_R'''

#5
def p_neural_term(p):
    '''NEURAL_TERM : EMPTY'''



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
    '''FACTOR : ID NEURAL_ID
              | CONSTANT NEURAL_CNT
              | LPAREN EXPRESSION RPAREN'''

#1
def p_neural_id(p):
    '''NEURAL_ID : EMPTY'''
    qm.operand_stack.append(p[-1])
    qm.types_stack.append(p[-1])


def p_s_expression(p):
    '''S_EXPRESSION : EXPRESSION
                    | EXPRESSION GT EXPRESSION
                    | EXPRESSION LT EXPRESSION'''


def p_h_expression(p):
    '''H_EXPRESSION : S_EXPRESSION H_EXPRESSION_R'''


def p_h_expression_r(p):
    '''H_EXPRESSION_R : OR H_EXPRESSION
                      | AND H_EXPRESSION
                      | EMPTY'''


def p_principal_block(p):
    '''PRINCIPAL_BLOCK : MAIN_K LPAREN RPAREN BLOCKSTART PRINCIPAL_BODY BLOCKEND'''


def p_principal_body(p):
    '''PRINCIPAL_BODY : STATEMENT PRINCIPAL_BODY_R'''


def p_principal_body_r(p):
    '''PRINCIPAL_BODY_R : PRINCIPAL_BODY
                         | EMPTY'''


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
