import sympy
def tetrate(a, b, d):
    if b>1:
        return a**tetrate(a, b-1, d)
    elif b<0:
        return tetrate(a, b+1, d)
    else:
        x=sympy.symbols('x')
        co=sympy.symbols(f'a0:{d+1}')
        f=sum(co[i]*x**i for i in range(d+1))
        r=[]
        r.append(f.subs(x, 0)-1)
        r.append(f.subs(x, 1)-a)
        for k in range(1, d):
            ll=f.diff(x, k).subs(x, 1)
            rr=(a**f.subs(x, x-1)).diff(x, k).subs(x, 1)
            r.append(ll-rr)
        p=f.subs(sympy.solve(r, co, dict=True)[0])
        return p.subs(x, b)
d=2 #d=3 doesn't work, idk why
print(tetrate(sympy.S('E'), sympy.S('1/2'), d).evalf())
print(tetrate(sympy.S('2'), sympy.S('3/2'), d).evalf())