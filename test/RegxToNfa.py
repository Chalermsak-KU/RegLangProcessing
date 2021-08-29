import unittest
from contextlib import redirect_stdout
from reglang.regx import regx

class TestRegxToNfa(unittest.TestCase):

    def testRegxToNfa1(self):
        checkFileName = 'testRegxToNfa1' + '.good'
        outFileName = 'testRegxToNfa1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                x = regx('aU(bc)*')
                n1 = x.nfa
                print(f'Attached NFA is')
                print(n1)
                n2 = x.to_nfa()
                print(f'Obtained NFA is')
                print(x.to_nfa())
                if id(n1) == id(n2):
                    print('Two NFAs are the same object')
                else:
                    print('Two NFAs are different objects')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
