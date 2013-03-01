def check_palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
        

max_palindrome=0
for i in xrange(100,1000):
    for j in xrange(100,1000):
        product=i*j
        if check_palindrome(product):            
            if max_palindrome<product:
                max_palindrome=product
            break
        
        
print  max_palindrome
        
    