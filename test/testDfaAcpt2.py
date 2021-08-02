from reglang.dfa import dfa

delta = {   # a DFA that accepts the empty set
}
dfa1 = dfa(delta=delta, start='s', finals={'f'})
print('DFA that accepts the empty set is')
print(40*'-')
print(dfa1)
print(40*'-')

inputlist = ['', '0', '00', '000', '0000']
for inpstr in inputlist:
    if dfa1.accept(inpstr):
        print(f"'{inpstr}' accepted")
    else:
        print(f"'{inpstr}' not accepted")

