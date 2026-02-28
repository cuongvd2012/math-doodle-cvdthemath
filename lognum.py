import math
class lognum: #1*2^6 lines of code
    def __init__(self, s: int, m, e: int):
        if s==0 or m==0:
            self.sign=0
            self.mantissa=1
            self.exponent=0
        else:
            ep=int(math.log2(m))
            e+=ep
            m/=2**ep
            if m<0:
                s=-s
                m=-m
            self.sign=s
            self.mantissa=m
            self.exponent=e
    def __abs__(self):
        return lognum(abs(self.sign), self.mantissa, self.exponent)
    def __neg__(self):
        return lognum(-self.sign, self.mantissa, self.exponent)
    def __eq__(self, other):
        return self.sign==other.sign and self.mantissa==other.mantissa and self.exponent==other.exponent
    def __lt__(self, other):
        if self.sign<other.sign: return True
        if self.sign>other.sign: return False
        if math.log2(self.mantissa)+self.exponent<math.log2(other.mantissa)+other.exponent: return True
        return False
    def __gt__(self, other):
        if self.sign>other.sign: return True
        if self.sign<other.sign: return False
        if math.log2(self.mantissa)+self.exponent>math.log2(other.mantissa)+other.exponent: return True
        return False
    def __le__(self, other):
        return self==other or self<other
    def __ge__(self, other):
        return self==other or self>other
    def __add__(self, other):
        if self.sign==1 and other.sign==-1:
            return self-(-other)
        if self.sign==-1 and other.sign==1:
            return other-(-self)
        if self.sign==0: return other
        if other.sign==0: return self
        if abs(self)>abs(other):
            return other+self
        return lognum(self.sign, self.mantissa*2**(self.exponent-other.exponent)+other.mantissa, other.exponent)
    def __sub__(self, other):
        if self.sign==1 and other.sign==-1:
            return self+(-other)
        if self.sign==-1 and other.sign==1:
            return self+(-other)
        if self.sign==0:
            other.sign=-other.sign
            return other
        if other.sign==0: return self
        if abs(other)>abs(self): return -(other-self)
        return lognum(self.sign, self.mantissa-other.mantissa*2**(other.exponent-self.exponent), self.exponent)
    def __mul__(self, other):
        return lognum(self.sign*other.sign, self.mantissa*other.mantissa, self.exponent+other.exponent)
    def __truediv__(self, other):
        return lognum(self.sign*other.sign, self.mantissa/other.mantissa, self.exponent-other.exponent)
    def __str__(self):
        return "0" if self.sign==0 else "-"*(self.sign==-1)+str(self.mantissa)+"*2^"+str(self.exponent)
