from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

nfa1delta = { # this nfa is essentially a dfa that accepts the complement of (01 U 010)*
    (0, '0') : {1},
    (0, '1') : {4},
    (1, '0') : {4},
    (1, '1') : {2},
    (2, '0') : {3},
    (2, '1') : {4},
    (3, '0') : {1},
    (3, '1') : {2},
    (4, '0') : {4},
    (4, '1') : {4}
}

nfa1 = nfa(delta=nfa1delta, start=0, finals={1, 4})
print('nfa1 is')
print(nfa1)
print(40*'-')

nfa2delta = { # this nfa accepts a different language from nfa1's
    (0, '0') : {1},
    (1, '1') : {2},
    (2, '0') : {3},
    (3, '0') : {1},
    (3, '1') : {2}
}
nfa2 = nfa(delta=nfa2delta, start=0, finals={2,3})
print(40*'-')
print('nfa2 is')
print(nfa2)
print(40*'-')

print(f'nfa1.equiv(nfa2) is {nfa1.equiv(nfa2)}')
print(f'nfa2.equiv(nfa1) is {nfa2.equiv(nfa1)}')

nfa3delta = { # this nfa accepts a different language from nfa1's
    (0, '0') : {1, 2},
    (1, '1') : {0},
    (2, '1') : {3},
    (3, '0') : {0}
}
nfa3 = nfa(delta=nfa3delta, start=0, finals={1,3})
print(40*'-')
print('nfa3 is')
print(nfa3)
print(40*'-')

print(f'nfa1.equiv(nfa3) is {nfa1.equiv(nfa3)}')
print(f'nfa2.equiv(nfa3) is {nfa2.equiv(nfa3)}')

nfa4delta = { # this nfa accepts a different language from nfa1's
    (0, '0') : {1},
    (1, '1') : {2},
    (2, '0') : {0},
    (2, '')  : {0}
}
nfa4 = nfa(delta=nfa4delta, start=0, finals={0,1,2})
print(40*'-')
print('nfa4 is')
print(nfa4)
print(40*'-')

print(f'nfa1.equiv(nfa4) is {nfa1.equiv(nfa4)}')
print(f'nfa2.equiv(nfa4) is {nfa2.equiv(nfa4)}')
print(f'nfa3.equiv(nfa4) is {nfa3.equiv(nfa4)}')
