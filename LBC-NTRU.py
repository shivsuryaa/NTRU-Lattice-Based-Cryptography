import sympy as sp
x=sp.Symbol('x')

#Taking polynomial input
def input_poly(name,n):
    coeff=list(map(int,input(f"Enter {name} coefficients: ").split()))
    coeff=[0]*(n-len(coeff))+coeff
    return sp.Poly(sum(c*x**(n-i-1) for i,c in enumerate(coeff)),x)

#Convert coefficient list to polynomial
def poly_from_coeff(coeff):
    n=len(coeff)
    return sp.Poly(sum(c*x**(n-i-1) for i,c in enumerate(coeff)),x)

#Get coefficients after reduction
def coeff_list(poly,n,mod=None,centered=False):
    expr=poly.as_expr() if isinstance(poly,sp.Poly) else poly
    poly=sp.Poly(sp.rem(expr,x**n-1,domain=sp.ZZ),x)
    coeff=[0]*n

    for (degree,),value in poly.terms():
        value=int(value)

        if mod is not None:
            value%=mod

            #Center lifting
            if centered and value>mod//2:
                value-=mod

        coeff[n-1-degree]=value

    return coeff

#Polynomial modulo operation
def poly_mod(poly,n,mod):
    return poly_from_coeff(coeff_list(poly,n,mod))

#Used during decryption
def center_lift(poly,n,mod):
    return poly_from_coeff(coeff_list(poly,n,mod,centered=True))

#Taking NTRU parameters
n=int(input("Enter n: "))
p=int(input("Enter p: "))
q=int(input("Enter q: "))

f=input_poly("f",n)
g=input_poly("g",n)
m=input_poly("m",n)
r=input_poly("r",n)

#Finding inverse of f
try:
    fp=poly_mod(sp.invert(f.as_expr(),x**n-1,domain=sp.GF(p)),n,p)
    fq=poly_mod(sp.invert(f.as_expr(),x**n-1,domain=sp.GF(q)),n,q)

except sp.polys.polyerrors.NotInvertible:
    print("Choose a different f")
    exit()

#Public key generation
h=poly_mod(p*fq.as_expr()*g.as_expr(),n,q)
print("h :",h.as_expr())

#Encryption
e=poly_mod(r.as_expr()*h.as_expr()+m.as_expr(),n,q)
print("e :",e.as_expr())

#Decryption
a=center_lift(f.as_expr()*e.as_expr(),n,q)
b=poly_mod(a,n,p)
c=poly_mod(b.as_expr()*fp.as_expr(),n,p)

print("Decrypted Message :",c.as_expr())

#Verification
if coeff_list(m,n,p)==coeff_list(c,n,p):
    print("Decryption Successful")
else:
    print("Decryption Failed")