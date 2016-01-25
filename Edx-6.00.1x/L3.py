
num = 10
for num in range(5):
    print num
print num 

print '------------'

divisor = 2
for num in range(0, 10, 2):
    print num/divisor 
    
print '------------'   
    
for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!'
        
print '------------'  
       
count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count 

print '------------'  

for num in range(2, 12, 2):
    print num
print 'Goodbye!' 

print '------------'    

print 'Hello!'
for num in range(10, 0, -2):
    print num

print '------------'  

end  = 6
val = 0
for num in range(0, end+1):
    val = val + num
print val

