from reglang.dfa import dfa

#-----------------------#
delta_n6 = {  # DFA p.93 L&P (for eliminating nonreachable states)
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
    (6, 'b') : 5,
    (7, 'a') : 6,
    (7, 'b') : 8,
    (8, 'a') : 7,
    (8, 'b') : 3,

}
n6 = dfa(delta=delta_n6, start=1, finals={1, 3, 7})
print('Original DFA is')
print(40*'-')
print(n6)
print(40*'-')
reachable_n6 = n6.remove_nonreachable()
print('reachable DFA is')
print(40*'-')
print(reachable_n6)
print(40*'-')
minimal_n6 = reachable_n6.minimized1()
print()
print('Minimized DFA n6 is')
print(40*'-')
print(minimal_n6)
print(40*'-')

