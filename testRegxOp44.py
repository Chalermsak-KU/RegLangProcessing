from fa import *

e = regx('#') # empty string
print(f"NFA for regular expression '{e.val}' is")
print(e.nfa)
n = regx('@') # empty set
print(f"NFA for regular expression '{n.val}' is")
print(n.nfa)

en = e&n
print(f"NFA for regular expression '#@' with value '{en.val}' is")
print(en.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {en.val} : string '{s}' -> {en > s}")
print()

ne = n&e
print(f"NFA for regular expression '@#' with value '{ne.val}' is")
print(ne.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {ne.val} : string '{s}' -> {ne > s}")
print()

