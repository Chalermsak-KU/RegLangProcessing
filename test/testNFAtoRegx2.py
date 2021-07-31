from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

delta10 = {  # NFA L&P exercise 2.3.7a (to convert to regexp)
    (1, 'a') : {1},
    (1, 'b') : {2},
    (2, 'a') : {2},
    (2, 'b') : {1}
}
m10 = nfa(delta=delta10, start=1, finals={2})

print()
print('NFA m10 is as follows:')
print(m10)
print()
n10 = m10.snfa()
print('simplified NFA for m10 is as follows:')
print(n10)
print()
r10recursive = m10.to_regx2()
print('[recursive algo]\nregexp is', r10recursive)
r10iterative = m10.to_regx()
print('\n[iterative algo]\nregexp is', r10iterative)

