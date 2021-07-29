from reglang import fa

delta1 = {  # DFA that accepts strings in {a,b,c}* that has no substring ac
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
dfa1 = fa.dfa(delta=delta1, start=0, finals={0,1})
print('dfa1 is')
print(dfa1)
print(40*'-')
delta2 = {  # another DFA that accepts the same language as dfa1
    (1, 'a') : 2,
    (1, 'b') : 3,
    (1, 'c') : 1,
    (2, 'a') : 2,
    (2, 'b') : 3,
    (2, 'c') : 5,
    (3, 'a') : 2,
    (3, 'b') : 3,
    (3, 'c') : 4,
    (4, 'a') : 2,
    (4, 'b') : 3,
    (4, 'c') : 4,
    (5, 'a') : 5,
    (5, 'b') : 5,
    (5, 'c') : 5
}
dfa2 = fa.dfa(delta=delta2, start=1, finals={1,2,3,4})
print('dfa2 is')
print(dfa2)
print(40*'-')
print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
