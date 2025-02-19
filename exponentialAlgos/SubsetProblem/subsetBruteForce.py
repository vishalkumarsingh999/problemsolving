import math
import string
def genrateSet(s, i):
    subset=[]
    de=""
    for j in range(len(s)):
        if (i & 1<<j)==1<<j :
            subset.append(s[j])
    #     de=f" i={i}, j={j},1<<j={1<<j}"
    #     print(de)
    # print(subset)
    return "".join(subset)

def allsubset(s: object):
    result=set()
    for i in range(0,2**len(s)):
        result.add(genrateSet(s,i))
    return result

if __name__ == '__main__':
    allset=allsubset('aaaa')
    print(allset,len(allset))
