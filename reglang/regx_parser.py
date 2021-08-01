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
    next_lexeme.str = _removeSpace(regxstr)
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
                _end_of_term(op_stack, outlist)
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                _end_of_factor(op_stack, outlist)
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
                _end_of_factor(op_stack, outlist)
            elif stack[-1] == '_P':
                stack.pop()
                pushstack([lexeme])
            else: # TOS is any symbol of the alphabet of the regular language
                stack.pop()
                state = Qstate
                _end_of_token_symbol(op_stack, outlist, lexeme)

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
                _end_of_term(op_stack, outlist)
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                _end_of_factor(op_stack, outlist)
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
                _end_of_term(op_stack, outlist)
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
                _end_of_factor(op_stack, outlist)
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
                _end_of_term(op_stack, outlist)
            elif stack[-1] == '_F':
                stack.pop()
                pushstack(['_P', '_Fp'])
            elif stack[-1] == '_Fp':
                stack.pop()
                _end_of_factor(op_stack, outlist)
            elif stack[-1] == '_P':
                return None, f'52 parse error at |{lexeme}|, expecting a factor'
            elif stack[-1] == ')':
                stack.pop()
                state = Qstate
                _end_of_parenthesized_expression(op_stack, outlist)
            else:
                return None, f'53 parse error at |{lexeme}|, expecting |{stack[-1]}|'

        else:
            return None, f'A1 Unknown parser state |{state}|'

def _end_of_term(op_stack, outlist): 
    '''internally used by the parser, called at the end of term'''
    if len(op_stack) != 0 and op_stack[-1] == 'U': # not the 1st term
        outlist.append(op_stack.pop())

def _end_of_factor(op_stack, outlist): 
    '''internally used by the parser, called when the parser's TOS matches a factor'''
    if len(op_stack) != 0 and op_stack[-1] == '&': # not 1st factor of current term
        outlist.append(op_stack.pop())

def _end_of_token_symbol(op_stack, outlist, lexeme):
    '''internally used by the parser, called when the parser's TOS matches a symbol'''
    outlist.append(lexeme)

def _end_of_parenthesized_expression(op_stack, outlist):
    '''internally used by the parser, called when parser's TOS matches token ')' '''
    assert op_stack[-1] == '('
    op_stack.pop()

def _removeSpace(s):
    '''Assumes s is a string,
       returns a copy of s with all spaces removed'''
    t = []
    for c in s:
        if c != ' ':
            t.append(c)
    return ''.join(t)

def go():
    print('Hi there! I am a regx_parser module.')

if __name__ == '__main__':
    go()
