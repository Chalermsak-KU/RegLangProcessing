from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)
n = regx('@') # empty set
print(f"NFA for regular expression '{n.val}' is")
print(n.nfa)

aUn = a|n
print(f"NFA for regular expression 'aU@' with value '{aUn.val}' is")
print(aUn.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {aUn.val} : string '{s}' -> {aUn > s}")
print()

nUa = n|a
print(f"NFA for regular expression '@Ua' with value '{nUa.val}' is")
print(nUa.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {nUa.val} : string '{s}' -> {nUa > s}")
print()

nUn = n|n
print(f"NFA for regular expression '@U@' with value {nUn.val}' is")
print(nUn.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {nUn.val} : string '{s}' -> {nUn > s}")
print()

