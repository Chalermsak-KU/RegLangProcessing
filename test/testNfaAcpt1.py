from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

delta_m2 = {   # an NFA p75 ex.2.2.9(a) L&P: language a*b(aUb)*
    (0, 'a'):{0},
    (0, 'b'):{0, 2},
    (0, '') :{1},
    (1, 'b'):{2, 4},
    (2, 'a'):{3},
    (3, '') :{4},
    (4, 'a'):{3}
}
m2 = nfa(delta=delta_m2, start=0, finals={3, 4})
print()
print('NFA m2:')
print(m2)
for inpstr in ['b', 'bb', 'bba', 'ab', 'aba', 'aababaabb', 'a', 'aa', '']:
    print('[accept version 1]')
    print(f'NFA m2 {"accepts" if m2._accept0(inpstr) else "does not accept"} "{inpstr}"')
    print('[accept version 2]')
    print(f'NFA m2 {"accepts" if m2.accept(inpstr) else "does not accept"} "{inpstr}"')
    print()

