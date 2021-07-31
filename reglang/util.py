
def prettySetStr(setObj):
    '''Assumes <setObj> is a Python set
       Returns a print-ready string of the set with members in sorted order.
    '''
    s = {repr(x) for x in setObj}  # convert the set into a set of representing strings
    slist = sorted(s)              # so that it can be safely sorted and becomes a list
    return '{' + ', '.join(slist) + '}'  # then return a string that represents it as a set.

def go():
    print('Hi there! I am a util module.')

if __name__ == '__main__':
    go()
