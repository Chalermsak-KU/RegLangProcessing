# Makefile for testing fa.py (for Unix-like System)
# Author: Chalermsak Chatdokmaiprai
# Organization: Dept. of Computer Engineering, Kasetsart University,
#               Bangkok, Thailand.
# Email Address: chalermsak.c@ku.th

PYTHON = python3
TESTDIR = .


fa.py: test

clean:
	cd $(TESTDIR); rm -f test*.out

test: t_msg testDFA testNFA testRegx

testDFA: testDfaDef testDfaAcpt testReachable testMinDFA testRenumberDFA testStanNumDFA testDfaToNfa testComplementDFA testDFAtoRegx testEqualDFA testEquivDFA testDfaEquivNfa

testNFA: testNfaDef testEClosure testNfaToDfa testNfaAcpt testNFAtoRegx testRenumberNFA testEquivNfa testNfaEquivDfa

testRegx: testRegxConstructor testPrimRegxGen testRegxOp testRegxToNfa testRegxToDfa testRegxEquiv

testDfaDef: testDfaDef1 testDfaDef2

testDfaAcpt: testDfaAcpt1 testDfaAcpt2 testDfaAcpt3 testDfaAcpt4

testReachable: testReachable1

testMinDFA: testMinDFA1 testMinDFA2 testMinDFA3 testMinDFA4 testMinDFA5 testMinDFA6

testRenumberDFA: testRenumberDFA1

testStanNumDFA: testStanNumDFA1 testStanNumDFA2

testDfaToNfa: testDfaToNfa1 testDfaToNfa2 testDfaToNfa3 

testComplementDFA: testComplementDFA1 testComplementDFA2 testComplementDFA3

testDFAtoRegx: testDFAtoRegx1 testDFAtoRegx2 testDFAtoRegx3 testDFAtoRegx4

testEqualDFA: testEqualDFA1 testEqualDFA2

testEquivDFA: testEquivDFA1 testEquivDFA2 testEquivDFA3 testEquivDFA4 testEquivDFA5 testEquivDFA6 testEquivDFA7 

testDfaEquivNfa: testDfaEquivNfa1 testDfaEquivNfa2 testDfaEquivNfa3 

testNfaDef: testNfaDef1 testNfaDef2

testEClosure: testEClosure1 testEClosure2

testNfaToDfa: testNfaToDfa1 testNfaToDfa2 testNfaToDfa3 testNfaToDfa4 testNfaToDfa5

testNfaAcpt: testNfaAcpt1 testNfaAcpt2 testNfaAcpt3

testNFAtoRegx: testNFAtoRegx1 testNFAtoRegx2 testNFAtoRegx3 testNFAtoRegx4 testNFAtoRegx5

testRenumberNFA: testRenumberNFA1

testEquivNfa: testEquivNfa1 testEquivNfa2 

testNfaEquivDfa: testNfaEquivDfa1 testNfaEquivDfa2 testNfaEquivDfa3 

testRegxConstructor: testRegxConstructor1 

testPrimRegxGen: testPrimRegxGen1 

testRegxOp: testRegxUnion testRegxCat testRegxStar testRegxMix

testRegxUnion: testRegxOp1 testRegxOp2 testRegxOp3 testRegxOp4 

testRegxCat: testRegxOp11 testRegxOp22 testRegxOp33 testRegxOp44 

testRegxStar: testRegxStar1

testRegxMix: testRegxMix1 testRegxMix2 testRegxMix3 testRegxMix4 testRegxMix11 testRegxMix22 testRegxMix33 testRegxMix44

testRegxToNfa: testRegxToNfa1

testRegxToDfa: testRegxToDfa1 testRegxToDfa2 testRegxToDfa3 testRegxToDfa4 

testRegxEquiv: testRegxEquiv1 testRegxEquiv2 testRegxEquiv3

t_msg:
	@echo
	@echo '   ** TESTING fa.py **'
	@echo
	@echo 'Any output from "diff" is a bad news.'
	@echo '----------'
#	@echo 'Press ENTER to continue.'
#	@read x

