"""
Package For Processing Finite Automata And Regular Expressions - version 1.0
Written by Chalermsak Chatdokmaiprai, Email: chalermsak.c@ku.th
First Release Date: April 11, 2020

Copyright 2020 Chalermsak Chatdokmaiprai

License: http://creativecommons.org/licenses/by-sa/4.0/
"""

import copy

emptyset = frozenset()

class nfa:
    '''represents a nondeterministic finite automata (NFA)
    Attributes:
        states : the set of all states (represented by any immutable object)
        sigma  : the input alphabet
        delta  : the transition (partial) function from states X sigma to 
                 the powerset of states
        start  : the start state
        finals : the set of all final states
        _decider : the dynamically-growing, partial DFA (object) that serves as 
                  the nfa's deterministic decider. The method accept() will 
                  incrementally add new states to this _decider as needed.
        _Rdict : a dict to be used internally by the method _R()
        _SNFA : a simplified NFA to be used internally by the method snfa()
    '''

    def __init__(self, delta, start, finals):
        '''Assumes that
        <delta> is a dictionary that represents the transition function.
            It maps the tuple (<state>, <symbol>) to <state>, where <state> 
            can be any python immutable object and <symbol> is a single-char 
            string.
        <start> is the start state
        <finals> is the (python) set of final states
        
        The attributes <states> and <sigma> are automatically derived from 
        the three arguments above.

        The attribute <_decider> is initialized to be a partial DFA with only 
        the start state.

        The attributes <_Rdict> and <_SNFA> are initialized to be their 
        minimal values
        '''
        self.states = {start}.union(finals)
        self.sigma = set()
        self.delta = delta
        self.start = start
        self.finals = finals
        for state, sym in self.delta:
            self.states.add(state)
            self.states.update(self.delta[state, sym])
            if sym != '':
                self.sigma.add(sym)
        self._decider = dfa.dfa(delta=dict(), start=None, finals=set())  # the equivalent (partial) DFA
        self._decider.sigma = self.sigma
        self._decider.start = tuple(sorted(self._ep_closure(self.start)))
        self._decider.states = {self._decider.start}
        if set(self._decider.start).intersection(self.finals) != emptyset:
            self._decider.finals.add(self._decider.start)
        self._Rdict = dict()  # using internally by the method _R()
        self._SNFA = None     # using internally by the method snfa()

    def __str__(self):
        s =  [f'states = {prettySetStr(self.states)}']
        s.append(f'sigma = {prettySetStr(self.sigma)}')
        s.append(f'start = {repr(self.start)}')
        s.append(f'finals = {prettySetStr(self.finals)}')
        s.append('delta = {')
        sorted_keystrlist = sorted([repr(x) for x in self.delta.keys()])
        for keystr in sorted_keystrlist:
            s.append(f'    {keystr} : {self.delta[eval(keystr)]}')
        s.append('}')
        return '\n'.join(s)

    def __repr__(self):
        s = list()
        s.append(f'nfa(start = {repr(self.start)},')
        s.append(f'    finals = {prettySetStr(self.finals)},')
        s.append( '    delta = {')
        sorted_keystrlist = sorted([repr(x) for x in self.delta.keys()])
        for keystr in sorted_keystrlist:
            s.append(f'      {keystr} : {self.delta[eval(keystr)]},')
        s.append('    })')
        return '\n'.join(s)

    def equiv(self, other):
        '''Assumes <self> is an nfa and <other> is either a dfa or an nfa.
        Checks if they are equivalent, meaning that they accept the same
        language.
           Returns True if they are equivalent, False otherwise.
        '''
        dfa_self  = self.to_dfa()
        dfa_other = other.to_dfa() if isinstance(other, nfa) else other
        return dfa_self.equiv(dfa_other)

    def _ep_closure(self, state):
        '''Assumes <state> is a state of the NFA <self>.
           Returns the set Epsilon-Closure of <state>, which is the set 
           of all states in the NFA that is reachable from <state> 
           without reading any input.
           
           This set is used in the algorithm converting an NFA to a DFA.
        '''
        closure_set = {state}
        que = [state]
        while que != []:
            h = que.pop(0)
            ep_to_set = self.delta.get((h, ''), emptyset)
            for q in ep_to_set:
                if q not in closure_set:
                    closure_set.add(q)
                    que.append(q)
        return closure_set

    def _calc_DFA_delta(self, Q, sym):
        '''Assumes <Q> is a set of some states in NFA <self> and <sym> 
           is a symbol in NFA's alphabet, so <Q> is in fact a state of 
           the DFA that is being constructed by the NFA-to-DFA conversion
           algorithm described in L&P pp.69-70.

           The set <Q> is in fact implemented as a tuple to make it 
           suitable for its use as part of a key
           (Q, sym) of the transition-function dict object. <sym> is 
           simply a single-char string.

           Computes and returns the value of the DFA's transition 
           function delta(Q, sym) which is another set of NFA's states 
           as defined in L&P p.70.
        '''
        nextstate = set()
        for q in Q:
            to_set = self.delta.get((q, sym), emptyset)
            for p in to_set:
                nextstate.update(self._ep_closure(p))
        return tuple(sorted(nextstate))

    def to_dfa(self):  # NFA-to-DFA conversion algorithm
        '''Returns a DFA equivalent to the given NFA <self>, using 
        the algo described in L&P pp.69-70
        '''
        dstart = tuple(sorted(self._ep_closure(self.start)))
        dstates = {dstart}
        ddelta = dict()
        que = [dstart]
        while que != []:
            Q = que.pop(0)
            for sym in self.sigma:
                P = ddelta[Q, sym] = self._calc_DFA_delta(Q, sym)
                if P not in dstates:
                    que.append(P)
                    dstates.add(P)
        dfinals = {Q for Q in dstates if set(Q).intersection(self.finals) != emptyset}
        newdfa = dfa.dfa(delta=ddelta, start=dstart, finals=dfinals)
        return newdfa

    def _accept0(self, w):
        '''Assume w is a string.
           Returns True if the NFA <self> accepts w, or False otherwise.

           Note: It dynamically builds a new partial DFA just enough 
           to do the job. The partial DFA is discarded when this 
           method returns.

           Note that this method is made obsolete by accept() method below.
        '''
        #print(f'Input is "{w}"') # debug
        n = dfa.dfa(delta=dict(), start=None, finals=set())  # the equivalent DFA
        n.sigma = self.sigma
        n.start = tuple(sorted(self._ep_closure(self.start)))
        n.states = {n.start}
        state = n.start
        for sym in w:
            #print(f'-- At {state}, read {sym}, ', end='')   # debug
            state = n.delta.setdefault((state, sym), self._calc_DFA_delta(state, sym))
            #print(f'go to {state}')   # debug
            n.states.add(state)
        
        # print these for debugging
        '''
        print('Partial DFA:')
        print('\tstart state =' , n.start)
        print('\tstate set =', n.states)
        print('\tdelta = {')
        for key in n.delta:
            print(f'\t  {key} : {n.delta[key]}')
        print('\t}')
        '''

        if set(state).intersection(self.finals) != emptyset:
            #print(f'-- Halt at a final state {state}') # debug
            return True
        else:
            #print(f'-- Halt at a nonfinal state {state}') # debug
            return False

    def accept(self, w):
        '''Assume w is a string.
           Returns True if the NFA <self> accepts w, or False otherwise.

           Note: It is essentially the same as the method _accept0() above 
           but the partial DFA is incrementally built into the 
           <_decider> attribute of the nfa <self> so it is preserved 
           within the nfa.
        '''
        #print(f'Input is "{w}"') # debug
        state = self._decider.start
        for sym in w:
            #print(f'-- At {state}, read {sym}, ', end='')   # debug
            if (state, sym) not in self._decider.delta:
                self._decider.delta[state, sym] = self._calc_DFA_delta(state, sym)
            state = self._decider.delta[state, sym]
            #print(f'go to {state}')   # debug
            if state not in self._decider.states:
                self._decider.states.add(state)
                if set(state).intersection(self.finals) != emptyset:
                    self._decider.finals.add(state)

        # print these for debugging
        '''
        print('Partial DFA:')
        print('\tstart state =' , self._decider.start)
        print('\tstate set =', self._decider.states)
        print('\tfinal set =', self._decider.finals)
        print('\tdelta = {')
        for key in self._decider.delta:
            print(f'\t  {key} : {self._decider.delta[key]}')
        print('\t}')
        '''

        if state in self._decider.finals:
            #print(f'-- Halt at a final state {state}') # debug
            return True
        else:
            #print(f'-- Halt at a nonfinal state {state}') # debug
            return False

    def _R(self, i, j, k, ep=False):
        if (i, j, k) in self._Rdict:
            return self._Rdict[i, j, k]

        if k == 0:
            result = regx.regx('@')
            for c in sorted(self.sigma) + ['']:
                if (i,c) in self.delta and j in self.delta[i, c]:
                    result = result | regx.regx(c if c != '' else '#')
            if ep and i == j:
                result = result | regx.regx('#')
        else:
            assert k > 0
            result = self._R(i,j,k-1,ep) | self._R(i,k,k-1,ep) & self._R(k,k,k-1,ep).star() & self._R(k,j,k-1,ep)

        self._Rdict[i, j, k] = result
        #print(f"_R({i},{j},{k}) = {result if result.val != '@' else '{}'}") # debug
        return result

    def snfa(self):
        '''Creates a new simplified NFA from the given NFA, so as to be 
        suitable for the NFA-to-RegularExpression conversion algorithm as 
        described in L&P. The resulting simplified NFA has the properties
        that (1) it has a single final state and (2) there are no transtions
        into the start state, nor out of the final state.

        The resulting new simpified NFA is returned and also saved as an
        attribute of the given NFA.
        '''
        if self._SNFA != None:
            return self._SNFA

        # map a sequence number to each state and inversely
        statelist = sorted(self.states)
        nstates = len(statelist)
        sid = {statelist[i] : i+1 for i in range(nstates)}
        #print(sid) # debug

        newdelta = dict()
        for state, sym in self.delta:
            newdelta[sid[state], sym] = {sid[q] for q in self.delta[state, sym]}
        newstart = nstates + 1
        newfinal = nstates + 2
        newdelta[newstart, ''] = {sid[self.start]}
        for q in self.finals:
            if (sid[q], '') in newdelta:
                newdelta[sid[q], ''].add(newfinal)
            else:
                newdelta[sid[q], ''] = {newfinal}
        self._SNFA = nfa(delta=newdelta, start=newstart, finals={newfinal}) 
        #print('Simplified NFA:'); print(self._SNFA) # debug
        return self._SNFA

    def to_regx2(self):  # conversion algo from NFA to regular expression - recursive version
        '''finds and returns a regular expression (regx object) for the language of NFA <self>
        '''
        n = self.snfa()
        return n._R(n.start, n.start+1, n.start-1)

    def to_regx1(self): # conversion algo from NFA to regular expression - iterative version
        '''finds and returns a regular expression (regx object) for the language of NFA <self>
        '''
        n = self.snfa()
        nstates = len(n.states)

        label = dict()
        for i, c in n.delta:
            for j in n.delta[i, c]:
                rsym = '#' if c == '' else c
                label[i, j] = label.setdefault((i, j), regx.regx('@')) | regx.regx(rsym)

        # for debugging
        '''
        print('\nfor k = 0 :')
        for key in label:
            print(key, label[key].val)
        '''

        for k in range(1, nstates-1):
            to_k   = [ i for i, j in label if j == k and i != k]
            from_k = [ j for i, j in label if i == k and j != k]
            for i in to_k:
                for j in from_k:
                    if (k, k) not in label:
                        beta = label[i, k] & label[k, j]
                    else:
                        beta = label[i, k] & label[k, k].star() & label[k, j]
                    if (i, j) in label:
                        label[i, j] = label[i, j] | beta
                    else:
                        label[i, j] = beta

            # romove state k and all arrows into and out of it
            labelkeys = [(i, j) for i, j in label]
            for i, j in labelkeys:
                if i == k or j == k:
                    del label[i, j]

            # for debugging
            '''
            print(f'\nfor k = {k} :')
            for key in label:
                print(key, label[key].val)
            '''

        if (nstates-1, nstates) in label:
            return label[nstates-1, nstates]
        else: # no transition from start state to final state
            return regx.regx('@')

    def to_regx(self): # conversion algo from NFA to regular expression
        '''finds and returns a regular expression (regx object) for the language of NFA <self>

        This function actually calls the above method to_regx1(), the iterative version
        '''
        return self.to_regx1()

    def renumbered(self, startnum=1):
        '''Assumes <startnum> is an integer.
           Creates a new NFA which is identical to the NFA <self> except 
           that the state names are renumbered starting from 
           <startnum> onwards.
           
           Returns the new renumbered NFA.
        '''
        statelist = list(self.states)
        nstates = len(statelist)
        sid = {statelist[i] : startnum + i for i in range(nstates)}
        #print(sid) # debug

        newdelta = dict()
        for state, sym in self.delta:
            newdelta[sid[state], sym] = {sid[q] for q in self.delta[state, sym]}

        newstart = sid[self.start]
        newfinals = {sid[q] for q in self.finals}

        return nfa(delta=newdelta, start=newstart, finals=newfinals)

def go():
    print('Hi there! I am an nfa module.')

from . import regx
from . import dfa
from .util import prettySetStr
if __name__ == '__main__':
    go()

