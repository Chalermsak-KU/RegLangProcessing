import fa

delta = {   # a DFA that accepts (01 U 010)*
    (0, '0') : 1,
    (1, '1') : 2,
    (2, '0'): 3,
    (3, '0'): 1,
    (3, '1'): 2
}
dfa1 = fa.dfa(delta=delta, start=0, finals={0, 2, 3})
print('DFA that accepts (01 U 010)* is')
print(40*'-')
print(dfa1)
print(40*'-')
inputlist = ['0101001','010010010','01','010','','1010','010001','01101','010100100101']
for inpstr in inputlist:
    if dfa1.accept(inpstr):
        print(f"'{inpstr}' accepted")
    else:
        print(f"'{inpstr}' not accepted")

