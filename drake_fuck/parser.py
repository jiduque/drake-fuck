"""
TODO: Turn this into a my parser class

"""


from drake_fuck.data import Commands, Command, Loop


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


def p_loop(p):
    """
    loop : OPEN_LOOP commands CLOSE_LOOP
    """
    p[0] = Loop(p[2])


def p_error(p):
    print("Syntax error in input!")

