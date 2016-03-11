# lecture 3.6, slide 2
# bisection search for square root

x = 5
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    
    print('ans = ' + str(ans) + ' ans**2 (' + str(ans**2) + ') x=' + str(x)    )
    print('')
    
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))