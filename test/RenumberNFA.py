import unittest
from contextlib import redirect_stdout
from reglang.nfa import nfa

class TestRenumberNFA(unittest.TestCase):

    def testRenumberNFA1(self):
        checkFileName = 'testRenumberNFA1' + '.good'
        outFileName = 'testRenumberNFA1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta12 = {  # NFA example in the sheet (to be converted to regexp)
                    (1, 'a') : {1, 2},
                    (1, 'b') : {2},
                    (2, 'a') : {5},
                    (3, 'b') : {4},
                    (4, 'a') : {1},
                    (4, 'b') : {3},
                    (4, '')  : {2},
                    (5, 'b') : {4}
                }
                m12 = nfa(delta=delta12, start=1, finals={4, 5})
                print()
                print(f'current NFA m12 (starting at {1}):\n{m12}')
                
                stnum = 11
                n12 = m12.renumbered(startnum=stnum)
                print(f'new renumbered NFA n12 (starting at {stnum}):\n{n12}')
                
                stnum = 1
                nn12 = n12.renumbered(startnum=stnum)
                print(f'new renumbered NFA nn12 (starting at {stnum}):\n{nn12}')
                
                stnum = 101
                nnn12 = m12.renumbered(startnum=stnum)
                print(f'new renumbered NFA nnn12 (starting at {stnum}):\n{nnn12}')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
