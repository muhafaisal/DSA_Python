def matchingStrings(stringList, queries):
    arr = []  
    for i in queries:
        arr.append(stringList.count(i))
    return arr