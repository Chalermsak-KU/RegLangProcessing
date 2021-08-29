import unittest
from contextlib import redirect_stdout
from reglang.nfa import nfa

class TestEClosure(unittest.TestCase):

    def testEClosure1(self):
        checkFileName = 'testEClosure1' + '.good'
        outFileName = 'testEClosure1' + '.out'

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
                for q in m02.states:
                    closure = m02._ep_closure(q)
                    print(f'E-closure of state {q} = {closure}')
                print(dash40)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testEClosure2(self):
        checkFileName = 'testEClosure2' + '.good'
        outFileName = 'testEClosure2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {   # an NFA
                    (0, 'a'):{1},
                    (0, '') :{2},
                    (1, 'b'):{3},
                    (1, '') :{0, 4},
                    (2, 'a'):{1, 5},
                    (2, 'b'):{2},
                    (2, '') :{4},
                    (3, '') :{4},
                    (4, '') :{6},
                    (5, 'a'):{5},
                    (5, '') :{6},
                }
                m1 = nfa(delta=delta1, start=0, finals={6})
                dash40 = 40*'-'
                print('NFA is as follows:')
                print(dash40)
                print(m1)
                print(dash40)
                for q in m1.states:
                    closure = m1._ep_closure(q)
                    print(f'E-closure of state {q} = {closure}')
                print(dash40)
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
