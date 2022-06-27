from drake_fuck.runner import BrainfuckProgram


if __name__ == '__main__':
    code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    dfp = BrainfuckProgram(code)
    dfp.run()
