from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

rstr = '(0U1)*111(0U1)*'
r = regx(rstr)
m = r.to_dfa()
print(f'Regular expression is {rstr}')
print(f'Resulting DFA is')
print(m)

