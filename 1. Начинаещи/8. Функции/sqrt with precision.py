def squareRoot(number, precision):
    start = 0
    ans = 0
    end = number
    exitflag = False
    
    # for computing integral part of square root of number
    while start <= end and exitflag == False:
        mid = float(start + end) / 2
        if mid * mid == number:
            ans = mid
            exitflag = True
        else:
            
            # incrementing start if integral part lies on right side of the mid
            if mid * mid < number:
                start = mid + 1
                ans = mid
                increment = 0.1
                for i in range(0, precision - 1 + 1, 1):
                    while ans * ans <= number:
                        ans = ans + increment
                    
                    # loop terminates when ans * ans > number
                    ans = ans - increment
                    increment = increment / 10
            else:
                
                # decrementing end if integral part lies on the left side of the mid
                end = mid - 1
            
            # for computing the fractional part of square root upto given precision
    
    return ans

# Main
# Flowgorithm 2.12
# 2018-03-04
# Find square root of number upto given precision using binary search
print("Result of squareRoot(50, 3) -> ", end='', flush=True)
print(squareRoot(50, 3))
print("Result of squareRoot(20, 2) -> ", end='', flush=True)
print(squareRoot(20, 2))
