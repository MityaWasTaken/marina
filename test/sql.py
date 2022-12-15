# unittesting for langauge

import sys

sys.path.append("../marina/sql")
# import lexer as l
import parse as p

test_string_1 = 'I hello'
test_string_2 = 'P'


# parser test code
p.Parser(test_string_2)

# lexer test code
# l = l.Lexer(test_string_1)
# print(l)