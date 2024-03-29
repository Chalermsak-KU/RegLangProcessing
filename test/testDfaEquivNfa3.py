from reglang.dfa import dfa
from reglang.nfa import nfa

dfa1delta = { # this dfa accepts binary strings that ends with 10
    (1, '0') : 1,
    (1, '1') : 2,
    (2, '0') : 3,
    (2, '1') : 2,
    (3, '0') : 1,
    (3, '1') : 2
}

dfa1 = dfa(delta=dfa1delta, start=1, finals={3})
print('dfa1 is')
print(dfa1)
print(40*'-')

nfa2delta = { # this nfa accepts the same language as dfa1's
    (1, '0') : {1},
    (1, '1') : {1, 2},
    (2, '0') : {3}
}
nfa2 = nfa(delta=nfa2delta, start=1, finals={3})
print(40*'-')
print('nfa2 is')
print(nfa2)
print(40*'-')

print(f'dfa1.equiv(nfa2) is {dfa1.equiv(nfa2)}')

