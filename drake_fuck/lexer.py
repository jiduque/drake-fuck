"""
TODO: make this into a my lexer class

"""

tokens = (
    'INCREMENT',
    'DECREMENT',
    'SHIFT_LEFT',
    'SHIFT_RIGHT',
    'OUTPUT',
    'INPUT',
    'OPEN_LOOP',
    'CLOSE_LOOP',
)

t_INCREMENT = r'\+'
t_DECREMENT = r'-'
t_SHIFT_LEFT = r'<'
t_SHIFT_RIGHT = r'>'
t_OUTPUT = r'\.'
t_INPUT = r','
t_OPEN_LOOP = r'\['
t_CLOSE_LOOP = r'\]'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)