from reglang import fa

delta = {   # a DFA that accepts (01 U 010)*
    ('s', '0') : '0',
    ('0', '1') : '01',
    ('01', '0'): '010',
    ('010', '0'): '0',
    ('010', '1'): '01'
}
dfa1 = fa.dfa(delta=delta, start='s', finals={'s', '01', '010'})
print('DFA that accepts (01 U 010)* is')
print(40*'-')
print(dfa1)
print(40*'-')
nfa1 = dfa1.to_nfa()
print('Equivalent NFA is')
print(40*'-')
print(nfa1)
print(40*'-')
