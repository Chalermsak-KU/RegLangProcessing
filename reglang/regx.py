"""
Package For Processing Finite Automata And Regular Expressions - version 1.0
Written by Chalermsak Chatdokmaiprai, Email: chalermsak.c@ku.th
First Release Date: April 11, 2020

Copyright 2020 Chalermsak Chatdokmaiprai

License: http://creativecommons.org/licenses/by-sa/4.0/
"""

import copy

class regx:
    '''represents a regular expression
    Attributes:
        val : the text string of the regular expression with the 
              following special symbols:
              U (union), * (star), @ (the empty set), # (the empty string) 
              and parentheses.
        nfa : the NFA that accepts the language of the regular expression
    '''

    def __init__(self, val='@'):  # '@' means the empty set
        if len(val) == 1:
            self.val = val
            if val == '@':  # represents the empty set
                deldict = dict()
            elif val == '#':  # represents the empty string
                deldict = { (1, ''):{2} }
            else: # represents a single symbol
                deldict = { (1, val):{2} }
            self.nfa = nfa.nfa(delta=deldict, start=1, finals={2})
        else: # not a singleton expression
            postfixlist, errmsg = regx_parser(val)
            if postfixlist == None:
                raise ValueError(errmsg)
            r = regx._eval_regx_postfix(postfixlist)
            self.val, self.nfa = r.val, r.nfa

    def __str__(self):
        return self.val

    def __repr__(self):
        return 'regx(' + repr(self.val) + ')';

    def __or__(self, other):  # operator | means union
        '''Assumes <self> and <other> are both regx objects.
           Returns a new regx object that are the union of <self> and <other>.
        '''
        # calculate the resultant regx string
        rlist = [r for r in [self.val, other.val] if r != '@']
        valstring = 'U'.join(rlist)
        val = valstring if valstring != '' else '@'

        # construct an NFA for the resultant regx
        nstatesSelf = len(self.nfa.states)
        nstatesOther = len(other.nfa.states)
        lhs_nfa = self.nfa.renumbered(1)
        rhs_nfa = other.nfa.renumbered(nstatesSelf+1)
        newstart = nstatesSelf + nstatesOther + 1
        newfinal = newstart + 1
        newdelta = dict([x for x in lhs_nfa.delta.items()] + [x for x in rhs_nfa.delta.items()])
        newdelta[newstart, ''] = {lhs_nfa.start, rhs_nfa.start}
        for f in lhs_nfa.finals:
            newdelta[f, ''] = {newfinal}
        for f in rhs_nfa.finals:
            newdelta[f, ''] = {newfinal}

        result = regx()
        result.val = val
        result.nfa = nfa.nfa(delta=newdelta, start=newstart, finals={newfinal})
        #print(); print(result.nfa) # debug
        return result

    def __and__(self, other):  # operator & means concatenation
        '''Assumes <self> and <other> are both regx objects.
           Returns a new regx object that are the concatenation of <self> and <other>.
        '''
        if self.val == '@' or other.val == '@': # at least one is the empty set
            return regx('@')

        # calculate the resultant regx string
        if self.val == '#':
            if other.val == '#': # both are epsilons
                val = '#'
            else:
                val = other.val
        else:
            if other.val == '#': # only self is not the epsilon
                val = self.val
            else: # both are not epsilons
                val =  '(' + self.val + ')'  if 'U' in self.val  else self.val
                val += '(' + other.val + ')' if 'U' in other.val else other.val

        # construct an NFA for the resultant regx
        nstatesSelf = len(self.nfa.states)
        nstatesOther = len(other.nfa.states)
        lhs_nfa = self.nfa.renumbered(1)
        rhs_nfa = other.nfa.renumbered(nstatesSelf+1)
        newdelta = dict([x for x in lhs_nfa.delta.items()] + [x for x in rhs_nfa.delta.items()])

        # merge the final state of lhs_nfa with the start state of rhs_dfa
        assert len(lhs_nfa.finals) == 1
        for f in lhs_nfa.finals:
            break  # because there is only one final state which f now is.
        for u in list(rhs_nfa.sigma) + ['']:
            if (rhs_nfa.start, u) in newdelta:
                newdelta[f, u] = newdelta[rhs_nfa.start, u]
                del newdelta[rhs_nfa.start, u]

        result = regx()
        result.val = val
        result.nfa = nfa.nfa(delta=newdelta, start=lhs_nfa.start, finals=rhs_nfa.finals)
        return result

    def star(self):
        '''Assumes <self> is a regx object.
           Returns a new regx object that are the Kleene Star of <self>.
        '''
        # calculate the resultant regx string
        if self.val == '@' or self.val == '#' :  # empty set or epsilon
            return regx('#')
        val = '(' + self.val + ')*' if len(self.val) > 1 else self.val + '*'

        # construct an NFA for the resultant regx
        self_nfa = self.nfa.renumbered(1)
        nstates = len(self_nfa.states)
        newdelta = dict([x for x in self_nfa.delta.items()])
        newstart = nstates + 1
        newfinal = newstart + 1
        newdelta[newstart, ''] = {self_nfa.start, newfinal}
        for f in self_nfa.finals:
            newdelta[f, ''] = {self_nfa.start, newfinal}

        result = regx()
        result.val = val
        result.nfa = nfa.nfa(delta=newdelta, start=newstart, finals={newfinal})
        return result

    def gen(self, s):
        '''Returns True if the regx <self> generates the string <s>, 
        or False otherwise.
        '''
        return self.nfa.accept(s)
        
    def __gt__(self, s):  # operator > means "generates the string"
        '''Returns True if the regx <self> generates the string <s>, 
        or False otherwise. This method is identical to the method gen() above.
        '''
        return self.nfa.accept(s)

    def to_nfa(self):
        '''Returns a (new) nfa object that accepts the language defined by 
        the regx <self>.
        Note that the returned nfa is just a deep copy of self.nfa
        '''
        return copy.deepcopy(self.nfa)

    def to_dfa(self):
        '''Returns a (new) dfa object that accepts the language defined by 
        the regx <self>. The returned dfa is a minimized, standard-numbered one.
        '''
        return self.nfa.to_dfa().renumbered().minimized().standard_numbered()

    def equiv(self, other):
        '''Assumes <self> and <other> are both regx objects.
           Checks if they are equivalent, meaning that they define the same
           language.
           Returns True if they are equivalent, False otherwise.
        '''
        return self.nfa.equiv(other.nfa)

    def __eq__(self, other):  # exactly the same as equiv() above
        return self.nfa.equiv(other.nfa)

    @staticmethod
    def _eval_regx_postfix(pfxlist):
        '''Assumes <pfxlist> is a list of postfix regular expression
           as is returned from the function regx_parser().
           
           Returns a regx object representing the given postfix regular
           expression.
        '''
        valstack = list()
        for item in pfxlist:
            if item == '*':
                operand1 = valstack.pop()
                valstack.append(operand1.star())
            elif item == '&':
                operand2 = valstack.pop()
                operand1 = valstack.pop()
                valstack.append(operand1 & operand2)
            elif item == 'U':
                operand2 = valstack.pop()
                operand1 = valstack.pop()
                valstack.append(operand1 | operand2)
            else: # a symbol in the regular language
                valstack.append(regx(item))
        assert len(valstack) == 1
        return valstack[0]

# --- end of class regx --- #

def go():
    print('Hi there! I am a regx module.')

from reglang import dfa
from reglang import nfa
from reglang.util import prettySetStr
from reglang.regx_parser import regx_parser
if __name__ == '__main__':
    go()

