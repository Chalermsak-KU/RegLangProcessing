from fa import *

a = regx('a')
for s in ['a', 'b', '1', '']:
    print(f"regx {a.val} : string '{s}' -> {a.gen(s)}")
print()

b = regx('b')
for s in ['a', 'b', '1', '']:
    print(f"regx {b.val} : string '{s}' -> {b.gen(s)}")
print()

e = regx('#') # represents the empty string
for s in ['a', 'b', '1', '']:
    print(f"regx {e.val} : string '{s}' -> {e.gen(s)}")
print()

n = regx('@') # represents the empty set
for s in ['a', 'b', '1', '']:
    print(f"regx {n.val} : string '{s}' -> {n.gen(s)}")
print()
