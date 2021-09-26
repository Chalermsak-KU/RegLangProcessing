import unittest
from contextlib import redirect_stdout
from reglang.regx import regx

class TestRegxStar(unittest.TestCase):

    def testRegxStar1(self):
        checkFileName = 'testRegxStar1' + '.good'
        outFileName = 'testRegxStar1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                
                astar = a.star
                print(f"NFA for regular expression 'a.star' with value '{astar.val}' is")
                print(astar.nfa)
                
                for s in ['', 'a', 'aa', 'aaa', 'b', 'ab', 'aaa3']:
                    print(f"regx {astar.val} : string '{s}' -> {astar > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
