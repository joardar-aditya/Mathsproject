def gensubset(L):
    if len(L) == 0:
        return [[]]
    smaller = gensubset(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(extra + small)
    return smaller + new

    
