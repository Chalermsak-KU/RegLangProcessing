from reglang.nfa import nfa

delta02 = {   # NFA fig 2.9 p.70 L&P
    (0, 'b'):{2},
    (0, '') :{1},
    (1, 'a'):{0, 4},
    (1, '') :{2, 3},
    (2, 'b'):{4},
    (3, 'a'):{4},
    (4, '') :{3}
}

m02 = nfa(delta=delta02, start=0, finals={4})
dash40 = 40*'-'
print('NFA is as follows:')
print(dash40)
print(m02)
print(dash40)

n02 = m02.to_dfa()
print('Equivalent DFA is as follows:')
print(dash40)
print(n02)
print(dash40)
