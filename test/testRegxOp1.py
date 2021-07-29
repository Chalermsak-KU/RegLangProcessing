from reglang.fa import *

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)
b = regx('b')
print(f"NFA for regular expression '{b.val}' is")
print(b.nfa)
aUb = a|b
print(f"NFA for regular expression '{aUb.val}' is")
print(aUb.nfa)

for s in ['a', 'b', '1', 'ba', '12a', '']:
    print(f"regx {aUb.val} : string '{s}' -> {aUb > s}")
print()

