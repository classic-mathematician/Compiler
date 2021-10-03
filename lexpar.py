import ply.lex as lex
import re
import codecs
import os
import sys


tokens = [

    #WORDS
    'ID',

    # OPERATORS
    'PLUS' ,        # +
    'MINUS' ,       # -
    'MULTIPLY',     # *
    'DIVIDE',       # /

    #ASSIGNATOR
    'EQUALS',       # =
    'SEMICOLON',


     # COMPARATORS
    'LT',           # <
    'GT',           # >
    'LTE',          # <=
    'GTE',          # >=
    'DOUBLEEQUAL',  # ==
    'AND',          # &
    'OR' ,          # |


    #BRACKETS
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # [
    'RBRACE',       # ]
    'BLOCKSTART',   # {
    'BLOCKEND',     # }


    # DATA TYPES
    'INTEGER',      # int
    'FLOAT',        # float
    'CHAR',         # char

    'COMMENT',      # %%

]


reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : 'DO',
    'for' : 'FOR',
    'return' : 'RETURN',
    'write' : 'WRITE',
    'to' : 'TO',
    'function' : 'FUNCTION',
    'void' : 'VOID',
    'vars' : 'VARS',
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    'read' : 'READ',
}

#addition of reserved words
tokens += list(reserved.values())


#regular expressions
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLY = r'\*'
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
t_AND = r'\&'
t_OR = r'\|'
t_COMMENT = r'\%\%.*'
t_ignore  = ' \t'



def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
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



data = '''
[25/(3*40) + {300-20} -16.5]
{(300-250)<(400-500)}
20 & 30 | 50 ;
VARS
for while
function
cham
%% This is a comment
'''

lexer.input(data)

for tok in lexer:
    print(tok)



# Parser
import  ply.yacc as yacc


precedence = (
    ('right', 'EQUALS'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'))


def p_program(p):
    '''program = block'''

def p_block(p):
	'''block : varDecl procDecl statement'''

def p_varDecl1(p):
	'''varDecl : VAR identList SEMMICOLOM'''

def p_varDeclEmpty(p):
	'''varDecl : empty'''

def p_identList1(p):
	'''identList : ID'''

def p_identList2(p):
	'''identList : identList COMMA ID'''

def p_procDecl1(p):
	'''procDecl : procDecl function TYPE ID LPAREN FUNC_PARAM RPAREN block'''

def p_procDeclEmpty(p):
	'''procDecl : empty'''

def p_statement1(p):
	'''statement : IF condition THEN statement'''

def p_statement2(p):
	'''statement : WHILE condition DO statement'''

def p_statementEmpty(p):
	'''statement : empty'''

def p_statementList1(p):
	'''statementList : statement'''

def p_relation1(p):
	'''relation : EQUALS'''

def p_relation2(p):
	'''relation : LT'''

def p_relation3(p):
	'''relation : GT'''

def p_relation4(p):
	'''relation : LTE'''

def p_relation5(p):
	'''relation : GTE'''

def p_expression1(p):
	'''expression : term'''

def p_expression2(p):
	'''expression : addOperator term'''

def p_expression3(p):
	'''expression : expression addOperator term'''

def p_addingOperator1(p):
	'''addOperator : PLUS'''

def p_minusOperator2(p):
	'''addOperator : MINUS'''

def p_term(p):
	'''term : factor'''

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''

def p_factor1(p):
	'''factor : ID'''

def p_factor2(p):
	'''factor : NUMBER'''

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''

def p_empty(p):
	'''empty :'''
	pass




yacc.yacc()
