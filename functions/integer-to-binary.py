import math

def intToBin(n):
    '''
    Convert a postive integer to its binary representation.
    MILA sample interview question
    Fall 2018
    '''
    binaryVal = []
    intVal = n
    
    # Handle base cases then general case
    if n < 0:
        return(str(intVal) + " has no binary represention.")
    elif n == 0: 
        binaryVal.append('0')
    elif n == 1: 
        binaryVal.append('1')
    else:
        exp = math.floor(math.log(n) / math.log(2))
        
        while (exp >= 0):
            
            binFactor = 2 ** exp
            
            if binFactor <= n:
                binaryVal.append('1')
                n -= binFactor
            else:
                binaryVal.append('0')
                
            exp -= 1 # update exponent
                
    return(str(intVal) + " in binary is: " + "".join(binaryVal))
        
    
# Sample set
nums = [-34,-2,0,1,33,70,256,257,258,259]

for n in nums:
    print(intToBin(n)) 

