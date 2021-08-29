import unittest
from contextlib import redirect_stdout
from reglang.regx import regx
from reglang.dfa import dfa

class TestRegxEquiv(unittest.TestCase):

    def testRegxEquiv1(self):
        checkFileName = 'testRegxEquiv1' + '.good'
        outFileName = 'testRegxEquiv1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                r1 = regx('c*(aUbc*)*')
                print(f'r1 is {r1}')
                
                del11 = {
                    (1,'a'): 2,
                    (1,'b'): 1,
                    (1,'c'): 1,
                    (2,'a'): 2,
                    (2,'b'): 1,
                    (2,'c'): 3,
                    (3,'a'): 3,
                    (3,'b'): 3,
                    (3,'c'): 3
                }
                d11 = dfa(delta=del11, start=1, finals={1,2})
                print(f'DFA d11 is')
                print(40*'-')
                print(d11)
                print(40*'-')
                r11 = d11.to_regx()
                print(f'r11 is {r11}')
                print(f'r1.equiv(r11) is {r1.equiv(r11)}')
                print(r1, '==', r11, 'is', r1 == r11)
                print(40*'-')
                r2 = regx('(#Ucc*)(aUb(c*cU#))*')
                print(f'r2 is {r2}')
                print(f'r1.equiv(r2) is {r1.equiv(r2)}')
                print(r1, '==', r2, 'is', r1 == r2)
                print(f'r11.equiv(r2) is {r11.equiv(r2)}')
                print(r11, '==', r2, 'is', r11 == r2)
                print(40*'-')
                r3 = regx('(#Ucc*)(aUbc*c)*')
                print(f'r3 is {r3}')
                print(f'r1.equiv(r3) is {r1.equiv(r3)}')
                print(r1, '==', r3, 'is', r1 == r3)
                print(f'r11.equiv(r3) is {r11.equiv(r3)}')
                print(r11, '==', r3, 'is', r11 == r3)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxEquiv2(self):
        checkFileName = 'testRegxEquiv2' + '.good'
        outFileName = 'testRegxEquiv2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                # r1 is the regx of {w in {0,1}*: w has no substring 111}
                r1 = regx('0* U 0*(1U11)(00*(1U11))*0*')
                r2 = regx('(#U1U11)(0U01U011)*')
                r3 = regx('(0U10U110)*(#U1U11)')
                print(r1, '==', r2, 'is', r1 == r2)
                print(r1, '==', r3, 'is', r1 == r3)
                print(r2, '==', r3, 'is', r2 == r3)
                
                r4 = regx('(1U11)(0U01U011)*')
                print(r1, '==', r4, 'is', r1 == r4)
                print(r2, '==', r4, 'is', r2 == r4)
                print(r3, '==', r4, 'is', r3 == r4)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxEquiv3(self):
        checkFileName = 'testRegxEquiv3' + '.good'
        outFileName = 'testRegxEquiv3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                # r1 is the regx of {w in {0,1}*: w ends with 10}
                r1 = regx('(0U1)*10')
                r2 = regx('@*(0U1)*10')
                r3 = regx('@U(0U1)*10')
                r4 = regx('0*(10*)*10')
                r5 = regx('1*(01*)*10')
                print(r1, '==', r2, 'is', r1 == r2)
                print(r1, '==', r3, 'is', r1 == r3)
                print(r1, '==', r4, 'is', r1 == r4)
                print(r1, '==', r5, 'is', r1 == r5)
                
                dfa1delta = { # this dfa accepts the same language as r1's
                    (1, '0') : 1,
                    (1, '1') : 2,
                    (2, '0') : 3,
                    (2, '1') : 2,
                    (3, '0') : 1,
                    (3, '1') : 2
                }
                dfa1 = dfa(delta=dfa1delta, start=1, finals={3})
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                r6 = dfa1.to_regx()
                print(f'The above dfa accepts the language with regx {r6}')
                print(40*'-')
                print(r1, '==', r6, 'is', r1 == r6)
                print(40*'-')
                
                r7 = regx('(0U01U011)*')
                print(r1, '==', r7, 'is', r1 == r7)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
