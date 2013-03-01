
squ_sum=0
sum_of_num=0
for i in xrange(1,101):
    squ_sum=squ_sum + i*i
    sum_of_num=sum_of_num + i
    
    
print abs((sum_of_num*sum_of_num)-squ_sum)
    
    
    