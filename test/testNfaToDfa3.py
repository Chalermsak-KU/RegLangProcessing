from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

delta04 = { # an NFA p75 ex.2.2.9(a) L&P: language a*b(aUb)*
    (0, 'a'):{0},
    (0, 'b'):{0, 2},
    (0, '') :{1},
    (1, 'b'):{2, 4},
    (2, 'a'):{3},
    (3, '') :{4},
    (4, 'a'):{3}
}

m04 = nfa(delta=delta04, start=0, finals={3, 4})
dash40 = 40*'-'
print('NFA is as follows:')
print(dash40)
print(m04)
print(dash40)

n04 = m04.to_dfa()
print('Equivalent DFA is as follows:')
print(dash40)
print(n04)
print(dash40)
