import sys

Source = str
DFSource = Source
BFSource = Source


KeywordMap = list[tuple[str, str]]


class Memory:
    def __init__(self, size: int) -> None:
        self._location = 0
        self._data = [0] * size

    def right(self) -> None:
        self._location += 1

    def left(self) -> None:
        self._location -= 1

    @property
    def data(self) -> int:
        return self._data[self._location]


class Commands:
    def __init__(self):
        self.commands = []

    def run(self, program):
        for command in self.commands:
            command.run(program)

    def __str__(self):
        return ''.join([str(command) for command in self.commands])


class Command:
    def __init__(self, command):
        self.command = command

    def run(self, program):
        if isinstance(self.command, Loop):
            self.command.run(program)

        if self.command == '+':
            program.data[program.location] += 1
        if self.command == '-':
            program.data[program.location] -= 1
        if self.command == '<':
            program.location -= 1
        if self.command == '>':
            program.location += 1
        if self.command == '.':
            sys.stdout.write(chr(program.data[program.location]))

    def __str__(self):
        return self.command


class Loop:
    def __init__(self, commands):
        self.commands = commands

    def run(self, program):
        while program.data[program.location] != 0:
            self.commands.run(program)

    def __str__(self):
        return '[' + str(self.commands) + ']'
