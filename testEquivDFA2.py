import fa

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
delta2 = {  # differs from delta1 only in state names
    (10, 'a') : 20,
    (10, 'b') : 30,
    (20, 'a') : 40,
    (20, 'b') : 10,
    (30, 'a') : 10,
    (30, 'b') : 40,
    (40, 'a') : 40,
    (40, 'b') : 40
}
dfa2 = fa.dfa(delta=delta2, start=10, finals={10,20})
print('dfa2 is')
print(dfa2)
print(40*'-')
print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
