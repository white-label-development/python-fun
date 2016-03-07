num = 19
print num

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
    
result = ""

if num == 0:
    result = "0"
    
while num > 2:
    result = str(num%2) + result
    print result
    num = num/2
    
if isNeg:
    result = "-" + result    
    
#given 19, result = "011". So a crap conversion atm.