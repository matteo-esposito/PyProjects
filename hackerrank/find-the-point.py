import os
import sys

def findPoint(px, py, qx, qy):
    '''
    Given 2 points, a and the center, find b (symmetric bound).
    '''
    return ("{0} {1}".format(2*qx-px, 2*qy-py))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())

    for n_itr in range(n):
        pyPyQxQy = input().split()
        px = int(pyPyQxQy[0])
        py = int(pyPyQxQy[1])
        qx = int(pyPyQxQy[2])
        qy = int(pyPyQxQy[3])
        result = findPoint(px, py, qx, qy)

        print(str(result))

        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')
    
    # fptr.close()