from reglang.regx import regx

a = regx('a')
b = regx('b')
c = regx('c')
e = regx('#')
i = regx('1')
o = regx('0')

no_ac = c.star() & (a | b&c.star()).star()
print(f"NFA for regular expression 'c*&(a|b&c*)*' with value '{no_ac.val}' is")
for s in ['', 'a', 'b', 'ccc', 'abcccaabc', 'ac', 'babcacc']:
    print(f"regx {no_ac.val} : string '{s}' -> {no_ac > s}")
print()

no111 = (e|i|i&i)&(o|o&i|o&i&i).star()
print(f"NFA for regular expression '(#|1|11)(0|01|011)*' with value '{no111.val}' is")
for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
    print(f"regx {no111.val} : string '{s}' -> {no111 > s}")
print()

x = b.star()|(b.star()&a&b.star()&a&b.star()&a&b.star()).star() # no.of a's divisible by 3
print(f"NFA for regular expression 'b*|(b*ab*ab*ab*)*' with value '{x.val}' is")
for s in ['', 'ab', 'baabbab', 'bbaa', 'aaa', 'aababbbaaab', 'aaaabaaaaa', 'babaabaa']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

no111 = o.star() | o.star()&(i|i&i)&(o&o.star()&(i|i&i)).star()&o.star()
print(f"NFA for regular expression '0*U0*(1U11)(00*(1U11))*0*' with value '{no111.val}' is")
for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
    print(f"regx {no111.val} : string '{s}' -> {no111 > s}")
print()
