import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EXPONENT',
    'EQUALS',
    'STRING',
]

reserved = {
    'start' : 'START',
    'stop' : 'STOP',
    'connect' : 'CONNECT',
    'post' : 'POST',
    'get': 'GET',
    'clear' : 'CLEAR',
    'client' : 'CLIENT',
    'server' : 'SERVER'
}

tokens += reserved.values()

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_EXPONENT = r'\^'
t_ignore = r' '

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*\"'
    t.type = 'STRING'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9()]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal characters '%s'" % t.value[0])
    t.lexer.skip(1)

#This builds the lexer
lexer = lex.lex()

precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'EXPONENT')
)

def p_statement_start_stop_client(p):
    '''
    statement: START CLIENT NAME
                | STOP NAME
    '''
    if p[1] == 'start' and p[2] == 'client':
        client = p[3]
            #start client
    elif p[1] == 'stop':
        #we delete the server
    else:
        print('yikes, that client start/stop did not work')

def p_statement_start_server(p):
    '''
    statement: START SERVER NAME
    '''
    if p[1] == 'start' and p[2] == 'server':
            client = p[3]
            #start server
    else:
        print('yikes, that server start did not work')

def p_statement_post(p):
    '''
    statement : NAME POST NAME expression
    '''
    if p[2] == 'post':
        #send message
    else:
        print("I mean, that was supposed to work. How did you mess it up? That did NOT post.")

def p_statement_connect(p):
    '''statement : NAME CONNECT NAME'''
    if p[2] == 'connect':
        client = p[1]
        target = p[3]
        #yikes

def p_calc(p):
    '''
    calc : expression
        | var_assign
        | empty
    '''
    print(run(p[1]))

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])

def p_expression(p):
    '''
    expression : expression EXPONENT expression
                | expression MULTIPLY expression
                | expression DIVIDE expression
                | expression PLUS expression
                | expression MINUS expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_int_float(p):
    '''
    expression : INT
                | FLOAT
    '''
    p[0] = p[1]

def p_expression_str(p):
    '''
    expression : STRING
    '''
    p[0] = ('str', p[1])

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

def p_error(p):
    print("Syntax Error Detected!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

#This builds the parser
parser = yacc.yacc()
var = {}
#env

def run(p):
    if type(p) == tuple:
        if p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '^':
            return run(p[1]) ** run(p[2])
        elif p[0] == '=':
            var[p[1]] = run(p[2])
        elif p[0] == 'var':
            if p[1] not in var:
                return 'Undeclared variable found'
            else:
                return var[p[1]]
    else:
        return p


while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)

