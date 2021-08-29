import unittest
from contextlib import redirect_stdout
from reglang.dfa import dfa

class TestEquivDFA(unittest.TestCase):

    def testEquivDFA1(self):
        checkFileName = 'testEquivDFA1' + '.good'
        outFileName = 'testEquivDFA1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {  # DFA p.100 L&P with one more final state
                    (1, 'a') : 2,
                    (1, 'b') : 3,
                    (2, 'a') : 4,
                    (2, 'b') : 1,
                    (3, 'a') : 1,
                    (3, 'b') : 4,
                    (4, 'a') : 4,
                    (4, 'b') : 4
                }
                dfa1 = dfa(delta=delta1, start=1, finals={1,2})
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                delta2 = {  # exactly the same as delta1
                    (1, 'a') : 2,
                    (1, 'b') : 3,
                    (2, 'a') : 4,
                    (2, 'b') : 1,
                    (3, 'a') : 1,
                    (3, 'b') : 4,
                    (4, 'a') : 4,
                    (4, 'b') : 4
                }
                dfa2 = dfa(delta=delta2, start=1, finals={1,2})
                print('dfa2 is')
                print(dfa2)
                print(40*'-')
                print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testEquivDFA2(self):
        checkFileName = 'testEquivDFA2' + '.good'
        outFileName = 'testEquivDFA2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {  # DFA p.100 L&P with one more final state
                    (1, 'a') : 2,
                    (1, 'b') : 3,
                    (2, 'a') : 4,
                    (2, 'b') : 1,
                    (3, 'a') : 1,
                    (3, 'b') : 4,
                    (4, 'a') : 4,
                    (4, 'b') : 4
                }
                dfa1 = dfa(delta=delta1, start=1, finals={1,2})
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                delta2 = {  # differs from delta1 only in state names
                    (10, 'a') : 20,
                    (10, 'b') : 30,
                    (20, 'a') : 40,
                    (20, 'b') : 10,
                    (30, 'a') : 10,
                    (30, 'b') : 40,
                    (40, 'a') : 40,
                    (40, 'b') : 40
                }
                dfa2 = dfa(delta=delta2, start=10, finals={10,20})
                print('dfa2 is')
                print(dfa2)
                print(40*'-')
                print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testEquivDFA3(self):
        checkFileName = 'testEquivDFA3' + '.good'
        outFileName = 'testEquivDFA3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {  # DFA that accepts strings in {a,b,c}* that has no substring ac
                    (0, 'a') : 1,
                    (0, 'b') : 0,
                    (0, 'c') : 0,
                    (1, 'a') : 1,
                    (1, 'b') : 0,
                    (1, 'c') : 2,
                    (2, 'a') : 2,
                    (2, 'b') : 2,
                    (2, 'c') : 2
                }
                dfa1 = dfa(delta=delta1, start=0, finals={0,1})
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                delta2 = {  # another DFA that accepts the same language as dfa1
                    (1, 'a') : 2,
                    (1, 'b') : 3,
                    (1, 'c') : 1,
                    (2, 'a') : 2,
                    (2, 'b') : 3,
                    (2, 'c') : 5,
                    (3, 'a') : 2,
                    (3, 'b') : 3,
                    (3, 'c') : 4,
                    (4, 'a') : 2,
                    (4, 'b') : 3,
                    (4, 'c') : 4,
                    (5, 'a') : 5,
                    (5, 'b') : 5,
                    (5, 'c') : 5
                }
                dfa2 = dfa(delta=delta2, start=1, finals={1,2,3,4})
                print('dfa2 is')
                print(dfa2)
                print(40*'-')
                print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testEquivDFA4(self):
        checkFileName = 'testEquivDFA4' + '.good'
        outFileName = 'testEquivDFA4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {  # DFA that accepts every string in {a,b,c}*
                    (0, 'a') : 1,
                    (0, 'b') : 0,
                    (0, 'c') : 0,
                    (1, 'a') : 1,
                    (1, 'b') : 0,
                    (1, 'c') : 2,
                    (2, 'a') : 2,
                    (2, 'b') : 2,
                    (2, 'c') : 2
                }
                dfa1 = dfa(delta=delta1, start=0, finals={0,1,2})
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                delta2 = {  # another DFA that accepts the same language as dfa1
                    (1, 'a') : 2,
                    (1, 'b') : 3,
                    (1, 'c') : 1,
                    (2, 'a') : 2,
                    (2, 'b') : 3,
                    (2, 'c') : 5,
                    (3, 'a') : 2,
                    (3, 'b') : 3,
                    (3, 'c') : 4,
                    (4, 'a') : 2,
                    (4, 'b') : 3,
                    (4, 'c') : 4,
                    (5, 'a') : 5,
                    (5, 'b') : 5,
                    (5, 'c') : 5
                }
                dfa2 = dfa(delta=delta2, start=1, finals={1,2,3,4,5})
                print('dfa2 is')
                print(dfa2)
                print(40*'-')
                print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testEquivDFA5(self):
        checkFileName = 'testEquivDFA5' + '.good'
        outFileName = 'testEquivDFA5' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {  # DFA that accepts the empty set
                    (0, 'a') : 1,
                    (0, 'b') : 0,
                    (0, 'c') : 0,
                    (1, 'a') : 1,
                    (1, 'b') : 0,
                    (1, 'c') : 2,
                    (2, 'a') : 2,
                    (2, 'b') : 2,
                    (2, 'c') : 2
                }
                dfa1 = dfa(delta=delta1, start=0, finals=set())
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                delta2 = {  # another DFA that accepts the same language as dfa1
                    (1, 'a') : 2,
                    (1, 'b') : 1,
                    (1, 'c') : 1,
                    (2, 'a') : 2,
                    (2, 'b') : 1,
                    (2, 'c') : 2,
                    (3, 'a') : 2,
                    (3, 'b') : 3,
                    (3, 'c') : 2
                }
                dfa2 = dfa(delta=delta2, start=1, finals={3})
                print('dfa2 is')
                print(dfa2)
                print(40*'-')
                print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testEquivDFA6(self):
        checkFileName = 'testEquivDFA6' + '.good'
        outFileName = 'testEquivDFA6' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {  # DFA that accepts the empty set
                    (0, 'a') : 1,
                    (0, 'b') : 0,
                    (0, 'c') : 0,
                    (1, 'a') : 1,
                    (1, 'b') : 0,
                    (1, 'c') : 2,
                    (2, 'a') : 2,
                    (2, 'b') : 2,
                    (2, 'c') : 2
                }
                dfa1 = dfa(delta=delta1, start=0, finals=set())
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                delta2 = {  # another DFA that accepts the empty set but different alphabet
                    (1, 'a') : 2,
                    (1, 'b') : 1,
                    (2, 'a') : 2,
                    (2, 'b') : 1,
                    (3, 'a') : 2,
                    (3, 'b') : 3
                }
                dfa2 = dfa(delta=delta2, start=1, finals={3})
                print('dfa2 is')
                print(dfa2)
                print(40*'-')
                print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testEquivDFA7(self):
        checkFileName = 'testEquivDFA7' + '.good'
        outFileName = 'testEquivDFA7' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta1 = {  # DFA that accepts strings in {a,b,c}* that has no substring ac
                    (0, 'a') : 1,
                    (0, 'b') : 0,
                    (0, 'c') : 0,
                    (1, 'a') : 1,
                    (1, 'b') : 0,
                    (1, 'c') : 2,
                    (2, 'a') : 2,
                    (2, 'b') : 2,
                    (2, 'c') : 2
                }
                dfa1 = dfa(delta=delta1, start=0, finals={0,1})
                print('dfa1 is')
                print(dfa1)
                print(40*'-')
                delta2 = {  # another DFA that accepts a different language from dfa1's
                    (1, 'a') : 2,
                    (1, 'b') : 3,
                    (1, 'c') : 1,
                    (2, 'a') : 2,
                    (2, 'b') : 3,
                    (2, 'c') : 5,
                    (3, 'a') : 2,
                    (3, 'b') : 3,
                    (3, 'c') : 4,
                    (4, 'a') : 2,
                    (4, 'b') : 3,
                    (4, 'c') : 4,
                    (5, 'a') : 5,
                    (5, 'b') : 5,
                    (5, 'c') : 5
                }
                dfa2 = dfa(delta=delta2, start=1, finals={1,3,4})
                print('dfa2 is')
                print(dfa2)
                print(40*'-')
                print(f'That dfa1 is equivalent to dfa2 is {dfa1.equiv(dfa2)}')
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
