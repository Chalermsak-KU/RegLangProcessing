from reglang.dfa import dfa

#-----------------------#
delta = {  # DFA p.94 L&P (for minimization algo)
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
dfa1 = dfa(delta=delta, start=1, finals={1, 3})
print('DFA that accepts (ab U ba)* is')
print(40*'-')
print(dfa1)
print(40*'-')
r = dfa1.to_regx()
print('Corresponding regular expression is')
print(r)
