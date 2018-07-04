import numpy as np
list=np.loadtxt('result.txt')
a=list[0]
b=list[1]
c=list[2]
print a.shape
num=np.dot(a,b)
cos=num/(np.linalg.norm(a)*np.linalg.norm(b))
print '1-2 cosine:'
print 0.5+0.5*cos
num=np.dot(a,c)
cos=num/(np.linalg.norm(a)*np.linalg.norm(c))
print '1-3 cosine:'
print 0.5+0.5*cos
num=np.dot(c,b)
cos=num/(np.linalg.norm(c)*np.linalg.norm(b))
print '2-3 cosine:'
print 0.5+0.5*cos
