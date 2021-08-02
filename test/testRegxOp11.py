from reglang.regx import regx

a = regx('a')
print(f"NFA for regular expression '{a.val}' is")
print(a.nfa)
b = regx('b')
print(f"NFA for regular expression '{b.val}' is")
print(b.nfa)
ab = a&b
print(f"NFA for regular expression 'a&b' with value '{ab.val}' is")
print(ab.nfa)

for s in ['a', 'b', '1', 'ab', 'ba', 'ab12', '']:
    print(f"regx {ab.val} : string '{s}' -> {ab > s}")
print()

