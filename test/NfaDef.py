import unittest
from contextlib import redirect_stdout
from reglang.nfa import nfa

class TestNfaDef(unittest.TestCase):

    def testNfaDef1(self):
        checkFileName = 'testNfaDef1' + '.good'
        outFileName = 'testNfaDef1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta02 = {   # NFA fig 2.9 p.70 L&P
                    (0, 'b'):{2},
                    (0, '') :{1},
                    (1, 'a'):{0, 4},
                    (1, '') :{2, 3},
                    (2, 'b'):{4},
                    (3, 'a'):{4},
                    (4, '') :{3}
                }
                
                m02 = nfa(delta=delta02, start=0, finals={4})
                dash40 = 40*'-'
                print('NFA is as follows:')
                print(dash40)
                print(m02)
                print(dash40)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNfaDef2(self):
        checkFileName = 'testNfaDef2' + '.good'
        outFileName = 'testNfaDef2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta04 = { # an NFA p75 ex.2.2.9(a) L&P: language a*b(aUb)*
                    (0, 'a'):{0},
                    (0, 'b'):{0, 2},
                    (0, '') :{1},
                    (1, 'b'):{2, 4},
                    (2, 'a'):{3},
                    (3, '') :{4},
                    (4, 'a'):{3}
                }
                
                m04 = nfa(delta=delta04, start=0, finals={3, 4})
                dash40 = 40*'-'
                print('NFA is as follows:')
                print(dash40)
                print(m04)
                print(dash40)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
