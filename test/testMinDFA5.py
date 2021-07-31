from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

delta = {  # another NFA from lecture note about thm2.2.1
    (0, 'a'):{1},
    (0, 'b'):{0},
    (0, '' ):{2},
    (1, 'b'):{3},
    (1, '' ):{0, 4},
    (2, 'a'):{1},
    (2, 'b'):{2, 5},
    (2, '' ):{4},
    (3, '' ):{4},
    (4, 'a'):{4},
    (4, '' ):{6},
    (5, 'b'):{5},
    (5, '' ):{6},
    (6, 'a'):{6}
}

m = nfa(delta=delta, start=0, finals={4}) # accepts all binary strings
dash40 = 40*'-'
print('NFA is as follows:')
print(dash40)
print(m)
print(dash40)

n = m.to_dfa().standard_numbered()
print('Equivalent DFA is as follows:')
print(dash40)
print(n)
print(dash40)

nmin1 = n.minimized1(verbose=True)
print(nmin1)
print(dash40)
nmin2 = n.minimized2(verbose=True)
print(nmin2)
print(dash40)
print(f'nmin1.equiv(nmin2) is {nmin1.equiv(nmin2)}')