testDfaDef1:
	@echo 'Test: initializing and printing a DFA object - (01 U 010)* DFA'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaDef2:
	@echo 'Test: initializing and printing a DFA object - the empty-set language'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaAcpt1:
	@echo 'Test: DFA accepting a string in (01 U 010)* : state names are strings'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaAcpt2:
	@echo 'Test: DFA accepting a string in the empty-set language'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaAcpt3:
	@echo 'Test: DFA accepting a string in (ab U ba)* '
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaAcpt4:
	@echo 'Test: DFA accepting a string in (01 U 010)* : state names are integers '
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testReachable1:
	@echo 'Test: removes nonreachable states from a DFA'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testMinDFA1:
	@echo 'Test: Minimization of DFA - DFA in L&P p94 - L&P algo'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testMinDFA2:
	@echo 'Test: Minimization of DFA - DFA in L&P p93 (has nonreachables) - L&P algo'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testMinDFA3:
	@echo 'Test: Minimization of DFA - # DFA p.156 HMU, 3rd Ed. - L&P algo VS Marking algo'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testMinDFA4:
	@echo 'Test: Minimization of DFA - # DFA Martin, 4th Ed., p.76 - L&P algo VS Marking algo'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testMinDFA5:
	@echo 'Test: Minimization of DFA - # DFA that accepts every string over the alphabet'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testMinDFA6:
	@echo 'Test: Minimization of DFA - DFA in L&P p93, minimization includes removal of nonreachables'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaDef1:
	@echo 'Test: initializing and printing a NFA object - NFA fig 2.9 p.70 L&P'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaDef2:
	@echo 'Test: initializing and printing a NFA object - NFA p75 ex.2.2.9(a) L&P: language a*b(aUb)'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEClosure1:
	@echo 'Test: Epsilon-Closure of an NFA object - NFA fig 2.9 p.70 L&P'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEClosure2:
	@echo 'Test: Epsilon-Closure of an NFA object - more comprehensive'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaToDfa1:
	@echo 'Test: NFA-to-DFA conversion - NFA fig 2.9 p70 L&P'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaToDfa2:
	@echo 'Test: NFA-to-DFA conversion - NFA ex.2.2.6 (a): L = (ab U aab U aba)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaToDfa3:
	@echo 'Test: NFA-to-DFA conversion - NFA p75 ex.2.2.9(a) L&P: language a*b(aUb)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaToDfa4:
	@echo 'Test: NFA-to-DFA conversion - another NFA for ex.2.2.6(a): L=(ab U aab U aba)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaToDfa5:
	@echo 'Test: NFA-to-DFA conversion - # another NFA from page 3 of lecture note about thm2.2.1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaAcpt1:
	@echo 'Test: NFA as an acceptor - NFA p75 ex.2.2.9(a) L&P: language a*b(aUb)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaAcpt2:
	@echo 'Test: NFA as an acceptor - NFA fig 2.9 p.70 L&P, language: (aa* U aa*b U b)(ep U (aUb)a*)'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaAcpt3:
	@echo 'Test: NFA as an acceptor - NFA ex.2.2.6 (a): L = (ab U aab U aba)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNFAtoRegx1:
	@echo 'Test: NFA-to-RegExp Conversion - # NFA L&P p.81'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNFAtoRegx2:
	@echo 'Test: NFA-to-RegExp Conversion - # NFA L&P exercise 2.3.7a'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNFAtoRegx3:
	@echo 'Test: NFA-to-RegExp Conversion - # NFA L&P exercise 2.3.7d'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNFAtoRegx4:
	@echo 'Test: NFA-to-RegExp Conversion - NFA example in the sheet'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNFAtoRegx5:
	@echo 'Test: NFA-to-RegExp Conversion - NFA example in the slides'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRenumberNFA1:
	@echo 'Test: Renumbered-state NFA - NFA example in the sheet'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxConstructor1:
	@echo 'Test: regular expression constructor #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testPrimRegxGen1:
	@echo 'Test: primitive regular expressions as string generators #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp1:
	@echo 'Test: regx operations - Union'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp2:
	@echo 'Test: regx operations - Union with empty string'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp3:
	@echo 'Test: regx operations - Union with empty set'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp4:
	@echo 'Test: regx operations - Union of emptyString and emptySet'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp11:
	@echo 'Test: regx operations - Concatenation'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp22:
	@echo 'Test: regx operations - Concatenation with empty string'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp33:
	@echo 'Test: regx operations - Concatenation with empty set'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxOp44:
	@echo 'Test: regx operations - Concat of emptyString and emptySet'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxStar1:
	@echo 'Test: regx operations - Star'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix1:
	@echo 'Test: regx operations - Mixed Operations #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix2:
	@echo 'Test: regx operations - Mixed Operations #2'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix3:
	@echo 'Test: regx operations - Mixed Operations #3'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix4:
	@echo 'Test: regx operations - Mixed Operations #4'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix11:
	@echo 'Test: regx expression parsing #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix22:
	@echo 'Test: regx expression parsing #2'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix33:
	@echo 'Test: regx expression parsing #3'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxMix44:
	@echo 'Test: regx expression parsing #4'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRenumberDFA1:
	@echo 'Test: Renumbered-state DFA - DFA example in the sheet'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testStanNumDFA1:
	@echo 'Test: Standard-numbered-state DFA - all states reachable'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testStanNumDFA2:
	@echo 'Test: Standard-numbered-state DFA - some states are unreachable'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaToNfa1:
	@echo 'Test: DFA-to-NFA conversion: #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaToNfa2:
	@echo 'Test: DFA-to-NFA conversion: #2'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaToNfa3:
	@echo 'Test: DFA-to-NFA conversion: #3'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testComplementDFA1:
	@echo 'Test: Complement DFA: #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testComplementDFA2:
	@echo 'Test: Complement DFA: #2'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testComplementDFA3:
	@echo 'Test: Complement DFA: #3'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDFAtoRegx1:
	@echo 'Test: DFA-to-regx conversion: #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDFAtoRegx2:
	@echo 'Test: DFA-to-regx conversion: #2'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDFAtoRegx3:
	@echo 'Test: DFA-to-regx conversion: #3'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDFAtoRegx4:
	@echo 'Test: DFA-to-regx conversion: #4'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEqualDFA1:
	@echo 'Test: Equality of two DFAs: #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEqualDFA2:
	@echo 'Test: Equality of two DFAs: #2'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxToNfa1:
	@echo 'Test: regx-to-NFA conversion: #1'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivDFA1:
	@echo 'Test: Equivalence of two DFAs #1: exactly the same DFAs'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivDFA2:
	@echo 'Test: Equivalence of two DFAs #2: DFAs differs only in state names'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivDFA3:
	@echo 'Test: Equivalence of two DFAs #3: Both accepts {w in {a,b,c}*: w does not contain ac}'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivDFA4:
	@echo 'Test: Equivalence of two DFAs #4: Both accepts every string in {a,b,c}*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivDFA5:
	@echo 'Test: Equivalence of two DFAs #5: Both accepts the empty set'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivDFA6:
	@echo 'Test: Equivalence of two DFAs #6: Both accepts the empty set but have different alphabets'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivDFA7:
	@echo 'Test: Equivalence of two DFAs #7: non-equivalent DFAs'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivNfa1:
	@echo 'Test: Equivalence of two NFAs #1: four equivalent NFAs'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testEquivNfa2:
	@echo 'Test: Equivalence of two NFAs #2: four non-equivalent NFAs'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaEquivNfa1:
	@echo 'Test: a DFA is equivalent to an NFA #1: test equivalence (01U010)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaEquivNfa2:
	@echo 'Test: a DFA is equivalent to an NFA #2: test non-equivalence'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testDfaEquivNfa3:
	@echo 'Test: a DFA is equivalent to an NFA #3: test equivalence (0U1)*10'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaEquivDfa1:
	@echo 'Test: an NFA is equivalent to a DFA #1: test equivalence (01U010)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaEquivDfa2:
	@echo 'Test: an NFA is equivalent to a DFA #2: test non-equivalence'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testNfaEquivDfa3:
	@echo 'Test: an NFA is equivalent to a DFA #3: test equivalence (0U1)*10'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxEquiv1:
	@echo "Test: Equivalence of two regx's #1: strings in {a,b,c}* that have no ac"
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxEquiv2:
	@echo "Test: Equivalence of two regx's #2: binary strings that have no 111"
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxEquiv3:
	@echo "Test: Equivalence of two regx's #3: binary strings that ends with 10"
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxToDfa1:
	@echo 'Test: regx-to-DFA conversion: #1 : c*(aUbc*)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxToDfa2:
	@echo 'Test: regx-to-DFA conversion: #2 : (0U1)*111(0U1)*'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxToDfa3:
	@echo 'Test: regx-to-DFA conversion: #3 : # (the set of the empty string)'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

testRegxToDfa4:
	@echo 'Test: regx-to-DFA conversion: #4 : @ (the empty set)'
	@echo '----------'
	PYTHONPATH=.. $(PYTHON) $(TESTDIR)/$@.py >$@.out
	diff $@.out $@.good && rm -f $@.out
	@echo '----------'

