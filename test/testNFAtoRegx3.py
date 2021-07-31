from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

delta11 = {  # NFA L&P exercise 2.3.7d (to convert to regexp)
    (1, 'a') : {2},
    (1, 'b') : {4},
    (2, 'b') : {3, 4},
    (3, 'a') : {3},
    (3, 'b') : {3},
    (4, 'a') : {2, 4}
}
m11 = nfa(delta=delta11, start=1, finals={3})
print()
print('NFA m11 is as follows:')
print(m11)
print()
n11 = m11.snfa()
print('simplified NFA for m11 is as follows:')
print(n11)
print()
r11recursive = m11.to_regx2()
print('[recursive algo]\nregexp is', r11recursive)
r11iterative = m11.to_regx()
print('\n[iterative algo]\nregexp is', r11iterative)

