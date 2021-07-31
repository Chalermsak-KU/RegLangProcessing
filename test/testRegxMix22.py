from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

x = regx('aUbc')
for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('(aUb)c')
for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('aUb*c')
for s in ['a', 'b', 'c', 'bc', 'bbc', 'ac', '']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('a(bc)*')
for s in ['a', 'b', 'c', 'abc', 'abcbcbc', 'bc', 'acbbc', '']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

