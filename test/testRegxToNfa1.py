from reglang.regx import regx

x = regx('aU(bc)*')
n1 = x.nfa
print(f'Attached NFA is')
print(n1)
n2 = x.to_nfa()
print(f'Obtained NFA is')
print(x.to_nfa())
if id(n1) == id(n2):
    print('Two NFAs are the same object')
else:
    print('Two NFAs are different objects')

