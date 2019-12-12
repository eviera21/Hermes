import ply.lex as lex
import ply.yacc as yacc
from env_controller import EnvController
import re

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
    'server' : 'SERVER',
    'message' : 'MESSAGE',
    'data' : 'DATA',
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
var = {}
env = EnvController()

def p_statement_start_stop_client(p):
    '''
    statement: START CLIENT NAME
                | STOP NAME
    '''
    if p[1] == 'start' and p[2] == 'client':
        client = p[3]
            #start client
        env.create_client(client)
    elif p[1] == 'stop':
        #we delete the server
        env.delete_client_or_server(p[2])
    else:
        print('yikes, that client start/stop did not work')

def p_statement_start_server(p):
    '''
    statement: START SERVER NAME
    '''
    if p[1] == 'start' and p[2] == 'server':
            server = p[3]
            #start server
            size = len(p)
            if(size == 4):
                env.create_server(server, "localhost",0)
                return
            env.create_server(server, p[4].replace('"',''), p[5])
    else:
        print('yikes, that server start did not work')

def p_statement_post(p):
    '''
    statement : NAME POST NAME expression
    '''
    if p[2] == 'post':
        #send message
        varName = p[2]
        env.info(varName)
    else:
        print("I mean, that was supposed to work. How did you mess it up? That did NOT post.")

def p_statement_connect(p):
    '''statement : NAME CONNECT NAME'''
    if p[2] == 'connect':
        client = p[1]
        target = p[3]
        data = env.verify_var(target)
        if re.match("http:\/\/www\. | https:\/\/www\. | http:\/\/", data.__str__()):
            env.connect_external(client,data)
            return
        msg = "PING PING PING . . ."
        env.send_messsage(client, target, msg)
    else:
        print("yikes, there's an error in local connection ...")

def p_statement_message(p):
    """
    statement : NAME POST NAME INT
            | NAME POST NAME FLOAT
            | NAME POST NAME STRING
    """
    if p[2] == "message":
        size = len(p)
        env.send_messsage(p[1],p[3],p[4].replace('"',''))
    else:
        print("yikes while sending message ...")

def p_statement_data(p):
    'statement: DATA NAME'
    if p[1] == "data":
        env.info(p[2])
    else:
        print("yikes while getting variable data ...")

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
