
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
    

chars = 'abcdefghijklmnopqrstuvwxyz'
input = 'aaacccssddbddd'
 
NonRepeat = _FindNonRepeat(input, chars)
print(NonRepeat)