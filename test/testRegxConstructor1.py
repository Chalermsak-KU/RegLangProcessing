from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)

b = regx('b')
print(f"NFA for regular expression '{b.val}' is")
print(b.nfa)

e = regx('#') # represents the empty string
print(f"NFA for regular expression '{e.val}' (empty string) is")
print(e.nfa)

n = regx('@') # represents the empty set
print(f"NFA for regular expression '{n.val}' (empty set) is")
print(n.nfa)

