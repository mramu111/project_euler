def is_prime(num):
	flag=True
	#import pdb;pdb.set_trace()
	#print num
	if num==2:
		return True
	elif num<2:
		return False
	else:
		#import pdb;pdb.set_trace()

		for i in xrange(2,int(num**0.5+1)):			
			if num%i==0:
				flag=False	
				return flag

	return flag
		

	
		
		
		

			

def primefactor(num):	
	for i in xrange(int(num**0.5+1),2,-2): 
		if is_prime(i) and num%i==0:
			print i
	


if __name__=='__main__':
	primefactor(600851475143)
