from fa import *

a = regx('a')
b = regx('b')
c = regx('c')

aUbc = a|b&c
print(f"NFA for regular expression 'a|b&c' with value '{aUbc.val}' is")
for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
    print(f"regx {aUbc.val} : string '{s}' -> {aUbc > s}")
print()

aUb_c = (a|b)&c
print(f"NFA for regular expression '(a|b)&c' with value '{aUb_c.val}' is")
for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
    print(f"regx {aUb_c.val} : string '{s}' -> {aUb_c > s}")
print()

aUbSTARc = a|b.star()&c
print(f"NFA for regular expression 'a|b.star()&c' with value '{aUbSTARc.val}' is")
for s in ['a', 'b', 'c', 'bc', 'bbc', 'ac', '']:
    print(f"regx {aUbSTARc.val} : string '{s}' -> {aUbSTARc > s}")
print()

x = a&(b&c).star()
print(f"NFA for regular expression 'a&(b&c).star()' with value '{x.val}' is")
for s in ['a', 'b', 'c', 'abc', 'abcbcbc', 'bc', 'acbbc', '']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

