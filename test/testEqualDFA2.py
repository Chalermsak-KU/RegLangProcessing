from reglang import fa

delta1 = {  # DFA p.100 L&P with one more final state
    (1, 'a') : 2,
    (1, 'b') : 3,
    (2, 'a') : 4,
    (2, 'b') : 1,
    (3, 'a') : 1,
    (3, 'b') : 4,
    (4, 'a') : 4,
    (4, 'b') : 4
}
dfa1 = fa.dfa(delta=delta1, start=1, finals={1,2})
print('dfa1 is')
print(dfa1)
print(40*'-')

# start state differs from dfa1's
delta2 = {  
    (1, 'a') : 2,
    (1, 'b') : 3,
    (2, 'a') : 4,
    (2, 'b') : 1,
    (3, 'a') : 1,
    (3, 'b') : 4,
    (4, 'a') : 4,
    (4, 'b') : 4
}
dfa2 = fa.dfa(delta=delta2, start=2, finals={1,2})
print('dfa2 is')
print(dfa2)
print(40*'-')
print(f'dfa1 == dfa2 is {dfa1 == dfa2}')
print(40*'-')

# final states differ from dfa1's
delta3 = {
    (1, 'a') : 2,
    (1, 'b') : 3,
    (2, 'a') : 4,
    (2, 'b') : 1,
    (3, 'a') : 1,
    (3, 'b') : 4,
    (4, 'a') : 4,
    (4, 'b') : 4
}
dfa3 = fa.dfa(delta=delta3, start=1, finals={1,3})
print('dfa3 is')
print(dfa3)
print(40*'-')
print(f'dfa1 == dfa3 is {dfa1 == dfa3}')
print(40*'-')

# Sigma differs from dfa1's
delta4 = {
    (1, 'a') : 2,
    (1, 'c') : 3,
    (2, 'a') : 4,
    (2, 'c') : 1,
    (3, 'a') : 1,
    (3, 'c') : 4,
    (4, 'a') : 4,
    (4, 'c') : 4
}
dfa4 = fa.dfa(delta=delta4, start=1, finals={1,2})
print('dfa4 is')
print(dfa4)
print(40*'-')
print(f'dfa1 == dfa4 is {dfa1 == dfa4}')
print(40*'-')

# delta differs from dfa1's
delta5 = {
    (1, 'a') : 2,
    (1, 'b') : 3,
    (2, 'a') : 4,
    (2, 'b') : 1,
    (3, 'a') : 1,
    (3, 'b') : 4,
    (4, 'a') : 4,
    (4, 'b') : 2  # here is what differs
}
dfa5 = fa.dfa(delta=delta5, start=1, finals={1,2})
print('dfa5 is')
print(dfa5)
print(40*'-')
print(f'dfa1 == dfa5 is {dfa1 == dfa5}')
print(40*'-')

