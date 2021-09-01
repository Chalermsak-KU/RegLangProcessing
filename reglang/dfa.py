"""
Package For Processing Finite Automata And Regular Expressions - version 1.0
Written by Chalermsak Chatdokmaiprai, Email: chalermsak.c@ku.th
First Release Date: April 11, 2020

Copyright 2020 Chalermsak Chatdokmaiprai

License: http://creativecommons.org/licenses/by-sa/4.0/
"""

import copy

emptyset = frozenset()

class dfa:
    '''represents a deterministic finite automata (DFA)
    Attributes:
        states : the set of all states (represented by any python immutable object)
        sigma  : the input alphabet
        delta  : the transition function from states x sigma to states
        start  : the start state
        finals : the set of all final states
    '''

    def __init__(self, delta, start, finals):
        '''Assumes that
        <delta> is a dictionary that represents the transition function.
            It maps the tuple (<state>, <symbol>) to <state>, where <state> can be 
            either string or integer and <symbol> is a single-char string. 
            The given <delta> may be a partial function in which case a hell state 
            will be automatically added to make <delta> a total function.
        <start> is the start state
        <finals> is the (python) set of final states
        
        The dfa object's attributes <states> and <sigma> are derived from the 
        three arguments above.  A trap state may be added to <states> make <delta> 
        a total function if the given <delta> is not.
        '''
        self.states = {start}.union(finals)
        self.sigma = set()
        self.delta = delta
        self.start = start
        self.finals = finals

        if isinstance(start, int):
            trapState = -999
        elif isinstance(start, str):
            trapState = '_H_'
        elif isinstance(start, tuple):
            trapState = ()
        else:
            trapState = None

        # extract states and sigma from delta
        for state, sym in self.delta:
            self.states.add(state)
            self.states.add(self.delta[state, sym])
            if sym == '':
                raise ValueError("input symbol of DFA can't be the empty string")
            self.sigma.add(sym)
        if self.sigma == set():
            self.sigma = {'0'}  # default alphabet

        # next, make delta a total function by adding a hell state if needed
        add_trap = False
        for state in self.states:
            for sym in self.sigma:
                if (state, sym) not in self.delta:
                    self.delta[state, sym] = trapState
                    add_trap= True
        if add_trap:
            self.states.add(trapState)
            for c in self.sigma:
                self.delta[trapState, c] = trapState

    def __str__(self):
        s =  [f'states = {prettySetStr(self.states)}']
        s.append(f'sigma = {prettySetStr(self.sigma)}')
        s.append(f'start = {repr(self.start)}')
        s.append(f'finals = {prettySetStr(self.finals)}')
        s.append('delta = {')
        sorted_keystrlist = sorted([repr(x) for x in self.delta.keys()])
        for keystr in sorted_keystrlist:
            s.append(f'    {keystr} : {repr(self.delta[eval(keystr)])}')
        #for key, val in sorted(self.delta.items()):
        #    s.append(f'    {key} : {val}')
        s.append('}')
        return '\n'.join(s)

    def __repr__(self):
        s = list()
        s.append(f'dfa(start = {repr(self.start)},')
        s.append(f'    finals = {prettySetStr(self.finals)},')
        s.append( '    delta = {')
        sorted_keystrlist = sorted([repr(x) for x in self.delta.keys()])
        for keystr in sorted_keystrlist:
            s.append(f'      {keystr} : {repr(self.delta[eval(keystr)])},')
        s.append('    })')
        return '\n'.join(s)

    def __eq__(self, other):
        '''Assumes that <self> and <other> are dfa objects.
        Checks if they are equal dfas (overloading ==).
           By equal dfas, we mean that their sets of states, their sets of 
        input symbols, their start states, their sets of final states, and 
        their delta functions are mathematically equal.
           Returns True if they are equal, False otherwise.
        '''
        if self.states != other.states:
            return False
        if self.sigma != other.sigma:
            return False
        if self.start != other.start:
            return False
        if self.finals != other.finals:
            return False
        for state, sym in self.delta:
            if self.delta[state, sym] != other.delta[state, sym]:
                return False
        return True

    def equiv(self, other):
        '''Assumes <self> is a dfa and <other> is either a dfa or an nfa.
        Checks if they are equivalent, meaning that they accept the same
        language.
           Returns True if they are equivalent, False otherwise.
        '''
        stan_self = self.minimized().standard_numbered()
        if isinstance(other, nfa.nfa):  # nfa needs to be converted to dfa first
            other = other.to_dfa()
        stan_other = other.minimized().standard_numbered()
        return stan_self == stan_other

    def accept(self, w):
        '''Assumes <w> is a string.
           Returns True if the DFA <self> accepts <w>, or False otherwise'''
        state = self.start
        for sym in w:
            if sym not in self.sigma:
                raise ValueError(f"symbol '{sym}' not in the DFA's input alphabet")
            state = self.delta[state, sym]
        return state in self.finals

    def to_nfa(self):
        '''Assumes <self> is a DFA.
           Returns a new NFA that is equivalent to the given DFA <self>'''
        nfa_start = self.start
        nfa_finals = self.finals
        nfa_delta = { (state,sym):{self.delta[state,sym]} for state,sym in self.delta }
        new_nfa = nfa.nfa(delta=nfa_delta, start=nfa_start, finals=nfa_finals)
        return new_nfa

    def to_regx(self):
        '''finds and returns a regular expression (regx object) for the language of DFA <self>
        '''
        return self.to_nfa().to_regx()

    def renumbered(self, startnum=1):
        '''Assumes <startnum> is an integer.
           Creates a new DFA which is identical to the DFA <self> 
           except that the state names are renumbered starting from 
           <startnum> onwards.
           
           Returns the new renumbered DFA.
        '''
        statelist = list(self.states)
        nstates = len(statelist)
        sid = {statelist[i] : startnum + i for i in range(nstates)}
        #print(sid) # debug

        newdelta = dict()
        for state, sym in self.delta:
            newdelta[sid[state], sym] = sid[self.delta[state, sym]]

        newstart = sid[self.start]
        newfinals = {sid[q] for q in self.finals}

        return dfa(delta=newdelta, start=newstart, finals=newfinals)

    def standard_numbered(self):
        '''Returns a new DFA that is essentially identical to the given DFA 
           <self> but has has all states renumbered in a standard way where 
           the start state is numbered 1 and the other states are numbered 
           2, 3, ... and so on. The state are numbered in the order of their 
           appearances in the algorithm for finding reachable states. 
           Incidentally, as a by-product, all nonreachable states are removed.
        '''
        new_id = dict()
        next_id = 1
        sorted_sigma = sorted(self.sigma)
        reachable_set = {self.start}
        new_id[self.start] = next_id; next_id += 1
        que = [self.start]
        while que != []:
            h = que.pop(0)
            for c in sorted_sigma:
                to_state = self.delta[h, c]
                if to_state not in reachable_set: # new reachable state
                    reachable_set.add(to_state)
                    que.append(to_state)
                    new_id[to_state] = next_id; next_id += 1

        # Use the computed reachable set to construct a new DFA
        newdelta = dict()
        for state, sym in self.delta:
            if state in reachable_set:
                newdelta[new_id[state], sym] = new_id[self.delta[state, sym]]
        newstart = new_id[self.start]
        newfinals = {new_id[q] for q in self.finals.intersection(reachable_set)}
        newDFA = dfa(delta=newdelta, start=newstart, finals=newfinals)
        return newDFA

    def complement(self):
        '''Returns a new DFA that accepts the language which is the complement
           of the language accepted by the given DFA <self>
        '''
        dfacomp = copy.deepcopy(self)
        dfacomp.finals = self.states - self.finals
        return dfacomp

    def remove_nonreachable(self):
        '''Returns a new DFA that is equivalent to the given DFA <self>
           but has no nonreachable states.
        '''
        reachable_set = {self.start}
        que = [self.start]
        while que != []:
            h = que.pop(0)
            for c in self.sigma:
                to_state = self.delta[h, c]
                if to_state not in reachable_set:
                    reachable_set.add(to_state)
                    que.append(to_state)

        # Use the computed reachable set to construct a new DFA
        newdelta = dict()
        for state, sym in self.delta:
            if state in reachable_set:
                newdelta[state, sym] = self.delta[state, sym]
        newfinals = self.finals.intersection(reachable_set)
        newDFA = dfa(delta=newdelta, start=self.start, finals=newfinals)
        return newDFA

    def minimized1(self, verbose=False):
        '''Returns a minimized DFA equivalent to the given DFA <self>,
        using the algorithm as described in L&P text.
        
        Note that the dfa <self> is assumed to have no nonreachable states.
        '''

        def build_partition(eclass):
            pdict = dict()
            for state in self.states:
                pdict.setdefault(eclass[state], set()).add(state)
            for classid in pdict:
                pdict[classid] = tuple(sorted(pdict[classid]))
            return pdict

        def print_partition(pdict):
            for classid in pdict:
                print(f' {pdict[classid]}', end='')
            print()

        # map each state to its first-round equiv class id (final or nonfinal)
        eclass = dict()
        for state in self.states:
            eclass[state] = (0,) if state in self.finals else (1,)
        nclasses = len(set(eclass.values()))  # can be 1 if the states are all final or all nonfinal.
        #if verbose:
        #    print('eclass:') # debug
        #    print(eclass) # debug
        
        # show first partitioning - for debugging - can be commented out
        if verbose:
            pdict = build_partition(eclass)
            print('First partitioning:')
            print_partition(pdict)

        # each iteration determines a new set of finer equiv classes
        while True:
            # compute next equivalent class id for each state
            new_eclass = dict()
            for state in self.states:
                new_classid = list(eclass[state])
                for c in self.sigma:
                    new_classid += list(eclass[self.delta[state, c]])
                new_eclass[state] = tuple(new_classid)

            #if verbose:
            #    print('eclass:') # debug
            #    print(new_eclass) # debug

            # check whether the new equiv classes are really finer than previous round.
            new_nclasses = len(set(new_eclass.values()))
            if new_nclasses > nclasses:  # new partition is finer than previous one
                # new partition is still finer, so next round is necessary
                eclass = new_eclass
                nclasses = new_nclasses

                # show new partitioning - for debugging - can be commented out
                if verbose:
                    pdict = build_partition(eclass)
                    print('Next partitioning:')
                    print_partition(pdict)
            else:  # new partition is the same as the previous one
                #print(f'new_nclasses is {new_nclasses}, nclasses is {nclasses}')  # debug
                assert new_nclasses == nclasses
                break

        # final partitioning (necessary - can't be commented out)
        pdict = build_partition(eclass)
        if verbose:
            print('Final partitioning:')
            print_partition(pdict)

        # constructing the minimized DFA from the equiv classes
        minDFAdelta = dict()
        minDFAfinals = set()
        for classid in pdict:
            statetuple = pdict[classid]
            if self.start in statetuple:
                minDFAstart = statetuple
            q = statetuple[0]  # extract any one state
            if q in self.finals:
                minDFAfinals.add(statetuple)
            for c in self.sigma:
                minDFAdelta[statetuple, c] = pdict[eclass[self.delta[q, c]]]

        minDFA = dfa(delta=minDFAdelta, start=minDFAstart, finals=minDFAfinals)
        return minDFA

    def minimized2(self, verbose=False):
        '''Returns a minimized DFA equivalent to the given DFA <self>,
        using the table-marking algorithm such as described in H&U text.
        
        Note that the dfa <self> is assumed to have no nonreachable states.
        '''

        def print_table():
            print(f'|{1}_{s[1]}_')
            for j in range(2, nstates+1):
                for i in range(1, j):
                    print(f' {tab[i, j]}', end='')
                print(f'|{j}_{s[j]}_')

        def is_still_equiv(state1, state2):
            for sym in self.sigma:
                s1_to = sid[self.delta[state1, sym]]
                s2_to = sid[self.delta[state2, sym]]
                if s1_to < s2_to:
                    if tab[s1_to, s2_to] > 0:  # is marked
                        return False
                elif s1_to > s2_to:
                    if tab[s2_to, s1_to] > 0:  # is marked
                        return False
            return True

        # map a sequence number to each state and inversely
        statelist = list(self.states)
        nstates = len(statelist)
        sid = {statelist[i] : i+1 for i in range(len(statelist))}
        #print(sid) # debug
        s = {i+1 : statelist[i] for i in range(len(statelist))}
        #print(s) # debug

        # create a table of state pairs and initialize it
        tab = dict()
        for i in range(1, nstates):
            for j in range(i+1, nstates+1):
                if (s[i] in self.finals) == (s[j] in self.finals):
                    tab[i, j] = 0
                else:
                    tab[i, j] = 1
        if verbose:
            print_table() # debug

        # the famous marking algorithm
        marknum = 1
        has_newmark = True
        while has_newmark:
            has_newmark = False
            marknum += 1
            for i in range(1, nstates):
                for j in range(i+1, nstates+1):
                    #print('check: ', i, j) # debug
                    if tab[i, j] == 0 and not is_still_equiv(s[i], s[j]):
                        tab[i, j] = marknum
                        has_newmark = True
            if has_newmark and verbose:   # debug
                print_table() # debug

        # determine the equivalent class of each state, using algo from Martin's text
        classnum = 0
        eclass = dict()
        eclass[1] = classnum
        for stateid in range(2, nstates+1):
            newclass = True
            for previous in range(1, stateid):
                if tab[previous, stateid] == 0:
                    eclass[stateid] = eclass[previous]
                    newclass = False
                    break
            if newclass:
                classnum += 1
                eclass[stateid] = classnum
        #if verbose:
        #    print('eclass:'); print(eclass) # debug

        # create a partition according to the equivalence classes
        plist = [set() for i in range(classnum+1)]
        for stateid in range(1, nstates+1):
            plist[eclass[stateid]].add(s[stateid])
        plist = [tuple(sorted(x)) for x in plist]
        if verbose:
            print('plist:'); print(plist) # debug

        # constructing the minimized DFA from the equiv classes
        minDFAdelta = dict()
        minDFAfinals = set()
        for statetuple in plist:
            if self.start in statetuple:
                minDFAstart = statetuple
            q = statetuple[0]  # extract any one state
            if q in self.finals:
                minDFAfinals.add(statetuple)
            for c in self.sigma:
                minDFAdelta[statetuple, c] = plist[eclass[sid[self.delta[q, c]]]]

        minDFA = dfa(delta=minDFAdelta, start=minDFAstart, finals=minDFAfinals)
        return minDFA

    def minimized(self, verbose=False):
        '''Returns a minimized DFA equivalent to the given DFA <self>.
        Unlike the methods minimized1() and minimized2() above, this method
        first eliminates all existing nonreachable states before doing the
        minimization.
        
        This function actually calls the above method minimized1()
        '''
        return self.remove_nonreachable().minimized1(verbose)

def go():
    print('Hi there! I am a dfa module.')

from . import nfa
from .util import prettySetStr
if __name__ == '__main__':
    go()

