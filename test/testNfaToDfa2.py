from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

delta03 = {  # NFA ex.2.2.6 (a): L = (ab U aab U aba)*
    (0, 'a'):{1},
    (1, 'a'):{2},
    (1, 'b'):{0, 3},
    (2, 'b'):{0},
    (3, 'a'):{0}
}

m03 = nfa(delta=delta03, start=0, finals={0})
dash40 = 40*'-'
print('NFA is as follows:')
print(dash40)
print(m03)
print(dash40)

n03 = m03.to_dfa()
print('Equivalent DFA is as follows:')
print(dash40)
print(n03)
print(dash40)
