from reglang import fa

#-----------------------#
delta_n5 = {  # DFA p.94 L&P (for minimization algo in L&P)
    (1, 'a') : 2,
    (1, 'b') : 4,
    (2, 'a') : 5,
    (2, 'b') : 3,
    (3, 'a') : 2,
    (3, 'b') : 6,
    (4, 'a') : 1,
    (4, 'b') : 5,
    (5, 'a') : 5,
    (5, 'b') : 5,
    (6, 'a') : 3,
    (6, 'b') : 5
}

n5 = fa.dfa(delta=delta_n5, start=1, finals={1, 3})
print('Original DFA is')
print(40*'-')
print(n5)
print(40*'-')
minimal_n5 = n5.minimized1()
print('Minimized DFA is')
print(40*'-')
print(minimal_n5)
print(40*'-')

