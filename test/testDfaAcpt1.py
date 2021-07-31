from reglang.dfa import dfa
from reglang.nfa import nfa
from reglang.regx import regx

delta = {   # a DFA that accepts (01 U 010)*
    ('s', '0') : '0',
    ('0', '1') : '01',
    ('01', '0'): '010',
    ('010', '0'): '0',
    ('010', '1'): '01'
}
dfa1 = dfa(delta=delta, start='s', finals={'s', '01', '010'})
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

