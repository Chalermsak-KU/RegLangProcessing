from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

e = regx('#') # empty string
print(f"NFA for regular expression '{e.val}' is")
print(e.nfa)
n = regx('@') # empty set
print(f"NFA for regular expression '{n.val}' is")
print(n.nfa)

eUn = e|n
print(f"NFA for regular expression '#U@' with value '{eUn.val}' is")
print(eUn.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {eUn.val} : string '{s}' -> {eUn > s}")
print()

nUe = n|e
print(f"NFA for regular expression '@U#' with value '{nUe.val}' is")
print(nUe.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {nUe.val} : string '{s}' -> {nUe > s}")
print()

