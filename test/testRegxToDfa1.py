from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

rstr = 'c*(aUbc*)*'
r = regx(rstr)
m = r.to_dfa()
print(f'Regular expression is {rstr}')
print(f'Resulting DFA is')
print(m)

