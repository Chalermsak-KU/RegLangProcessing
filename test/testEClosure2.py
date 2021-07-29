from reglang import fa

delta1 = {   # an NFA
    (0, 'a'):{1},
    (0, '') :{2},
    (1, 'b'):{3},
    (1, '') :{0, 4},
    (2, 'a'):{1, 5},
    (2, 'b'):{2},
    (2, '') :{4},
    (3, '') :{4},
    (4, '') :{6},
    (5, 'a'):{5},
    (5, '') :{6},
}
m1 = fa.nfa(delta=delta1, start=0, finals={6})
dash40 = 40*'-'
print('NFA is as follows:')
print(dash40)
print(m1)
print(dash40)
for q in m1.states:
    closure = m1.ep_closure(q)
    print(f'E-closure of state {q} = {closure}')
print(dash40)
