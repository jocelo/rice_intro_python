def smaller_root(a, b, c):
    discriminant  = (b**2) - (4.0*a*c)
    
    if discriminant  > 0:
        sol1 = ( (-1.0*b) + discriminant**(1.0/2.0) ) / (2.0 * a)
        sol2 = ( (-1.0*b) - discriminant**(1.0/2.0) ) / (2.0 * a)
        if sol1 > sol2:
            return sol2
        else:
            return sol1
    elif discriminant  == 0:
        sol = ( (-1*b) + discriminant**(1.0/2.0) ) / (2.0 * a)
        return sol
    else:
        print "Error: No real solutions"

def test(a, b, c):
    """Tests the smaller_root function."""
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)