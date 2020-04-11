"""
Module For Processing Finite Automata And Regular Expressions - version 1.0
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
        three arguments above.  A hell state '_H_' may be added to <states> make 
        <delta> a total function if the given <delta> is not.
        '''
        self.states = {start}.union(finals)
        self.sigma = set()
        self.delta = delta
        self.start = start
        self.finals = finals

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
        add_HELL = False
        for state in self.states:
            for sym in self.sigma:
                if (state, sym) not in self.delta:
                    self.delta[state, sym] = '_H_'
                    add_HELL= True
        if add_HELL:
            self.states.add('_H_')
            for c in self.sigma:
                self.delta['_H_', c] = '_H_'

    def __str__(self):
        s =  [f'states = {sorted(self.states)}']
        s.append(f'sigma = {sorted(self.sigma)}')
        s.append(f'start = {self.start}')
        s.append(f'finals = {sorted(self.finals)}')
        s.append('delta = {')
        for key, val in sorted(self.delta.items()):
                s.append(f'    {key} : {val}')
        s.append('}')
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
        if isinstance(other, nfa):  # nfa needs to be converted to dfa first
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
        new_nfa = nfa(delta=nfa_delta, start=nfa_start, finals=nfa_finals)
        return new_nfa

    def to_regx(self):
        '''finds and returns a regular expression (regx object) for the language of DFA <self>
        '''
        return self.to_nfa().to_regx()

    def renumbered(self, startnum):
        '''Assumes <startnum> is an integer.
           Creates a new DFA which is identical to the DFA <self> 
           except that the state names are renumbered starting from 
           <startnum> onwards.
           
           Returns the new renumbered DFA.
        '''
        statelist = sorted(self.states)
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

    def minimized(self):
        '''Returns a minimized DFA equivalent to the given DFA <self>,
        using the table-marking algorithm such as described in H&U text
        
        This function actually calls the above method minimized2()
        '''
        return self.minimized2()

# --- end of class dfa --- #

class nfa:
    '''represents a nondeterministic finite automata (NFA)
    Attributes:
        states : the set of all states (represented by any immutable object)
        sigma  : the input alphabet
        delta  : the transition (partial) function from states X sigma to 
                 the powerset of states
        start  : the start state
        finals : the set of all final states
        decider : the dynamically-growing, partial DFA (object) that serves as 
                  the nfa's deterministic decider. The method accept() will 
                  incrementally add new states to this decider as needed.
        Rdict : a dict to be used internally by the method R()
        SNFA : a simplified NFA to be used internally by the method snfa()
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

        The attribute <decider> is initialized to be a partial DFA with only 
        the start state.

        The attributes <Rdict> and <SNFA> are initialized to be their 
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
        self.decider = dfa(delta=dict(), start=None, finals=set())  # the equivalent (partial) DFA
        self.decider.sigma = self.sigma
        self.decider.start = tuple(sorted(self.ep_closure(self.start)))
        self.decider.states = {self.decider.start}
        if set(self.decider.start).intersection(self.finals) != emptyset:
            self.decider.finals.add(self.decider.start)
        self.Rdict = dict()  # using internally by the method R()
        self.SNFA = None     # using internally by the method snfa()

    def __str__(self):
        s =  [f'states = {sorted(self.states)}']
        s.append(f'sigma = {sorted(self.sigma)}')
        s.append(f'start = {self.start}')
        s.append(f'finals = {sorted(self.finals)}')
        s.append('delta = {')
        for key, val in sorted(self.delta.items()):
                s.append(f'    {key} : {val}')
        s.append('}')
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

    def ep_closure(self, state):
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

    def calc_DFA_delta(self, Q, sym):
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
                nextstate.update(self.ep_closure(p))
        return tuple(sorted(nextstate))

    def to_dfa(self):  # NFA-to-DFA conversion algorithm
        '''Returns a DFA equivalent to the given NFA <self>, using 
        the algo described in L&P pp.69-70
        '''
        dstart = tuple(sorted(self.ep_closure(self.start)))
        dstates = {dstart}
        ddelta = dict()
        que = [dstart]
        while que != []:
            Q = que.pop(0)
            for sym in self.sigma:
                P = ddelta[Q, sym] = self.calc_DFA_delta(Q, sym)
                if P not in dstates:
                    que.append(P)
                    dstates.add(P)
        dfinals = {Q for Q in dstates if set(Q).intersection(self.finals) != emptyset}
        newdfa = dfa(delta=ddelta, start=dstart, finals=dfinals)
        return newdfa

    def accept1(self, w):
        '''Assume w is a string.
           Returns True if the NFA <self> accepts w, or False otherwise.

           Note: It dynamically builds a new partial DFA just enough 
           to do the job. The partial DFA is discarded when this 
           method returns.
        '''
        #print(f'Input is "{w}"') # debug
        n = dfa(delta=dict(), start=None, finals=set())  # the equivalent DFA
        n.sigma = self.sigma
        n.start = tuple(sorted(self.ep_closure(self.start)))
        n.states = {n.start}
        state = n.start
        for sym in w:
            #print(f'-- At {state}, read {sym}, ', end='')   # debug
            state = n.delta.setdefault((state, sym), self.calc_DFA_delta(state, sym))
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

           Note: It is essentially the same as the method accept1() above 
           but the partial DFA is incrementally built into the 
           <decider> attribute of the nfa <self> so it is preserved 
           within the nfa.
        '''
        #print(f'Input is "{w}"') # debug
        state = self.decider.start
        for sym in w:
            #print(f'-- At {state}, read {sym}, ', end='')   # debug
            if (state, sym) not in self.decider.delta:
                self.decider.delta[state, sym] = self.calc_DFA_delta(state, sym)
            state = self.decider.delta[state, sym]
            #print(f'go to {state}')   # debug
            if state not in self.decider.states:
                self.decider.states.add(state)
                if set(state).intersection(self.finals) != emptyset:
                    self.decider.finals.add(state)

        # print these for debugging
        '''
        print('Partial DFA:')
        print('\tstart state =' , self.decider.start)
        print('\tstate set =', self.decider.states)
        print('\tfinal set =', self.decider.finals)
        print('\tdelta = {')
        for key in self.decider.delta:
            print(f'\t  {key} : {self.decider.delta[key]}')
        print('\t}')
        '''

        if state in self.decider.finals:
            #print(f'-- Halt at a final state {state}') # debug
            return True
        else:
            #print(f'-- Halt at a nonfinal state {state}') # debug
            return False

    def R(self, i, j, k, ep=False):
        if (i, j, k) in self.Rdict:
            return self.Rdict[i, j, k]

        if k == 0:
            result = regx('@')
            for c in sorted(self.sigma) + ['']:
                if (i,c) in self.delta and j in self.delta[i, c]:
                    result = result | regx(c if c != '' else '#')
            if ep and i == j:
                result = result | regx('#')
        else:
            assert k > 0
            result = self.R(i,j,k-1,ep) | self.R(i,k,k-1,ep) & self.R(k,k,k-1,ep).star() & self.R(k,j,k-1,ep)

        self.Rdict[i, j, k] = result
        #print(f"R({i},{j},{k}) = {result if result.val != '@' else '{}'}") # debug
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
        if self.SNFA != None:
            return self.SNFA

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
        self.SNFA = nfa(delta=newdelta, start=newstart, finals={newfinal}) 
        #print('Simplified NFA:'); print(self.SNFA) # debug
        return self.SNFA

    def to_regx2(self):  # conversion algo from NFA to regular expression - recursive version
        '''finds and returns a regular expression (regx object) for the language of NFA <self>
        '''
        n = self.snfa()
        return n.R(n.start, n.start+1, n.start-1)

    def to_regx1(self): # conversion algo from NFA to regular expression - iterative version
        '''finds and returns a regular expression (regx object) for the language of NFA <self>
        '''
        n = self.snfa()
        nstates = len(n.states)

        label = dict()
        for i, c in n.delta:
            for j in n.delta[i, c]:
                rsym = '#' if c == '' else c
                label[i, j] = label.setdefault((i, j), regx('@')) | regx(rsym)

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
            return regx('@')

    def to_regx(self): # conversion algo from NFA to regular expression
        '''finds and returns a regular expression (regx object) for the language of NFA <self>

        This function actually calls the above method to_regx1()
        '''
        return self.to_regx1()

    def renumbered(self, startnum):
        '''Assumes <startnum> is an integer.
           Creates a new NFA which is identical to the NFA <self> except 
           that the state names are renumbered starting from 
           <startnum> onwards.
           
           Returns the new renumbered NFA.
        '''
        statelist = sorted(self.states)
        nstates = len(statelist)
        sid = {statelist[i] : startnum + i for i in range(nstates)}
        #print(sid) # debug

        newdelta = dict()
        for state, sym in self.delta:
            newdelta[sid[state], sym] = {sid[q] for q in self.delta[state, sym]}

        newstart = sid[self.start]
        newfinals = {sid[q] for q in self.finals}

        return nfa(delta=newdelta, start=newstart, finals=newfinals)

# --- end of class nfa --- #

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
            self.nfa = nfa(delta=deldict, start=1, finals={2})
        else: # not a singleton expression
            postfixlist, errmsg = regx_parser(val)
            if postfixlist == None:
                raise ValueError(errmsg)
            r = eval_regx_postfix(postfixlist)
            self.val, self.nfa = r.val, r.nfa

    def __str__(self):
        return self.val

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
        result.nfa = nfa(delta=newdelta, start=newstart, finals={newfinal})
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
        result.nfa = nfa(delta=newdelta, start=lhs_nfa.start, finals=rhs_nfa.finals)
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
        result.nfa = nfa(delta=newdelta, start=newstart, finals={newfinal})
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

    def equiv(self, other):
        '''Assumes <self> and <other> are both regx objects.
           Checks if they are equivalent, meaning that they define the same
           language.
           Returns True if they are equivalent, False otherwise.
        '''
        return self.nfa.equiv(other.nfa)

    def __eq__(self, other):  # exactly the same as equiv() above
        return self.nfa.equiv(other.nfa)

# --- end of class regx --- #

def removeSpace(s):
    '''Assumes s is a string,
       returns a copy of s with all spaces removed'''
    t = []
    for c in s:
        if c != ' ':
            t.append(c)
    return ''.join(t)

def regx_parser(regxstr):
    '''Assumes <regxstr> is a string of regular expressions
       using U, *, and () as operators, then parses and translates
       the expression into an equivalent postfix expression.

       Returns a tuple (<postfix>, <errmsg>) where <postfix> is
       the string of postfix expression if the parsing is successful
       and <errmsg> will be '' is this case. But if there is a
       parse error, <postfix> will be None and <errmsg> is a string
       comprising a proper error message.'''

    def pushstack(symlist):
        for i in range(1, len(symlist)+1):
            stack.append(symlist[-i])

    def next_lexeme():
        if next_lexeme.pos < next_lexeme.len:
            lexeme = next_lexeme.str[next_lexeme.pos]
            next_lexeme.pos += 1
        else:
            lexeme = ''
        return lexeme

    # parser's states
    Qstate = 1
    union_state = 2
    star_state = 3
    lparen_state = 4
    rparen_state = 5 
    symbol_state = 6
    EOSstate = -1
    
    state = Qstate     # parser's state
    stack = ['_E']      # parser's PDA stack
    outlist = []       # postfix output sequence
    op_stack = []      # postfix operator stack

    # prepare the regx string to feed the parser
    next_lexeme.str = removeSpace(regxstr)
    next_lexeme.len = len(next_lexeme.str)
    next_lexeme.pos = 0

    while True:

        if state == Qstate:
            lexeme = next_lexeme()
            if lexeme == '':
                state = EOSstate
            elif lexeme == 'U':
                state = union_state
            elif lexeme == '*':
                state = star_state
            elif lexeme == '(':
                state = lparen_state
            elif lexeme == ')':
                state = rparen_state
            else: # any other symbol is legitimate
                state = symbol_state

        elif state == EOSstate:
            if stack == []:
                # print('parse successful')
                return outlist, ''
            elif stack[-1] == '_E':
                stack.pop()
                pushstack(['_T', '_Ep'])
            elif stack[-1] == '_Ep':
                stack.pop()
            elif stack[-1] == '_T':
                stack.pop()
                pushstack(['_F', '_Tp'])
            elif stack[-1] == '_Tp':
                stack.pop()
                end_of_term(op_stack, outlist)
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                end_of_factor(op_stack, outlist)
            elif stack[-1] == '_P':
                return None, '01 parse error at EOS, expecting a factor'
            else:
                return None, f'02 parse error at EOS, expecting |{stack[-1]}|'

        elif state == symbol_state:
            if stack == []:
                return None, f'11 parse error at |{lexeme}|'
            elif stack[-1] == '_E':
                stack.pop()
                pushstack(['_T', '_Ep'])
            elif stack[-1] == '_Ep':
                stack.pop()
            elif stack[-1] == '_T':
                stack.pop()
                pushstack(['_F', '_Tp'])
            elif stack[-1] == '_Tp':
                stack.pop()
                pushstack(['_F', '_Tp'])
                op_stack.append('&') # another concatenated factor occurs
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                end_of_factor(op_stack, outlist)
            elif stack[-1] == '_P':
                stack.pop()
                pushstack([lexeme])
            else: # TOS is any symbol of the alphabet of the regular language
                stack.pop()
                state = Qstate
                end_of_token_symbol(op_stack, outlist, lexeme)

        elif state == union_state:
            if stack == []:
                return None, '21 parse error at |{lexeme}|'
            elif stack[-1] == '_E':
                stack.pop()
                pushstack(['_T', '_Ep'])
            elif stack[-1] == '_Ep':
                stack.pop()
                pushstack(['U', '_T', '_Ep'])
            elif stack[-1] == '_T':
                stack.pop()
                pushstack(['_F', '_Tp'])
            elif stack[-1] == '_Tp':
                stack.pop()
                end_of_term(op_stack, outlist)
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                end_of_factor(op_stack, outlist)
            elif stack[-1] == '_P':
                return None, f'22 parse error at |{lexeme}|, expecting a factor'
            elif stack[-1] == 'U':
                stack.pop()
                state = Qstate
                op_stack.append('U')
            else:
                return None, f'23 parse error at |{lexeme}|, expecting |{stack[-1]}|'

        elif state == star_state:
            if stack == []:
                return None, f'31 parse error at |{lexeme}|'
            elif stack[-1] == '_E':
                stack.pop()
                pushstack(['_T', '_Ep'])
            elif stack[-1] == '_Ep':
                stack.pop()
            elif stack[-1] == '_T':
                stack.pop()
                pushstack(['_F', '_Tp'])
            elif stack[-1] == '_Tp':
                stack.pop()
                end_of_term(op_stack, outlist)
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                pushstack(['*', '_Fp'])
            elif stack[-1] == '_P':
                return None, f'32 parse error at |{lexeme}|, expecting a factor'
            elif stack[-1] == '*':
                stack.pop()
                state = Qstate
                outlist.append('*')
            else:
                return None, f'33 parse error at |{lexeme}|, expecting |{stack[-1]}|'

        elif state == lparen_state:
            if stack == []:
                return None, f'41 parse error at |{lexeme}|'
            elif stack[-1] == '_E':
                stack.pop()
                pushstack(['_T', '_Ep'])
            elif stack[-1] == '_Ep':
                stack.pop()
            elif stack[-1] == '_T':
                stack.pop()
                pushstack(['_F', '_Tp'])
            elif stack[-1] == '_Tp':
                stack.pop()
                pushstack(['_F', '_Tp'])
                op_stack.append('&') # another concatenated factor occurs
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                end_of_factor(op_stack, outlist)
            elif stack[-1] == '_P':
                stack.pop()
                pushstack(['(', '_E', ')'])
            elif stack[-1] == '(':
                stack.pop()
                state = Qstate
                op_stack.append('(')  # to serve as the left wall against the enclosing expression
            else:
                return None, f'42 parse error at |{lexeme}|, expecting |{stack[-1]}|'

        elif state == rparen_state:
            if stack == []:
                return None, f'51 parse error at |{lexeme}|'
            elif stack[-1] == '_E':
                stack.pop()
                pushstack(['_T', '_Ep'])
            elif stack[-1] == '_Ep':
                stack.pop()
            elif stack[-1] == '_T':
                stack.pop()
                pushstack(['_F', '_Tp'])
            elif stack[-1] == '_Tp':
                stack.pop()
                end_of_term(op_stack, outlist)
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                end_of_factor(op_stack, outlist)
            elif stack[-1] == '_P':
                return None, f'52 parse error at |{lexeme}|, expecting a factor'
            elif stack[-1] == ')':
                stack.pop()
                state = Qstate
                end_of_parenthesized_expression(op_stack, outlist)
            else:
                return None, f'53 parse error at |{lexeme}|, expecting |{stack[-1]}|'

        else:
            return None, f'A1 Unknown parser state |{state}|'

def end_of_term(op_stack, outlist): 
    '''internally used by the parser, called at the end of term'''
    if len(op_stack) != 0 and op_stack[-1] == 'U': # not the 1st term
        outlist.append(op_stack.pop())

def end_of_factor(op_stack, outlist): 
    '''internally used by the parser, called when the parser's TOS matches a factor'''
    if len(op_stack) != 0 and op_stack[-1] == '&': # not 1st factor of current term
        outlist.append(op_stack.pop())

def end_of_token_symbol(op_stack, outlist, lexeme):
    '''internally used by the parser, called when the parser's TOS matches a symbol'''
    outlist.append(lexeme)

def end_of_parenthesized_expression(op_stack, outlist):
    '''internally used by the parser, called when parser's TOS matches token ')' '''
    assert op_stack[-1] == '('
    op_stack.pop()

def eval_regx_postfix(pfxlist):
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

def go():
    print('Hi there! I am an FA module.')

if __name__ == '__main__':
    go()

