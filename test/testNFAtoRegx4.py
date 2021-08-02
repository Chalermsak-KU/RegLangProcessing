from reglang.nfa import nfa

delta12 = {  # NFA example in the sheet (to convert to regexp)
    (1, 'a') : {1, 2},
    (1, 'b') : {2},
    (2, 'a') : {5},
    (3, 'b') : {4},
    (4, 'a') : {1},
    (4, 'b') : {3},
    (4, '')  : {2},
    (5, 'b') : {4}
}
m12 = nfa(delta=delta12, start=1, finals={4, 5})
print()
print('NFA m12 is as follows:')
print(m12)
print()
n12 = m12.snfa()
print('simplified NFA for m12 is as follows:')
print(n12)
print()
r12recursive = m12.to_regx2()
print('[recursive algo]\nregexp is', r12recursive)
r12iterative = m12.to_regx()
print('\n[iterative algo]\nregexp is', r12iterative)

