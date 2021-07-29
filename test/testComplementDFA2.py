from reglang import fa

delta = {   # a DFA that accepts the empty set
}
dfa1 = fa.dfa(delta=delta, start='s', finals={'f'})
print('DFA that accepts the empty set is')
print(40*'-')
print(dfa1)
print(40*'-')
dfa2 = dfa1.complement()
print('Complemented DFA is')
print(40*'-')
print(dfa2)
print(40*'-')
