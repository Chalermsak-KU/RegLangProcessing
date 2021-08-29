import unittest
from contextlib import redirect_stdout
from reglang.dfa import dfa

class TestDfaDef(unittest.TestCase):

    def testDfaDef1(self):
        checkFileName = 'testDfaDef1' + '.good'
        outFileName = 'testDfaDef1' + '.out'
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

        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testDfaDef2(self):
        checkFileName = 'testDfaDef2' + '.good'
        outFileName = 'testDfaDef2' + '.out'
        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta = {   # a DFA that accepts the empty set
                }
                dfa1 = dfa(delta=delta, start='s', finals={'f'})
                print('DFA that accepts the empty set is')
                print(40*'-')
                print(dfa1)
                print(40*'-')

        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
