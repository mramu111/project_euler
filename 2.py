
def fib():
    sumtotal=0
    a,b=1,1
    while True:
	print a,b
	if a<=4000000:			
	    if a%2==0:
		sumtotal=sumtotal + a

	    else:
		break

	    a,b, = b,a+b
	return sumtotal


if __name__=='__main__':
	sumtotal=fib()
	print sumtotal

