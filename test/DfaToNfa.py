import unittest
from contextlib import redirect_stdout
from reglang.dfa import dfa

class TestDfaToNfa(unittest.TestCase):

    def testDfaToNfa1(self):
        checkFileName = 'testDfaToNfa1' + '.good'
        outFileName = 'testDfaToNfa1' + '.out'

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
                nfa1 = dfa1.to_nfa()
                print('Equivalent NFA is')
                print(40*'-')
                print(nfa1)
                print(40*'-')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDfaToNfa2(self):
        checkFileName = 'testDfaToNfa2' + '.good'
        outFileName = 'testDfaToNfa2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta = {   # a DFA that accepts the empty set
                }
                dfa1 = dfa(delta=delta, start='s', finals={'f'})
                print('DFA that accepts the empty set is')
                print(40*'-')
                print(dfa1)
                print(40*'-')
                nfa1 = dfa1.to_nfa()
                print('Equivalent NFA is')
                print(40*'-')
                print(nfa1)
                print(40*'-')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDfaToNfa3(self):
        checkFileName = 'testDfaToNfa3' + '.good'
        outFileName = 'testDfaToNfa3' + '.out'

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
                nfa1 = dfa1.to_nfa()
                print('Equivalent NFA is')
                print(40*'-')
                print(nfa1)
                print(40*'-')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
