import unittest
from contextlib import redirect_stdout
from reglang.nfa import nfa

class TestNfaToDfa(unittest.TestCase):

    def testNfaToDfa1(self):
        checkFileName = 'testNfaToDfa1' + '.good'
        outFileName = 'testNfaToDfa1' + '.out'

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
                
                n02 = m02.to_dfa()
                print('Equivalent DFA is as follows:')
                print(dash40)
                print(n02)
                print(dash40)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNfaToDfa2(self):
        checkFileName = 'testNfaToDfa2' + '.good'
        outFileName = 'testNfaToDfa2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta03 = {  # NFA ex.2.2.6 (a): L = (ab U aab U aba)*
                    (0, 'a'):{1},
                    (1, 'a'):{2},
                    (1, 'b'):{0, 3},
                    (2, 'b'):{0},
                    (3, 'a'):{0}
                }
                
                m03 = nfa(delta=delta03, start=0, finals={0})
                dash40 = 40*'-'
                print('NFA is as follows:')
                print(dash40)
                print(m03)
                print(dash40)
                
                n03 = m03.to_dfa()
                print('Equivalent DFA is as follows:')
                print(dash40)
                print(n03)
                print(dash40)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNfaToDfa3(self):
        checkFileName = 'testNfaToDfa3' + '.good'
        outFileName = 'testNfaToDfa3' + '.out'

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
                
                n04 = m04.to_dfa()
                print('Equivalent DFA is as follows:')
                print(dash40)
                print(n04)
                print(dash40)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNfaToDfa4(self):
        checkFileName = 'testNfaToDfa4' + '.good'
        outFileName = 'testNfaToDfa4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta05 = {  # another NFA for ex.2.2.6 (a): L = (ab U aab U aba)* 
                    (0, 'a'):{1, 2, 4},
                    (1, 'b'):{0},
                    (2, 'a'):{3},
                    (3, 'b'):{0},
                    (4, 'b'):{5},
                    (5, 'a'):{0}
                }
                
                m05 = nfa(delta=delta05, start=0, finals={0})
                dash40 = 40*'-'
                print('NFA is as follows:')
                print(dash40)
                print(m05)
                print(dash40)
                
                n05 = m05.to_dfa()
                print('Equivalent DFA is as follows:')
                print(dash40)
                print(n05)
                print(dash40)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNfaToDfa5(self):
        checkFileName = 'testNfaToDfa5' + '.good'
        outFileName = 'testNfaToDfa5' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta = {  # another NFA from lecture note about thm2.2.1
                    (0, 'a'):{1},
                    (0, 'b'):{0},
                    (0, '' ):{2},
                    (1, 'b'):{3},
                    (1, '' ):{0, 4},
                    (2, 'a'):{1},
                    (2, 'b'):{2, 5},
                    (2, '' ):{4},
                    (3, '' ):{4},
                    (4, 'a'):{4},
                    (4, '' ):{6},
                    (5, 'b'):{5},
                    (5, '' ):{6},
                    (6, 'a'):{6}
                }
                
                m = nfa(delta=delta, start=0, finals={3})
                dash40 = 40*'-'
                print('NFA is as follows:')
                print(dash40)
                print(m)
                print(dash40)
                
                n = m.to_dfa()
                print('Equivalent DFA is as follows:')
                print(dash40)
                print(n)
                print(dash40)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
