import unittest
from contextlib import redirect_stdout
from reglang.dfa import dfa
from reglang.nfa import nfa

class TestMinDFA(unittest.TestCase):

    def testMinDFA1(self):
        checkFileName = 'testMinDFA1' + '.good'
        outFileName = 'testMinDFA1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                #-----------------------#
                delta_n5 = {  # DFA p.94 L&P (for minimization algo in L&P)
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
                
                n5 = dfa(delta=delta_n5, start=1, finals={1, 3})
                print('Original DFA is')
                print(40*'-')
                print(n5)
                print(40*'-')
                minimal_n5 = n5.minimized1()
                print('Minimized DFA is')
                print(40*'-')
                print(minimal_n5)
                print(40*'-')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testMinDFA2(self):
        checkFileName = 'testMinDFA2' + '.good'
        outFileName = 'testMinDFA2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                #-----------------------#
                delta_n6 = {  # DFA p.93 L&P (for eliminating nonreachable states)
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
                    (6, 'b') : 5,
                    (7, 'a') : 6,
                    (7, 'b') : 8,
                    (8, 'a') : 7,
                    (8, 'b') : 3,
                
                }
                n6 = dfa(delta=delta_n6, start=1, finals={1, 3, 7})
                print('Original DFA is')
                print(40*'-')
                print(n6)
                print(40*'-')
                reachable_n6 = n6.remove_nonreachable()
                print('reachable DFA is')
                print(40*'-')
                print(reachable_n6)
                print(40*'-')
                minimal_n6 = reachable_n6.minimized1()
                print()
                print('Minimized DFA n6 is')
                print(40*'-')
                print(minimal_n6)
                print(40*'-')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testMinDFA3(self):
        checkFileName = 'testMinDFA3' + '.good'
        outFileName = 'testMinDFA3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                #-----------------------#
                delta_n7 = {  # DFA p.156 HMU, 3rd Ed. (for minimization algo)
                    ('A', 0) : 'B',
                    ('A', 1) : 'F',
                    ('B', 0) : 'G',
                    ('B', 1) : 'C',
                    ('C', 0) : 'A',
                    ('C', 1) : 'C',
                    ('D', 0) : 'C',
                    ('D', 1) : 'G',
                    ('E', 0) : 'H',
                    ('E', 1) : 'F',
                    ('F', 0) : 'C',
                    ('F', 1) : 'G',
                    ('G', 0) : 'G',
                    ('G', 1) : 'E',
                    ('H', 0) : 'G',
                    ('H', 1) : 'C'
                }
                n7 = dfa(delta=delta_n7, start='A', finals={'C'})
                print('\nDFA n7:')
                print(40*'-')
                print(n7)
                print(40*'-')
                print('\nAbout to Minimize n7 (method 1: L&P)')
                min1_n7 = n7.minimized1()
                print('\nMinimized n7 is (method 1: L&P)')
                print(40*'-')
                print(min1_n7)
                print(40*'-')
                print('\nAbout to Minimize n7 (method 2: marking algo)')
                min2_n7 = n7.minimized2()
                print('\nMinimized n7 is (method 2: marking algo)')
                print(40*'-')
                print(min2_n7)
                print(40*'-')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testMinDFA4(self):
        checkFileName = 'testMinDFA4' + '.good'
        outFileName = 'testMinDFA4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                #-----------------------#
                delta_n8 = {  # DFA Martin, 4th Ed., p.76 (for minimization algo)
                    (0, 'a') : 1,
                    (0, 'b') : 9,
                    (1, 'a') : 8,
                    (1, 'b') : 2,
                    (2, 'a') : 3,
                    (2, 'b') : 2,
                    (3, 'a') : 2,
                    (3, 'b') : 4,
                    (4, 'a') : 5,
                    (4, 'b') : 8,
                    (5, 'a') : 4,
                    (5, 'b') : 5,
                    (6, 'a') : 7,
                    (6, 'b') : 5,
                    (7, 'a') : 6,
                    (7, 'b') : 5,
                    (8, 'a') : 1,
                    (8, 'b') : 3,
                    (9, 'a') : 7,
                    (9, 'b') : 8
                }
                n8 = dfa(delta=delta_n8, start=0, finals={3, 4, 8, 9})
                print('\nDFA n8:')
                print(40*'-')
                print(n8)
                print(40*'-')
                print('\nAbout to minimize n8 (method 1: L&P)')
                min1_n8 = n8.minimized1(verbose=True)
                print('\nMinimized n8: (method 1: L&P)')
                print(40*'-')
                print(min1_n8)
                print(40*'-')
                print('\nAbout to Minimize n8 (method 2: marking algo)')
                min2_n8 = n8.minimized2(verbose=True)
                print('\nMinimized n8: (method 2: marking algo)')
                print(40*'-')
                print(min2_n8)
                print(40*'-')
                #-----------------------#
                print(f'min1_n8.equiv(min2_n8) is {min1_n8.equiv(min2_n8)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testMinDFA5(self):
        checkFileName = 'testMinDFA5' + '.good'
        outFileName = 'testMinDFA5' + '.out'

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
                
                m = nfa(delta=delta, start=0, finals={4}) # accepts all binary strings
                dash40 = 40*'-'
                print('NFA is as follows:')
                print(dash40)
                print(m)
                print(dash40)
                
                n = m.to_dfa().standard_numbered()
                print('Equivalent DFA is as follows:')
                print(dash40)
                print(n)
                print(dash40)
                
                nmin1 = n.minimized1(verbose=True)
                print(nmin1)
                print(dash40)
                nmin2 = n.minimized2(verbose=True)
                print(nmin2)
                print(dash40)
                print(f'nmin1.equiv(nmin2) is {nmin1.equiv(nmin2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testMinDFA6(self):
        checkFileName = 'testMinDFA6' + '.good'
        outFileName = 'testMinDFA6' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                #-----------------------#
                delta_n6 = {  # DFA p.93 L&P (for eliminating nonreachable states)
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
                    (6, 'b') : 5,
                    (7, 'a') : 6,
                    (7, 'b') : 8,
                    (8, 'a') : 7,
                    (8, 'b') : 3,
                
                }
                n6 = dfa(delta=delta_n6, start=1, finals={1, 3, 7})
                print('Original DFA is')
                print(40*'-')
                print(n6)
                print(40*'-')
                print('Minimized DFA n6 is')
                minimal_n6 = n6.minimized()
                print(40*'-')
                print(minimal_n6)
                print(40*'-')
                print('Minimized DFA n6 is (verbosely)')
                minimal_n6 = n6.minimized(verbose=True)
                print(40*'-')
                print(minimal_n6)
                print(40*'-')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
