import unittest
from contextlib import redirect_stdout
from reglang.nfa import nfa

class TestNfaAcpt(unittest.TestCase):

    def testNfaAcpt1(self):
        checkFileName = 'testNfaAcpt1' + '.good'
        outFileName = 'testNfaAcpt1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta_m2 = {   # an NFA p75 ex.2.2.9(a) L&P: language a*b(aUb)*
                    (0, 'a'):{0},
                    (0, 'b'):{0, 2},
                    (0, '') :{1},
                    (1, 'b'):{2, 4},
                    (2, 'a'):{3},
                    (3, '') :{4},
                    (4, 'a'):{3}
                }
                m2 = nfa(delta=delta_m2, start=0, finals={3, 4})
                print()
                print('NFA m2:')
                print(m2)
                for inpstr in ['b', 'bb', 'bba', 'ab', 'aba', 'aababaabb', 'a', 'aa', '']:
                    print('[accept version 1]')
                    print(f'NFA m2 {"accepts" if m2._accept0(inpstr) else "does not accept"} "{inpstr}"')
                    print('[accept version 2]')
                    print(f'NFA m2 {"accepts" if m2.accept(inpstr) else "does not accept"} "{inpstr}"')
                    print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNfaAcpt2(self):
        checkFileName = 'testNfaAcpt2' + '.good'
        outFileName = 'testNfaAcpt2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta_m3 = {   # NFA fig 2.9 p.70 L&P, language: (aa* U aa*b U b)(ep U (aUb)a*)
                    (0, 'b'):{2},
                    (0, '') :{1},
                    (1, 'a'):{0, 4},
                    (1, '') :{2, 3},
                    (2, 'b'):{4},
                    (3, 'a'):{4},
                    (4, '') :{3}
                }
                m3 = nfa(delta=delta_m3, start=0, finals={4})
                print()
                print('NFA m3 is as follows:')
                print(m3)
                print()
                for inpstr in ['', 'a', 'b', 'aab', 'aaba', 'aabba', 'aabbb', 'aabbabab']:
                    print('[accept version 1]')
                    print(f'NFA m3 {"accepts" if m3._accept0(inpstr) else "does not accept"} "{inpstr}"')
                    print('[accept version 2]')
                    print(f'NFA m3 {"accepts" if m3.accept(inpstr) else "does not accept"} "{inpstr}"')
                    print()
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNfaAcpt3(self):
        checkFileName = 'testNfaAcpt3' + '.good'
        outFileName = 'testNfaAcpt3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta_m4 = { # NFA ex.2.2.6 (a): L = (ab U aab U aba)*
                    (0, 'a'):{1},
                    (1, 'a'):{2},
                    (1, 'b'):{0, 3},
                    (2, 'b'):{0},
                    (3, 'a'):{0}
                }
                m4 = nfa(delta=delta_m4, start=0, finals={0})
                print()
                print('NFA m4 is as follows:')
                print(m4)
                print()
                tlist = ['', 'a', 'b', 'ab', 'aab', 'aba', 'bab', 'abab','abaa', 'abaaababab', 'abaaabb']
                for inpstr in tlist:
                    print('[accept version 1]')
                    print(f'NFA m4 {"accepts" if m4._accept0(inpstr) else "does not accept"} "{inpstr}"')
                    print('[accept version 2]')
                    print(f'NFA m4 {"accepts" if m4.accept(inpstr) else "does not accept"} "{inpstr}"')
                    print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
