import sys

from drake_fuck.lexer import Lexer

import ply.yacc as yacc


class Commands:
    def __init__(self):
        self.commands = []

    def run(self, program):
        for command in self.commands:
            command.run(program)


class Command:
    def __init__(self, command):
        self.command = command

    def run(self, program):
        if isinstance(self.command, Loop):
            self.command.run(program)

        if self.command == '+':
            program.data.val += 1

        if self.command == '-':
            program.data.val -= 1

        if self.command == '<':
            program.data.left()

        if self.command == '>':
            program.data.right()

        if self.command == '.':
            sys.stdout.write(chr(program.data.val))


class Loop:
    def __init__(self, commands):
        self.commands = commands

    def run(self, program):
        while program.data.val != 0:
            self.commands.run(program)


class Parser(object):

    tokens = Lexer.tokens

    def __init__(self):
        self.lexer = Lexer()
        self.parser = yacc.yacc(module=self)

    @staticmethod
    def p_commands(p):
        """
        commands : command
                 | commands command
        """
        if len(p) == 2:
            p[0] = Commands()
            p[0].commands = [p[1]]
            return

        if not p[1]:
            p[1] = Commands()

        p[1].commands.append(p[2])
        p[0] = p[1]

    @staticmethod
    def p_command(p):
        """
        command : INCREMENT
                | DECREMENT
                | SHIFT_LEFT
                | SHIFT_RIGHT
                | OUTPUT
                | INPUT
                | loop
        """
        if isinstance(p[1], str):
            p[0] = Command(p[1])
        else:
            p[0] = p[1]

    @staticmethod
    def p_loop(p):
        """
        loop : OPEN_LOOP commands CLOSE_LOOP
        """
        p[0] = Loop(p[2])

    @staticmethod
    def p_error(p):
        print("Syntax error in input!")
