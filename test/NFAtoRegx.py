import unittest
from contextlib import redirect_stdout
from reglang.nfa import nfa

class TestNFAtoRegx(unittest.TestCase):

    def testNFAtoRegx1(self):
        checkFileName = 'testNFAtoRegx1' + '.good'
        outFileName = 'testNFAtoRegx1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta9 = {  # NFA L&P p.81 (to convert to regexp)
                    (1, 'a') : {1},
                    (1, 'b') : {3},
                    (2, 'a') : {2},
                    (2, 'b') : {1},
                    (3, 'a') : {3},
                    (3, 'b') : {2}
                }
                m9 = nfa(delta=delta9, start=1, finals={3})
                print()
                print('NFA m9 is as follows:')
                print(m9)
                print()
                n9 = m9.snfa()
                print('simplified NFA for m9 is as follows:')
                print(n9)
                print()
                r9recursive = m9.to_regx2()
                print('[recursive algo]\nregexp is', r9recursive)
                r9iterative = m9.to_regx()
                print('\n[iterative algo]\nregexp is', r9iterative)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNFAtoRegx2(self):
        checkFileName = 'testNFAtoRegx2' + '.good'
        outFileName = 'testNFAtoRegx2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta10 = {  # NFA L&P exercise 2.3.7a (to convert to regexp)
                    (1, 'a') : {1},
                    (1, 'b') : {2},
                    (2, 'a') : {2},
                    (2, 'b') : {1}
                }
                m10 = nfa(delta=delta10, start=1, finals={2})
                
                print()
                print('NFA m10 is as follows:')
                print(m10)
                print()
                n10 = m10.snfa()
                print('simplified NFA for m10 is as follows:')
                print(n10)
                print()
                r10recursive = m10.to_regx2()
                print('[recursive algo]\nregexp is', r10recursive)
                r10iterative = m10.to_regx()
                print('\n[iterative algo]\nregexp is', r10iterative)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNFAtoRegx3(self):
        checkFileName = 'testNFAtoRegx3' + '.good'
        outFileName = 'testNFAtoRegx3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta11 = {  # NFA L&P exercise 2.3.7d (to convert to regexp)
                    (1, 'a') : {2},
                    (1, 'b') : {4},
                    (2, 'b') : {3, 4},
                    (3, 'a') : {3},
                    (3, 'b') : {3},
                    (4, 'a') : {2, 4}
                }
                m11 = nfa(delta=delta11, start=1, finals={3})
                print()
                print('NFA m11 is as follows:')
                print(m11)
                print()
                n11 = m11.snfa()
                print('simplified NFA for m11 is as follows:')
                print(n11)
                print()
                r11recursive = m11.to_regx2()
                print('[recursive algo]\nregexp is', r11recursive)
                r11iterative = m11.to_regx()
                print('\n[iterative algo]\nregexp is', r11iterative)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNFAtoRegx4(self):
        checkFileName = 'testNFAtoRegx4' + '.good'
        outFileName = 'testNFAtoRegx4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta12 = {  # NFA example in the sheet (to convert to regexp)
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
                print('NFA m12 is as follows:')
                print(m12)
                print()
                n12 = m12.snfa()
                print('simplified NFA for m12 is as follows:')
                print(n12)
                print()
                r12recursive = m12.to_regx2()
                print('[recursive algo]\nregexp is', r12recursive)
                r12iterative = m12.to_regx()
                print('\n[iterative algo]\nregexp is', r12iterative)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testNFAtoRegx5(self):
        checkFileName = 'testNFAtoRegx5' + '.good'
        outFileName = 'testNFAtoRegx5' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta = {  # NFA example in Kleene's Thm-2 slides  (to convert to regexp)
                    (1, 'a') : {2},
                    (1, 'b') : {1, 3},
                    (2, 'a') : {3},
                    (3, 'a') : {3},
                    (3, 'b') : {3},
                    (3, '')  : {4},
                    (4, 'a') : {2},
                    (4, 'b') : {2, 4}
                }
                m = nfa(delta=delta, start=1, finals={2, 4})
                print()
                print('NFA m is as follows:')
                print(m)
                print()
                n = m.snfa()
                print('simplified NFA for m is as follows:')
                print(n)
                print()
                r_recursive = m.to_regx2()
                print('[recursive algo]\nregexp is', r_recursive)
                r_iterative = m.to_regx()
                print('\n[iterative algo]\nregexp is', r_iterative)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
