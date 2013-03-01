def pentagonal():    
    for i in xrange(1,99999):    
        num=i*(3*i-1)/2   
        yield num   

elements=[]
for term in pentagonal():    
    global elements    
    elements.append(term)      
    
    
for i,term in enumerate(elements):            
    diff=abs(term-elements[-i])
    sum_of_two=(term+elements[-i])
    if sum_of_two in elements and diff in elements:
        print term
        print elements[-i]
    
   