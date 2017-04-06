
import re

def tokenize(s):
    op = r'[\-\+\*\^\(\)/]'
    num = r'-?([0-9]+(\.[0-9]+)?)|(\.[0-9]+)'
    ts = [item.group() for item in re.finditer('({})|({})'.format(num,op),s)]
    k = 1
    while k <= len(ts)-1:
        if any(d in ts[k] for d in '0123456789') and any(d in ts[k-1] for d in '0123456789)'):
                ts = ts[:k] + ['+'] + ts[k:]
        k += 1
    return ts
            

def RPN(alg):
    """ Assumes input is list of strings (tokens) in algebraic notation.
        '+-*/^()' allowed. Decimal and negative numbers allowed.
        Output is a list of strings in RPN. """
    instack = alg
    outqueue = []
    opstack = []
    while instack:
        t = instack.pop(0)
        if any(d in t for d in '0123456789'):
            outqueue.append(t)
        elif t in '+-*/^':
            while opstack and (
                    (t in '+-' and opstack[-1] in '+-*/') or
                    (t in '*/' and opstack[-1] in '*/')):
                outqueue.append(opstack.pop())
            opstack.append(t)
        elif t == '(':
            opstack.append(t)
        elif t == ')':
            while opstack and opstack[-1] != '(':
                outqueue.append(opstack.pop())
            if not opstack:
                print('parenthesis error')
                return []
            opstack.pop()
    while opstack:
        ot = opstack.pop()
        if ot in '()':
            print('parenthesis error')
            return []
        outqueue.append(ot)
    return outqueue

if __name__ == '__main__':
    s = '3+(5-1)+(-8-(-4-2))'
    print('orig: ' + s)
    rt = tokenize(s)
    print('tkns: ' + ' '.join(rt))
    rr = RPN(rt)
    print('rpn:  ' + ' '.join(rr))

    
