# py3.6_05
def chessboardSpace(numberOfGrains) :
    chessboardSpaces = 1
    placedGrains = 1
    while (placedGrains < numberOfGrains) :
        placedGrains *= 2
        chessboardSpaces += 1
    return chessboardSpaces
# 上述算法的效率是O(Logn)
res = chessboardSpace(11)
print("this res is : ", res)
