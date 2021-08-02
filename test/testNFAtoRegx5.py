from reglang.nfa import nfa

delta = {  # NFA example in Kleene's Thm-2 slides  (to convert to regexp)
    (1, 'a') : {2},
    (1, 'b') : {1, 3},
    (2, 'a') : {3},
    (3, 'a') : {3},
    (3, 'b') : {3},
    (3, '')  : {4},
    (4, 'a') : {2},
    (4, 'b') : {2, 4}
}
m = nfa(delta=delta, start=1, finals={2, 4})
print()
print('NFA m is as follows:')
print(m)
print()
n = m.snfa()
print('simplified NFA for m is as follows:')
print(n)
print()
r_recursive = m.to_regx2()
print('[recursive algo]\nregexp is', r_recursive)
r_iterative = m.to_regx()
print('\n[iterative algo]\nregexp is', r_iterative)

