import fa 

delta_n1 = {  # DFA p.94 L&P (for minimization algo in L&P)
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

n1 = fa.dfa(delta=delta_n1, start=1, finals={1, 3})
print('Original DFA is')
print(40*'-')
print(f'current DFA n1 (starting at {1}):\n{n1}')

stnum = 11
m11 = n1.renumbered(startnum=stnum)
print(40*'-')
print(f'new renumbered DFA m11 (starting at {stnum}):\n{m11}')

stnum = 1
m1 = n1.renumbered(startnum=stnum)
print(40*'-')
print(f'new renumbered DFA m1 (starting at {stnum}):\n{m1}')

stnum = 101
m101 = n1.renumbered(startnum=stnum)
print(40*'-')
print(f'new renumbered DFA m101 (starting at {stnum}):\n{m101}')

