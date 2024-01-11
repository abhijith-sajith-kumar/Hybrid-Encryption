import math
class Fnctn:
    def __init__(self,n):
        self.n = n
    def nrst_sqrt(self,n):
        if math.isqrt(n) ** 2 == n:
            sqrt_val = math.isqrt(n)

        else:
            sqrt_val = math.isqrt(n) + 1

        return sqrt_val
    
    def arr_fill(self,n,list):
        if math.isqrt(self.n) ** 2 == n:
            return list
        else:
            x = self.nrst_sqrt(n) ** 2
            p = x - len(list)
            for i in range(0, p):
                list.append(ord("X"))
            return list