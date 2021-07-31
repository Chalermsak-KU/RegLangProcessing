from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

delta = {  # DFA p.93 L&P (for eliminating nonreachable states)
    (1, 'a') : 2,
    (1, 'b') : 4,
    (2, 'a') : 5,
    (2, 'b') : 3,
    (3, 'a') : 2,
    (3, 'b') : 6,
    (4, 'a') : 1,
    (4, 'b') : 5,
    (5, 'a') : 5,
    (5, 'b') : 5,
    (6, 'a') : 3,
    (6, 'b') : 5,
    (7, 'a') : 6,
    (7, 'b') : 8,
    (8, 'a') : 7,
    (8, 'b') : 3
}
dfa1 = dfa(delta=delta, start=1, finals={1, 3, 7})
print('Original DFA is')
print(40*'-')
print(dfa1)
print(40*'-')
reachable_dfa = dfa1.remove_nonreachable()
print('nonreachable-free DFA is')
print(40*'-')
print(reachable_dfa)
print(40*'-')

