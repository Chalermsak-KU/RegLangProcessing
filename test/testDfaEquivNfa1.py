from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

dfa1delta = { # this dfa accepts (01 U 010)*
    (0, '0') : 1,
    (0, '1') : 4,
    (1, '0') : 4,
    (1, '1') : 2,
    (2, '0') : 3,
    (2, '1') : 4,
    (3, '0') : 1,
    (3, '1') : 2,
    (4, '0') : 4,
    (4, '1') : 4
}

dfa1 = dfa(delta=dfa1delta, start=0, finals={0, 2, 3})
print('dfa1 is')
print(dfa1)
print(40*'-')

nfa2delta = { # this nfa accepts the same language as dfa1's
    (0, '0') : {1},
    (1, '1') : {2},
    (2, '0') : {3},
    (3, '0') : {1},
    (3, '1') : {2}
}
nfa2 = nfa(delta=nfa2delta, start=0, finals={0, 2, 3})
print(40*'-')
print('nfa2 is')
print(nfa2)
print(40*'-')

print(f'dfa1.equiv(nfa2) is {dfa1.equiv(nfa2)}')

nfa3delta = { # this nfa accepts the same language as dfa1's
    (0, '0') : {1, 2},
    (1, '1') : {0},
    (2, '1') : {3},
    (3, '0') : {0}
}
nfa3 = nfa(delta=nfa3delta, start=0, finals={0})
print(40*'-')
print('nfa3 is')
print(nfa3)
print(40*'-')

print(f'dfa1.equiv(nfa3) is {dfa1.equiv(nfa3)}')

nfa4delta = { # this nfa accepts the same language as dfa1's
    (0, '0') : {1},
    (1, '1') : {2},
    (2, '0') : {0},
    (2, '')  : {0}
}
nfa4 = nfa(delta=nfa4delta, start=0, finals={0})
print(40*'-')
print('nfa4 is')
print(nfa4)
print(40*'-')

print(f'dfa1.equiv(nfa4) is {dfa1.equiv(nfa4)}')
