f=open('13.csv','r')
numbers=str(f.read())
sum_digits=0
total = [int(i) for i in numbers.split("\n")]
total=  sum(total)
print str(total)[0:10]   

