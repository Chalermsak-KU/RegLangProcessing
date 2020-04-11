import fa

#-----------------------#
delta = {  # DFA p.100 L&P
    (1, 'a') : 2,
    (1, 'b') : 3,
    (2, 'a') : 4,
    (2, 'b') : 1,
    (3, 'a') : 1,
    (3, 'b') : 4,
    (4, 'a') : 4,
    (4, 'b') : 4
}
dfa1 = fa.dfa(delta=delta, start=1, finals={1})
print('DFA that accepts (ab U ba)* is')
print(40*'-')
print(dfa1)
print(40*'-')
r = dfa1.to_regx()
print('Corresponding regular expression is')
print(r)
