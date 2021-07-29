from reglang import fa

rstr = '(0U1)*111(0U1)*'
r = fa.regx(rstr)
m = r.to_dfa()
print(f'Regular expression is {rstr}')
print(f'Resulting DFA is')
print(m)

