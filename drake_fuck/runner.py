"""
TODO: use lexer and parser from my class

"""

import drake_fuck.lexer as lex_rules
import drake_fuck.parser as par_rules

import ply.lex as lex
import ply.yacc as yacc


class BrainfuckProgram:
    def __init__(self, source):
        self.source = source
        self.data = [0] * 20
        self.location = 0

    def run(self):
        commands = self.parse(self.source)
        commands.run(self)

    @staticmethod
    def parse(source):
        lexer = lex.lex(module=lex_rules)
        parser = yacc.yacc(module=par_rules)
        return parser.parse(source)

    def __str__(self):
        return str(self.parse(self.source))
