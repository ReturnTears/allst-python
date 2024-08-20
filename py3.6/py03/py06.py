# py3.6_06
def selectAStrings(array) :
    newArray = []
    i = 0
    for arr in array :
        if (arr.startswith("a")):
            newArray.append(arr)
        i += 1
    return newArray
# 上述算法的效率是O(n)
arr = ['hello', 'world', 'aaa', 'bbb', 'ccc']
print(selectAStrings(arr)) # output: ['aaa']
