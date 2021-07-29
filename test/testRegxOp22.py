from reglang.fa import *

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)
e = regx('#') # represents the empty string
print(f"NFA for regular expression '{e.val}' is")
print(e.nfa)

ae = a&e
print(f"NFA for regular expression a# with value '{ae.val}' is")
print(ae.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {ae.val} : string '{s}' -> {ae > s}")
print()

ea = e&a
print(f"NFA for regular expression #a with value '{ea.val}' is")
print(ea.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {ea.val} : string '{s}' -> {ea > s}")
print()

ee = e&e
print(f"NFA for regular expression ## with value '{ee.val}' is")
print(ee.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {ee.val} : string '{s}' -> {ee > s}")
print()

