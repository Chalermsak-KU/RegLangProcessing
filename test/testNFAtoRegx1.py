from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

delta9 = {  # NFA L&P p.81 (to convert to regexp)
    (1, 'a') : {1},
    (1, 'b') : {3},
    (2, 'a') : {2},
    (2, 'b') : {1},
    (3, 'a') : {3},
    (3, 'b') : {2}
}
m9 = nfa(delta=delta9, start=1, finals={3})
print()
print('NFA m9 is as follows:')
print(m9)
print()
n9 = m9.snfa()
print('simplified NFA for m9 is as follows:')
print(n9)
print()
r9recursive = m9.to_regx2()
print('[recursive algo]\nregexp is', r9recursive)
r9iterative = m9.to_regx()
print('\n[iterative algo]\nregexp is', r9iterative)

