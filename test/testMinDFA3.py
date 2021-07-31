from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

#-----------------------#
delta_n7 = {  # DFA p.156 HMU, 3rd Ed. (for minimization algo)
    ('A', 0) : 'B',
    ('A', 1) : 'F',
    ('B', 0) : 'G',
    ('B', 1) : 'C',
    ('C', 0) : 'A',
    ('C', 1) : 'C',
    ('D', 0) : 'C',
    ('D', 1) : 'G',
    ('E', 0) : 'H',
    ('E', 1) : 'F',
    ('F', 0) : 'C',
    ('F', 1) : 'G',
    ('G', 0) : 'G',
    ('G', 1) : 'E',
    ('H', 0) : 'G',
    ('H', 1) : 'C'
}
n7 = dfa(delta=delta_n7, start='A', finals={'C'})
print('\nDFA n7:')
print(40*'-')
print(n7)
print(40*'-')
print('\nAbout to Minimize n7 (method 1: L&P)')
min1_n7 = n7.minimized1()
print('\nMinimized n7 is (method 1: L&P)')
print(40*'-')
print(min1_n7)
print(40*'-')
print('\nAbout to Minimize n7 (method 2: marking algo)')
min2_n7 = n7.minimized2()
print('\nMinimized n7 is (method 2: marking algo)')
print(40*'-')
print(min2_n7)
print(40*'-')

