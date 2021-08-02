from reglang.dfa import dfa
from reglang.regx import regx

r1 = regx('c*(aUbc*)*')
print(f'r1 is {r1}')

del11 = {
    (1,'a'): 2,
    (1,'b'): 1,
    (1,'c'): 1,
    (2,'a'): 2,
    (2,'b'): 1,
    (2,'c'): 3,
    (3,'a'): 3,
    (3,'b'): 3,
    (3,'c'): 3
}
d11 = dfa(delta=del11, start=1, finals={1,2})
print(f'DFA d11 is')
print(40*'-')
print(d11)
print(40*'-')
r11 = d11.to_regx()
print(f'r11 is {r11}')
print(f'r1.equiv(r11) is {r1.equiv(r11)}')
print(r1, '==', r11, 'is', r1 == r11)
print(40*'-')
r2 = regx('(#Ucc*)(aUb(c*cU#))*')
print(f'r2 is {r2}')
print(f'r1.equiv(r2) is {r1.equiv(r2)}')
print(r1, '==', r2, 'is', r1 == r2)
print(f'r11.equiv(r2) is {r11.equiv(r2)}')
print(r11, '==', r2, 'is', r11 == r2)
print(40*'-')
r3 = regx('(#Ucc*)(aUbc*c)*')
print(f'r3 is {r3}')
print(f'r1.equiv(r3) is {r1.equiv(r3)}')
print(r1, '==', r3, 'is', r1 == r3)
print(f'r11.equiv(r3) is {r11.equiv(r3)}')
print(r11, '==', r3, 'is', r11 == r3)
