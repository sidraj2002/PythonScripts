
def _FindNonRepeat(_InputString, chars):
    count = 0
    _NonRepeat = {}

    for i in chars:
        count = _InputString.count(i)
        if count > 1:
            print(count,i)
        if count == 1:
            _NonRepeat[count] = i
            #print(_NonRepeat)
    return(_NonRepeat)
    
def _FindNonRepeat2(_InputString, chars):
    return(_InputString.count('a'))

chars = 'abcdefghijklmnopqrstuvwxyz'
input = 'aaacccssddbddd'
 
NonRepeat = _FindNonRepeat2(input, chars)
print(NonRepeat)