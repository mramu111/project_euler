def is_prime(num):
    flag=True	
    if num==2:
	    return True
    elif num<2:
	    return False
    else:
	for i in xrange(2,int(num**0.5+1)):			
	    if num%i==0:
		flag=False	
		return flag

    return flag




number_dict={}
list_primes=[]
for i in xrange(1,2000000):
    if is_prime(i):
	list_primes.append(i)
	

print sum(list_primes)
