import unittest
from contextlib import redirect_stdout
from reglang.regx import regx

class TestPrimRegxGen(unittest.TestCase):

    def testPrimRegxGen1(self):
        checkFileName = 'testPrimRegxGen1' + '.good'
        outFileName = 'testPrimRegxGen1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                for s in ['a', 'b', '1', '']:
                    print(f"regx {a.val} : string '{s}' -> {a.gen(s)}")
                print()
                
                b = regx('b')
                for s in ['a', 'b', '1', '']:
                    print(f"regx {b.val} : string '{s}' -> {b.gen(s)}")
                print()
                
                e = regx('#') # represents the empty string
                for s in ['a', 'b', '1', '']:
                    print(f"regx {e.val} : string '{s}' -> {e.gen(s)}")
                print()
                
                n = regx('@') # represents the empty set
                for s in ['a', 'b', '1', '']:
                    print(f"regx {n.val} : string '{s}' -> {n.gen(s)}")
                print()
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
