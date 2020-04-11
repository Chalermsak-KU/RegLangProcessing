from fa import *

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)
n = regx('@') # empty set
print(f"NFA for regular expression '{n.val}' is")
print(n.nfa)

an = a&n
print(f"NFA for regular expression 'a@' with value '{an.val}' is")
print(an.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {an.val} : string '{s}' -> {an > s}")
print()

na = n&a
print(f"NFA for regular expression '@a' with value '{na.val}' is")
print(na.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {na.val} : string '{s}' -> {na > s}")
print()

nn = n&n
print(f"NFA for regular expression '@@' with value {nn.val}' is")
print(nn.nfa)
for s in ['a', 'b', 'aa', '12a', '']:
    print(f"regx {nn.val} : string '{s}' -> {nn > s}")
print()

