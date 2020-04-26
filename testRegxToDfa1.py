import fa

rstr = 'c*(aUbc*)*'
r = fa.regx(rstr)
m = r.to_dfa()
print(f'Regular expression is {rstr}')
print(f'Resulting DFA is')
print(m)

