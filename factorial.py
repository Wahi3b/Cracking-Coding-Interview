#Using the Python language, have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it (ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18. 
def FirstFactorial(num): 
    if num==0: return 1
    if num >= 1:
        return num * FirstFactorial(num-1)
#Time complexity is O(n) since every recursive call takes constant time and it is done n times

#Testing    
result = FirstFactorial(5)
print(result)