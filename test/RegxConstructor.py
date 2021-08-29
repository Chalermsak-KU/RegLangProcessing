import unittest
from contextlib import redirect_stdout
from reglang.regx import regx

class TestRegxConstructor(unittest.TestCase):

    def testRegxConstructor1(self):
        checkFileName = 'testRegxConstructor1' + '.good'
        outFileName = 'testRegxConstructor1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                
                b = regx('b')
                print(f"NFA for regular expression '{b.val}' is")
                print(b.nfa)
                
                e = regx('#') # represents the empty string
                print(f"NFA for regular expression '{e.val}' (empty string) is")
                print(e.nfa)
                
                n = regx('@') # represents the empty set
                print(f"NFA for regular expression '{n.val}' (empty set) is")
                print(n.nfa)
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
