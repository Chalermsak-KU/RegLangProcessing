from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

delta = {   # a DFA that accepts (01 U 010)*
    ('s', '0') : '0',
    ('0', '1') : '01',
    ('01', '0'): '010',
    ('010', '0'): '0',
    ('010', '1'): '01'
}
dfa1 = dfa(delta=delta, start='s', finals={'s', '01', '010'})
print('DFA that accepts (01 U 010)* is')
print(40*'-')
print(dfa1)
print(40*'-')
dfa2 = dfa1.complement()
print('Complemented DFA is')
print(40*'-')
print(dfa2)
print(40*'-')
