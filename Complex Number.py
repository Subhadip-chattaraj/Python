import cmath
import math

if __name__=='__main__':
    z=complex(input())
    x=z.real
    y=z.imag
    r=math.sqrt(pow(x,2)+pow(y,2))
    print(r)
    print(cmath.phase(z))
