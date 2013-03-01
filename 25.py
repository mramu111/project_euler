def fib():    
    a,b=0,1
    while True:	
	#print  a
	if len(str(a))==1000:
	    import pdb;pdb.set_trace()
	    break
	a,b, = b,a+b
	yield a
	


if __name__=='__main__':
    a=[]
    for i in fib():
	#print i	
	a.append(i)
    print a[0],
    print a[1],
    print len(a)
	