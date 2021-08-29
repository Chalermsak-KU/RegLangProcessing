import unittest
from contextlib import redirect_stdout
from reglang.regx import regx

class TestRegxOp(unittest.TestCase):

    def testRegxOp1(self):
        checkFileName = 'testRegxOp1' + '.good'
        outFileName = 'testRegxOp1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                b = regx('b')
                print(f"NFA for regular expression '{b.val}' is")
                print(b.nfa)
                aUb = a|b
                print(f"NFA for regular expression '{aUb.val}' is")
                print(aUb.nfa)
                
                for s in ['a', 'b', '1', 'ba', '12a', '']:
                    print(f"regx {aUb.val} : string '{s}' -> {aUb > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxOp11(self):
        checkFileName = 'testRegxOp11' + '.good'
        outFileName = 'testRegxOp11' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                b = regx('b')
                print(f"NFA for regular expression '{b.val}' is")
                print(b.nfa)
                ab = a&b
                print(f"NFA for regular expression 'a&b' with value '{ab.val}' is")
                print(ab.nfa)
                
                for s in ['a', 'b', '1', 'ab', 'ba', 'ab12', '']:
                    print(f"regx {ab.val} : string '{s}' -> {ab > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxOp2(self):
        checkFileName = 'testRegxOp2' + '.good'
        outFileName = 'testRegxOp2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                e = regx('#') # represents the empty string
                print(f"NFA for regular expression '{e.val}' is")
                print(e.nfa)
                
                aUe = a|e
                print(f"NFA for regular expression '{aUe.val}' is")
                print(aUe.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {aUe.val} : string '{s}' -> {aUe > s}")
                print()
                
                eUa = e|a
                print(f"NFA for regular expression '{eUa.val}' is")
                print(eUa.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {eUa.val} : string '{s}' -> {eUa > s}")
                print()
                
                eUe = e|e
                print(f"NFA for regular expression '{eUe.val}' is")
                print(eUe.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {eUe.val} : string '{s}' -> {eUe > s}")
                print()
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxOp22(self):
        checkFileName = 'testRegxOp22' + '.good'
        outFileName = 'testRegxOp22' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                e = regx('#') # represents the empty string
                print(f"NFA for regular expression '{e.val}' is")
                print(e.nfa)
                
                ae = a&e
                print(f"NFA for regular expression a# with value '{ae.val}' is")
                print(ae.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {ae.val} : string '{s}' -> {ae > s}")
                print()
                
                ea = e&a
                print(f"NFA for regular expression #a with value '{ea.val}' is")
                print(ea.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {ea.val} : string '{s}' -> {ea > s}")
                print()
                
                ee = e&e
                print(f"NFA for regular expression ## with value '{ee.val}' is")
                print(ee.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {ee.val} : string '{s}' -> {ee > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxOp3(self):
        checkFileName = 'testRegxOp3' + '.good'
        outFileName = 'testRegxOp3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                n = regx('@') # empty set
                print(f"NFA for regular expression '{n.val}' is")
                print(n.nfa)
                
                aUn = a|n
                print(f"NFA for regular expression 'aU@' with value '{aUn.val}' is")
                print(aUn.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {aUn.val} : string '{s}' -> {aUn > s}")
                print()
                
                nUa = n|a
                print(f"NFA for regular expression '@Ua' with value '{nUa.val}' is")
                print(nUa.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {nUa.val} : string '{s}' -> {nUa > s}")
                print()
                
                nUn = n|n
                print(f"NFA for regular expression '@U@' with value {nUn.val}' is")
                print(nUn.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {nUn.val} : string '{s}' -> {nUn > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxOp33(self):
        checkFileName = 'testRegxOp33' + '.good'
        outFileName = 'testRegxOp33' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                print(f"NFA for regular expression '{a.val}' is")
                print(a.nfa)
                n = regx('@') # empty set
                print(f"NFA for regular expression '{n.val}' is")
                print(n.nfa)
                
                an = a&n
                print(f"NFA for regular expression 'a@' with value '{an.val}' is")
                print(an.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {an.val} : string '{s}' -> {an > s}")
                print()
                
                na = n&a
                print(f"NFA for regular expression '@a' with value '{na.val}' is")
                print(na.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {na.val} : string '{s}' -> {na > s}")
                print()
                
                nn = n&n
                print(f"NFA for regular expression '@@' with value {nn.val}' is")
                print(nn.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {nn.val} : string '{s}' -> {nn > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxOp4(self):
        checkFileName = 'testRegxOp4' + '.good'
        outFileName = 'testRegxOp4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                e = regx('#') # empty string
                print(f"NFA for regular expression '{e.val}' is")
                print(e.nfa)
                n = regx('@') # empty set
                print(f"NFA for regular expression '{n.val}' is")
                print(n.nfa)
                
                eUn = e|n
                print(f"NFA for regular expression '#U@' with value '{eUn.val}' is")
                print(eUn.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {eUn.val} : string '{s}' -> {eUn > s}")
                print()
                
                nUe = n|e
                print(f"NFA for regular expression '@U#' with value '{nUe.val}' is")
                print(nUe.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {nUe.val} : string '{s}' -> {nUe > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxOp44(self):
        checkFileName = 'testRegxOp44' + '.good'
        outFileName = 'testRegxOp44' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                e = regx('#') # empty string
                print(f"NFA for regular expression '{e.val}' is")
                print(e.nfa)
                n = regx('@') # empty set
                print(f"NFA for regular expression '{n.val}' is")
                print(n.nfa)
                
                en = e&n
                print(f"NFA for regular expression '#@' with value '{en.val}' is")
                print(en.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {en.val} : string '{s}' -> {en > s}")
                print()
                
                ne = n&e
                print(f"NFA for regular expression '@#' with value '{ne.val}' is")
                print(ne.nfa)
                for s in ['a', 'b', 'aa', '12a', '']:
                    print(f"regx {ne.val} : string '{s}' -> {ne > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
