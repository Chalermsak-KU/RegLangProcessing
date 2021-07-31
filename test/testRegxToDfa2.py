from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

rstr = '(0U1)*111(0U1)*'
r = regx(rstr)
m = r.to_dfa()
print(f'Regular expression is {rstr}')
print(f'Resulting DFA is')
print(m)

