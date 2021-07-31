from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

a = regx('a')
b = regx('b')
c = regx('c')

aU_bc_STAR = a|(b&c).star()
print(f"NFA for regular expression 'a|(b&c).star()' with value '{aU_bc_STAR.val}' is")
for s in ['a', '', 'bc', 'bcbc', 'abc', 'bcc', 'ac']:
    print(f"regx {aU_bc_STAR.val} : string '{s}' -> {aU_bc_STAR > s}")
print()

_aUb_STARc = (a|b).star()&c
print(f"NFA for regular expression '(a|b).star()&c' with value '{_aUb_STARc.val}' is")
for s in ['', 'c', 'ac', 'bc', 'abbac', 'aab', 'cab']:
    print(f"regx {_aUb_STARc.val} : string '{s}' -> {_aUb_STARc > s}")
print()

aUbc_STAR = (a|b&c).star()
print(f"NFA for regular expression '(a|b&c).star()' with value '{aUbc_STAR.val}' is")
for s in ['', 'a', 'bc', 'bcbc', 'aaa', 'bcabcaa', 'aabc', 'cb', 'acbc']:
    print(f"regx {aUbc_STAR.val} : string '{s}' -> {aUbc_STAR > s}")
print()
