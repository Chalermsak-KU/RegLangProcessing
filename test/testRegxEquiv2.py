from reglang import fa

# r1 is the regx of {w in {0,1}*: w has no substring 111}
r1 = fa.regx('0* U 0*(1U11)(00*(1U11))*0*')
r2 = fa.regx('(#U1U11)(0U01U011)*')
r3 = fa.regx('(0U10U110)*(#U1U11)')
print(r1, '==', r2, 'is', r1 == r2)
print(r1, '==', r3, 'is', r1 == r3)
print(r2, '==', r3, 'is', r2 == r3)

r4 = fa.regx('(1U11)(0U01U011)*')
print(r1, '==', r4, 'is', r1 == r4)
print(r2, '==', r4, 'is', r2 == r4)
print(r3, '==', r4, 'is', r3 == r4)

