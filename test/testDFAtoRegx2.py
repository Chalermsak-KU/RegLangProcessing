from reglang import fa

delta = {   # a DFA that accepts the empty set
}
dfa1 = fa.dfa(delta=delta, start='s', finals={'f'})
print('DFA that accepts the empty set is')
print(40*'-')
print(dfa1)
print(40*'-')
r = dfa1.to_regx()
print('Corresponding regular expression is')
print(r)
