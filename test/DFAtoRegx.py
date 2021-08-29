import unittest
from contextlib import redirect_stdout
from reglang.dfa import dfa

class TestDFAtoRegx(unittest.TestCase):

    def testDFAtoRegx1(self):
        checkFileName = 'testDFAtoRegx1' + '.good'
        outFileName = 'testDFAtoRegx1' + '.out'

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
                r = dfa1.to_regx()
                print('Corresponding regular expression is')
                print(r)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDFAtoRegx2(self):
        checkFileName = 'testDFAtoRegx2' + '.good'
        outFileName = 'testDFAtoRegx2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta = {   # a DFA that accepts the empty set
                }
                dfa1 = dfa(delta=delta, start='s', finals={'f'})
                print('DFA that accepts the empty set is')
                print(40*'-')
                print(dfa1)
                print(40*'-')
                r = dfa1.to_regx()
                print('Corresponding regular expression is')
                print(r)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDFAtoRegx3(self):
        checkFileName = 'testDFAtoRegx3' + '.good'
        outFileName = 'testDFAtoRegx3' + '.out'

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
                r = dfa1.to_regx()
                print('Corresponding regular expression is')
                print(r)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDFAtoRegx4(self):
        checkFileName = 'testDFAtoRegx4' + '.good'
        outFileName = 'testDFAtoRegx4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                #-----------------------#
                delta = {  # DFA p.100 L&P
                    (1, 'a') : 2,
                    (1, 'b') : 3,
                    (2, 'a') : 4,
                    (2, 'b') : 1,
                    (3, 'a') : 1,
                    (3, 'b') : 4,
                    (4, 'a') : 4,
                    (4, 'b') : 4
                }
                dfa1 = dfa(delta=delta, start=1, finals={1})
                print('DFA that accepts (ab U ba)* is')
                print(40*'-')
                print(dfa1)
                print(40*'-')
                r = dfa1.to_regx()
                print('Corresponding regular expression is')
                print(r)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
