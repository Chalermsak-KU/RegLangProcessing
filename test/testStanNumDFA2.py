from reglang import fa 

delta_n1 = {  # DFA p.93 L&P (for minimization algo in L&P)
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
    ('six', 'b') : 'five',
    ('seven', 'a') : 'six',
    ('seven', 'b') : 'eight',
    ('eight', 'a') : 'seven',
    ('eight', 'b') : 'three'
}

n1 = fa.dfa(delta=delta_n1, start='one', finals={'one', 'three'})
print('Original DFA is')
print(40*'-')
print(f'current DFA n1:\n{n1}')

m1 = n1.standard_numbered()
print(40*'-')
print(f'Standard-numbered DFA m1:\n{m1}')

