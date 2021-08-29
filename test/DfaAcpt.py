import unittest
from contextlib import redirect_stdout
from reglang.dfa import dfa

class TestDfaAcpt(unittest.TestCase):

    def testDfaAcpt1(self):
        checkFileName = 'testDfaAcpt1' + '.good'
        outFileName = 'testDfaAcpt1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
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
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDfaAcpt2(self):
        checkFileName = 'testDfaAcpt2' + '.good'
        outFileName = 'testDfaAcpt2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta = {   # a DFA that accepts the empty set
                }
                dfa1 = dfa(delta=delta, start='s', finals={'f'})
                print('DFA that accepts the empty set is')
                print(40*'-')
                print(dfa1)
                print(40*'-')
                
                inputlist = ['', '0', '00', '000', '0000']
                for inpstr in inputlist:
                    if dfa1.accept(inpstr):
                        print(f"'{inpstr}' accepted")
                    else:
                        print(f"'{inpstr}' not accepted")
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDfaAcpt3(self):
        checkFileName = 'testDfaAcpt3' + '.good'
        outFileName = 'testDfaAcpt3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                #-----------------------#
                delta = {  # DFA p.94 L&P (for minimization algo)
                    (1, 'a') : 2,
                    (1, 'b') : 4,
                    (2, 'a') : 5,
                    (2, 'b') : 3,
                    (3, 'a') : 2,
                    (3, 'b') : 6,
                    (4, 'a') : 1,
                    (4, 'b') : 5,
                    (5, 'a') : 5,
                    (5, 'b') : 5,
                    (6, 'a') : 3,
                    (6, 'b') : 5
                }
                dfa1 = dfa(delta=delta, start=1, finals={1, 3})
                print('DFA that accepts (ab U ba)* is')
                print(40*'-')
                print(dfa1)
                print(40*'-')
                
                inputlist = ['', 'a', 'b', 'ab', 'ba', 'abbabaab', 'abaaba', 'bababa', 'babbab']
                for inpstr in inputlist:
                    if dfa1.accept(inpstr):
                        print(f"'{inpstr}' accepted")
                    else:
                        print(f"'{inpstr}' not accepted")
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDfaAcpt4(self):
        checkFileName = 'testDfaAcpt4' + '.good'
        outFileName = 'testDfaAcpt4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta = {   # a DFA that accepts (01 U 010)*
                    (0, '0') : 1,
                    (1, '1') : 2,
                    (2, '0'): 3,
                    (3, '0'): 1,
                    (3, '1'): 2
                }
                dfa1 = dfa(delta=delta, start=0, finals={0, 2, 3})
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
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
