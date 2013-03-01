
sum_total=0
for i in xrange(1000):
    if i%3==0:
        sum_total=sum_total+i
    if i%5==0 and not  i%3==0:
        sum_total=sum_total+i
        
        
print sum_total