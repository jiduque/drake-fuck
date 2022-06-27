import unittest

from drake_fuck.convert import *


class ConversionTests(unittest.TestCase):
    brain_fuck_code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    drake_fuck_code = "I'm on one I'm on one I'm on one I'm on one I'm on one I'm on one I'm on one I'm on one " \
                          "started from the bottom right foot I'm on one I'm on one I'm on one I'm on one started " \
                          "from the bottom right foot I'm on one I'm on one right foot I'm on one I'm on one I'm on " \
                          "one right foot I'm on one I'm on one I'm on one right foot I'm on one left foot left foot " \
                          "left foot left foot it's not one now we here right foot I'm on one right foot I'm on one " \
                          "right foot it's not one right foot right foot I'm on one started from the bottom left foot " \
                          "now we here left foot it's not one now we here right foot right foot out right foot it's " \
                          "not one it's not one it's not one out I'm on one I'm on one I'm on one I'm on one I'm on " \
                          "one I'm on one I'm on one out out I'm on one I'm on one I'm on one out right foot right " \
                          "foot out left foot it's not one out left foot out I'm on one I'm on one I'm on one out " \
                          "it's not one it's not one it's not one it's not one it's not one it's not one out it's not " \
                          "one it's not one it's not one it's not one it's not one it's not one it's not one it's not " \
                          "one out right foot right foot I'm on one out right foot I'm on one I'm on one out"

    def test_to_drake(self):
        input_code = self.brain_fuck_code
        expected_output = self.drake_fuck_code

        output = to_drake(input_code)
        self.assertEqual(expected_output, output)

    def test_something(self):
        input_code = self.drake_fuck_code
        expected_output = self.brain_fuck_code

        output = to_brain(input_code)
        self.assertEqual(expected_output, output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
