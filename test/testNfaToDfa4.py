from reglang.nfa import nfa

delta05 = {  # another NFA for ex.2.2.6 (a): L = (ab U aab U aba)* 
    (0, 'a'):{1, 2, 4},
    (1, 'b'):{0},
    (2, 'a'):{3},
    (3, 'b'):{0},
    (4, 'b'):{5},
    (5, 'a'):{0}
}

m05 = nfa(delta=delta05, start=0, finals={0})
dash40 = 40*'-'
print('NFA is as follows:')
print(dash40)
print(m05)
print(dash40)

n05 = m05.to_dfa()
print('Equivalent DFA is as follows:')
print(dash40)
print(n05)
print(dash40)
