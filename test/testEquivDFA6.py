from reglang import fa

delta1 = {  # DFA that accepts the empty set
    (0, 'a') : 1,
    (0, 'b') : 0,
    (0, 'c') : 0,
    (1, 'a') : 1,
    (1, 'b') : 0,
    (1, 'c') : 2,
    (2, 'a') : 2,
    (2, 'b') : 2,
    (2, 'c') : 2
}
dfa1 = fa.dfa(delta=delta1, start=0, finals=set())
print('dfa1 is')
print(dfa1)
print(40*'-')
delta2 = {  # another DFA that accepts the empty set but different alphabet
    (1, 'a') : 2,
    (1, 'b') : 1,
    (2, 'a') : 2,
    (2, 'b') : 1,
    (3, 'a') : 2,
    (3, 'b') : 3
}
dfa2 = fa.dfa(delta=delta2, start=1, finals={3})
print('dfa2 is')
print(dfa2)
print(40*'-')
print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
