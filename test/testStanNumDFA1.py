from reglang.dfa import dfa

delta_n1 = {  # DFA p.94 L&P (for minimization algo in L&P)
    ('one', 'a') : 'two',
    ('one', 'b') : 'four',
    ('two', 'a') : 'five',
    ('two', 'b') : 'three',
    ('three', 'a') : 'two',
    ('three', 'b') : 'six',
    ('four', 'a') : 'one',
    ('four', 'b') : 'five',
    ('five', 'a') : 'five',
    ('five', 'b') : 'five',
    ('six', 'a') : 'three',
    ('six', 'b') : 'five'
}

n1 = dfa(delta=delta_n1, start='one', finals={'one', 'three'})
print('Original DFA is')
print(40*'-')
print(f'current DFA n1:\n{n1}')

m1 = n1.standard_numbered()
print(40*'-')
print(f'Standard-numbered DFA m1:\n{m1}')

m2 = m1.standard_numbered()
print(40*'-')
print(f'Standard-numbered DFA m2:\n{m2}')

