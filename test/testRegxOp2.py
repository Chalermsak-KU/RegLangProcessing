from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)
e = regx('#') # represents the empty string
print(f"NFA for regular expression '{e.val}' is")
print(e.nfa)

aUe = a|e
print(f"NFA for regular expression '{aUe.val}' is")
print(aUe.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {aUe.val} : string '{s}' -> {aUe > s}")
print()

eUa = e|a
print(f"NFA for regular expression '{eUa.val}' is")
print(eUa.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {eUa.val} : string '{s}' -> {eUa > s}")
print()

eUe = e|e
print(f"NFA for regular expression '{eUe.val}' is")
print(eUe.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {eUe.val} : string '{s}' -> {eUe > s}")
print()
