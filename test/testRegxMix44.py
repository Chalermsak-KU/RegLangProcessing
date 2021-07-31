from reglang.dfa import *
from reglang.nfa import *
from reglang.regx import *

x = regx('c*(aUbc*)*')
for s in ['', 'a', 'b', 'ccc', 'abcccaabc', 'ac', 'babcacc']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('(#U1U11)(0U01U011)*')
for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('b* U (b*ab*ab*ab*)*') # no.of a's divisible by 3
for s in ['', 'ab', 'baabbab', 'bbaa', 'aaa', 'aababbbaaab', 'aaaabaaaaa', 'babaabaa']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

x = regx('0* U 0*(1U11)(00*(1U11))*0*') 
for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
    print(f"regx {x.val} : string '{s}' -> {x > s}")
print()

