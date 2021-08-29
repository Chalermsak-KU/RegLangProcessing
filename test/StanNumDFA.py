import unittest
from contextlib import redirect_stdout
from reglang.dfa import dfa

class TestStanNumDFA(unittest.TestCase):

    def testStanNumDFA1(self):
        checkFileName = 'testStanNumDFA1' + '.good'
        outFileName = 'testStanNumDFA1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta_n1 = {  # DFA p.94 L&P (for minimization algo in L&P)
                    ('one', 'a') : 'two',
                    ('one', 'b') : 'four',
                    ('two', 'a') : 'five',
                    ('two', 'b') : 'three',
                    ('three', 'a') : 'two',
                    ('three', 'b') : 'six',
                    ('four', 'a') : 'one',
                    ('four', 'b') : 'five',
                    ('five', 'a') : 'five',
                    ('five', 'b') : 'five',
                    ('six', 'a') : 'three',
                    ('six', 'b') : 'five'
                }
                
                n1 = dfa(delta=delta_n1, start='one', finals={'one', 'three'})
                print('Original DFA is')
                print(40*'-')
                print(f'current DFA n1:\n{n1}')
                
                m1 = n1.standard_numbered()
                print(40*'-')
                print(f'Standard-numbered DFA m1:\n{m1}')
                
                m2 = m1.standard_numbered()
                print(40*'-')
                print(f'Standard-numbered DFA m2:\n{m2}')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testStanNumDFA2(self):
        checkFileName = 'testStanNumDFA2' + '.good'
        outFileName = 'testStanNumDFA2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                delta_n1 = {  # DFA p.93 L&P (for minimization algo in L&P)
                    ('one', 'a') : 'two',
                    ('one', 'b') : 'four',
                    ('two', 'a') : 'five',
                    ('two', 'b') : 'three',
                    ('three', 'a') : 'two',
                    ('three', 'b') : 'six',
                    ('four', 'a') : 'one',
                    ('four', 'b') : 'five',
                    ('five', 'a') : 'five',
                    ('five', 'b') : 'five',
                    ('six', 'a') : 'three',
                    ('six', 'b') : 'five',
                    ('seven', 'a') : 'six',
                    ('seven', 'b') : 'eight',
                    ('eight', 'a') : 'seven',
                    ('eight', 'b') : 'three'
                }
                
                n1 = dfa(delta=delta_n1, start='one', finals={'one', 'three'})
                print('Original DFA is')
                print(40*'-')
                print(f'current DFA n1:\n{n1}')
                
                m1 = n1.standard_numbered()
                print(40*'-')
                print(f'Standard-numbered DFA m1:\n{m1}')
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
