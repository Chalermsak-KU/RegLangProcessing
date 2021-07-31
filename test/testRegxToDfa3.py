from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

rstr = '#'
r = regx(rstr)
m = r.to_dfa()
print(f'Regular expression is {rstr}')
print(f'Resulting DFA is')
print(m)

