from functools import reduce


l=[{1:2,3:4},{1:6,3:8},{1:'a',3:'b'}]
print(reduce(lambda a,b: str(a)+' '+str(b),list(map(lambda x: reduce(lambda a,b: str(a)+','+str(b),list(map(lambda y: str(y)+":"+str(x[y]),x))),l))))