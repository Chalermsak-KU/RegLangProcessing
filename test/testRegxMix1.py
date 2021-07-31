from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

a = regx('a')
b = regx('b')
c = regx('c')

aUbUc = a|b|c
print(f"NFA for regular expression 'a|b|c' with value '{aUbUc.val}' is")
print(aUbUc.nfa)
for s in ['a', 'b', 'c', '1', 'ab', 'cbaa', '']:
    print(f"regx {aUbUc.val} : string '{s}' -> {aUbUc > s}")
print()

abc = a&b&c
print(f"NFA for regular expression 'a&b&c' with value '{abc.val}' is")
print(abc.nfa)
for s in ['a', 'b', 'c', 'ab', 'bc', 'abc', 'abcd', 'a12b', '']:
    print(f"regx {abc.val} : string '{s}' -> {abc > s}")
print()

ass = a.star().star()
print(f"NFA for regular expression 'a.star().star()' with value '{ass.val}' is")
print(ass.nfa)
for s in ['', 'a', 'aa', 'aaa', 'aaaa', 'b', 'aaab', 'a12b']:
    print(f"regx {ass.val} : string '{s}' -> {ass > s}")
print()

