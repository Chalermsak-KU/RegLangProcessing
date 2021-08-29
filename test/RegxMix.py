import unittest
from contextlib import redirect_stdout
from reglang.regx import regx

class TestRegxMix(unittest.TestCase):

    def testRegxMix1(self):
        checkFileName = 'testRegxMix1' + '.good'
        outFileName = 'testRegxMix1' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                b = regx('b')
                c = regx('c')
                
                aUbUc = a|b|c
                print(f"NFA for regular expression 'a|b|c' with value '{aUbUc.val}' is")
                print(aUbUc.nfa)
                for s in ['a', 'b', 'c', '1', 'ab', 'cbaa', '']:
                    print(f"regx {aUbUc.val} : string '{s}' -> {aUbUc > s}")
                print()
                
                abc = a&b&c
                print(f"NFA for regular expression 'a&b&c' with value '{abc.val}' is")
                print(abc.nfa)
                for s in ['a', 'b', 'c', 'ab', 'bc', 'abc', 'abcd', 'a12b', '']:
                    print(f"regx {abc.val} : string '{s}' -> {abc > s}")
                print()
                
                ass = a.star().star()
                print(f"NFA for regular expression 'a.star().star()' with value '{ass.val}' is")
                print(ass.nfa)
                for s in ['', 'a', 'aa', 'aaa', 'aaaa', 'b', 'aaab', 'a12b']:
                    print(f"regx {ass.val} : string '{s}' -> {ass > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxMix11(self):
        checkFileName = 'testRegxMix11' + '.good'
        outFileName = 'testRegxMix11' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                x = regx('aUbUc')
                print(f"NFA for regular expression 'aUbUc' with value '{x.val}' is")
                print(x.nfa)
                for s in ['a', 'b', 'c', '1', 'ab', 'cbaa', '']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('abc')
                print(f"NFA for regular expression 'abc' with value '{x.val}' is")
                print(x.nfa)
                for s in ['a', 'b', 'c', 'ab', 'bc', 'abc', 'abcd', 'a12b', '']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('a**')
                print(f"NFA for regular expression 'a**' with value '{x.val}' is")
                print(x.nfa)
                for s in ['', 'a', 'aa', 'aaa', 'aaaa', 'b', 'aaab', 'a12b']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxMix2(self):
        checkFileName = 'testRegxMix2' + '.good'
        outFileName = 'testRegxMix2' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                b = regx('b')
                c = regx('c')
                
                aUbc = a|b&c
                print(f"NFA for regular expression 'a|b&c' with value '{aUbc.val}' is")
                for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
                    print(f"regx {aUbc.val} : string '{s}' -> {aUbc > s}")
                print()
                
                aUb_c = (a|b)&c
                print(f"NFA for regular expression '(a|b)&c' with value '{aUb_c.val}' is")
                for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
                    print(f"regx {aUb_c.val} : string '{s}' -> {aUb_c > s}")
                print()
                
                aUbSTARc = a|b.star()&c
                print(f"NFA for regular expression 'a|b.star()&c' with value '{aUbSTARc.val}' is")
                for s in ['a', 'b', 'c', 'bc', 'bbc', 'ac', '']:
                    print(f"regx {aUbSTARc.val} : string '{s}' -> {aUbSTARc > s}")
                print()
                
                x = a&(b&c).star()
                print(f"NFA for regular expression 'a&(b&c).star()' with value '{x.val}' is")
                for s in ['a', 'b', 'c', 'abc', 'abcbcbc', 'bc', 'acbbc', '']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxMix22(self):
        checkFileName = 'testRegxMix22' + '.good'
        outFileName = 'testRegxMix22' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                x = regx('aUbc')
                for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('(aUb)c')
                for s in ['a', 'b', 'c', 'bc', 'ab', 'ac', '']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('aUb*c')
                for s in ['a', 'b', 'c', 'bc', 'bbc', 'ac', '']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('a(bc)*')
                for s in ['a', 'b', 'c', 'abc', 'abcbcbc', 'bc', 'acbbc', '']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxMix3(self):
        checkFileName = 'testRegxMix3' + '.good'
        outFileName = 'testRegxMix3' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                b = regx('b')
                c = regx('c')
                
                aU_bc_STAR = a|(b&c).star()
                print(f"NFA for regular expression 'a|(b&c).star()' with value '{aU_bc_STAR.val}' is")
                for s in ['a', '', 'bc', 'bcbc', 'abc', 'bcc', 'ac']:
                    print(f"regx {aU_bc_STAR.val} : string '{s}' -> {aU_bc_STAR > s}")
                print()
                
                _aUb_STARc = (a|b).star()&c
                print(f"NFA for regular expression '(a|b).star()&c' with value '{_aUb_STARc.val}' is")
                for s in ['', 'c', 'ac', 'bc', 'abbac', 'aab', 'cab']:
                    print(f"regx {_aUb_STARc.val} : string '{s}' -> {_aUb_STARc > s}")
                print()
                
                aUbc_STAR = (a|b&c).star()
                print(f"NFA for regular expression '(a|b&c).star()' with value '{aUbc_STAR.val}' is")
                for s in ['', 'a', 'bc', 'bcbc', 'aaa', 'bcabcaa', 'aabc', 'cb', 'acbc']:
                    print(f"regx {aUbc_STAR.val} : string '{s}' -> {aUbc_STAR > s}")
                print()
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxMix33(self):
        checkFileName = 'testRegxMix33' + '.good'
        outFileName = 'testRegxMix33' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                x = regx('aU(bc)*')
                for s in ['a', '', 'bc', 'bcbc', 'abc', 'bcc', 'ac']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('(aUb)*c')
                for s in ['', 'c', 'ac', 'bc', 'abbac', 'aab', 'cab']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('(aUbc)*')
                for s in ['', 'a', 'bc', 'bcbc', 'aaa', 'bcabcaa', 'aabc', 'cb', 'acbc']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxMix4(self):
        checkFileName = 'testRegxMix4' + '.good'
        outFileName = 'testRegxMix4' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                a = regx('a')
                b = regx('b')
                c = regx('c')
                e = regx('#')
                i = regx('1')
                o = regx('0')
                
                no_ac = c.star() & (a | b&c.star()).star()
                print(f"NFA for regular expression 'c*&(a|b&c*)*' with value '{no_ac.val}' is")
                for s in ['', 'a', 'b', 'ccc', 'abcccaabc', 'ac', 'babcacc']:
                    print(f"regx {no_ac.val} : string '{s}' -> {no_ac > s}")
                print()
                
                no111 = (e|i|i&i)&(o|o&i|o&i&i).star()
                print(f"NFA for regular expression '(#|1|11)(0|01|011)*' with value '{no111.val}' is")
                for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
                    print(f"regx {no111.val} : string '{s}' -> {no111 > s}")
                print()
                
                x = b.star()|(b.star()&a&b.star()&a&b.star()&a&b.star()).star() # no.of a's divisible by 3
                print(f"NFA for regular expression 'b*|(b*ab*ab*ab*)*' with value '{x.val}' is")
                for s in ['', 'ab', 'baabbab', 'bbaa', 'aaa', 'aababbbaaab', 'aaaabaaaaa', 'babaabaa']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                no111 = o.star() | o.star()&(i|i&i)&(o&o.star()&(i|i&i)).star()&o.star()
                print(f"NFA for regular expression '0*U0*(1U11)(00*(1U11))*0*' with value '{no111.val}' is")
                for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
                    print(f"regx {no111.val} : string '{s}' -> {no111 > s}")
                print()
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

    def testRegxMix44(self):
        checkFileName = 'testRegxMix44' + '.good'
        outFileName = 'testRegxMix44' + '.out'

        with open(outFileName, 'w') as outf:
            with redirect_stdout(outf):
                
                x = regx('c*(aUbc*)*')
                for s in ['', 'a', 'b', 'ccc', 'abcccaabc', 'ac', 'babcacc']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('(#U1U11)(0U01U011)*')
                for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('b* U (b*ab*ab*ab*)*') # no.of a's divisible by 3
                for s in ['', 'ab', 'baabbab', 'bbaa', 'aaa', 'aababbbaaab', 'aaaabaaaaa', 'babaabaa']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
                x = regx('0* U 0*(1U11)(00*(1U11))*0*') 
                for s in ['', '0', '1', '11', '01101', '11010001101', '111', '001110', '0110001011101']:
                    print(f"regx {x.val} : string '{s}' -> {x > s}")
                print()
                
        with open(outFileName) as outf:
            outStr = outf.read()
        with open(checkFileName) as f:
            checkStr = f.read()

        self.assertEqual(outStr, checkStr)

if __name__ == '__main__':
    unittest.main()
