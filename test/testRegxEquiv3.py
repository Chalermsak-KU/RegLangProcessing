from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

# r1 is the regx of {w in {0,1}*: w ends with 10}
r1 = regx('(0U1)*10')
r2 = regx('@*(0U1)*10')
r3 = regx('@U(0U1)*10')
r4 = regx('0*(10*)*10')
r5 = regx('1*(01*)*10')
print(r1, '==', r2, 'is', r1 == r2)
print(r1, '==', r3, 'is', r1 == r3)
print(r1, '==', r4, 'is', r1 == r4)
print(r1, '==', r5, 'is', r1 == r5)

dfa1delta = { # this dfa accepts the same language as r1's
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
r6 = dfa1.to_regx()
print(f'The above dfa accepts the language with regx {r6}')
print(40*'-')
print(r1, '==', r6, 'is', r1 == r6)
print(40*'-')

r7 = regx('(0U01U011)*')
print(r1, '==', r7, 'is', r1 == r7)

