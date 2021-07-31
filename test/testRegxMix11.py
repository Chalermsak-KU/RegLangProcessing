from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

x = regx('aUbUc')
print(f"NFA for regular expression 'aUbUc' with value '{x.val}' is")
print(x.nfa)
for s in ['a', 'b', 'c', '1', 'ab', 'cbaa', '']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('abc')
print(f"NFA for regular expression 'abc' with value '{x.val}' is")
print(x.nfa)
for s in ['a', 'b', 'c', 'ab', 'bc', 'abc', 'abcd', 'a12b', '']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('a**')
print(f"NFA for regular expression 'a**' with value '{x.val}' is")
print(x.nfa)
for s in ['', 'a', 'aa', 'aaa', 'aaaa', 'b', 'aaab', 'a12b']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

