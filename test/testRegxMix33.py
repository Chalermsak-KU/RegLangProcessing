from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

x = regx('aU(bc)*')
for s in ['a', '', 'bc', 'bcbc', 'abc', 'bcc', 'ac']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('(aUb)*c')
for s in ['', 'c', 'ac', 'bc', 'abbac', 'aab', 'cab']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('(aUbc)*')
for s in ['', 'a', 'bc', 'bcbc', 'aaa', 'bcabcaa', 'aabc', 'cb', 'acbc']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()
