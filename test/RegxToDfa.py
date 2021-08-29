import unittest
from contextlib import redirect_stdout
from reglang.regx import regx

class TestRegxToDfa(unittest.TestCase):

    def testRegxToDfa1(self):
        checkFileName = 'testRegxToDfa1' + '.good'
        outFileName = 'testRegxToDfa1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                rstr = 'c*(aUbc*)*'
                r = regx(rstr)
                m = r.to_dfa()
                print(f'Regular expression is {rstr}')
                print(f'Resulting DFA is')
                print(m)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxToDfa2(self):
        checkFileName = 'testRegxToDfa2' + '.good'
        outFileName = 'testRegxToDfa2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                rstr = '(0U1)*111(0U1)*'
                r = regx(rstr)
                m = r.to_dfa()
                print(f'Regular expression is {rstr}')
                print(f'Resulting DFA is')
                print(m)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxToDfa3(self):
        checkFileName = 'testRegxToDfa3' + '.good'
        outFileName = 'testRegxToDfa3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                rstr = '#'
                r = regx(rstr)
                m = r.to_dfa()
                print(f'Regular expression is {rstr}')
                print(f'Resulting DFA is')
                print(m)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxToDfa4(self):
        checkFileName = 'testRegxToDfa4' + '.good'
        outFileName = 'testRegxToDfa4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                rstr = '@'
                r = regx(rstr)
                m = r.to_dfa()
                print(f'Regular expression is {rstr}')
                print(f'Resulting DFA is')
                print(m)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
