from drake_fuck.data import Source
from drake_fuck.lexer import Lexer
from drake_fuck.parser import Parser


class Memory:
    def __init__(self, size: int) -> None:
        self._location = 0
        self._data = [0] * size

    def right(self) -> None:
        self._location += 1

    def left(self) -> None:
        self._location -= 1

    @property
    def val(self) -> int:
        return self._data[self._location]

    @val.setter
    def val(self, value):
        self._data[self._location] = value


class BrainfuckProgram:
    def __init__(self, source: Source) -> None:
        self.source = source
        self.data = Memory(size=20)

    def run(self):
        commands = self.parse(self.source)
        commands.run(self)

    @staticmethod
    def parse(source: Source):
        lexer_builder = Lexer()
        parser_builder = Parser()

        lexer = lexer_builder.lexer
        parser = parser_builder.parser

        return parser.parse(source, lexer=lexer)
