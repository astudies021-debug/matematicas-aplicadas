import sympy as s
from fractions import Fraction as F
import math
T=lambda v: math.trunc(v*1e4)/1e4
# Ej1 RK4 sistema (exacto, sin redondeo)
f=lambda t,x,y:3*x-3*y+2; g=lambda t,x,y:-6*x-t
def rk(f,g,t,x,y,H,r=lambda v:v):
    K1=r(H*f(t,x,y));C1=r(H*g(t,x,y))
    K2=r(H*f(t+H/2,x+K1/2,y+C1/2));C2=r(H*g(t+H/2,x+K1/2,y+C1/2))
    K3=r(H*f(t+H/2,x+K2/2,y+C2/2));C3=r(H*g(t+H/2,x+K2/2,y+C2/2))
    K4=r(H*f(t+H,x+K3,y+C3));C4=r(H*g(t+H,x+K3,y+C3))
    return [K1,C1,K2,C2,K3,C3,K4,C4],x+(K1+2*(K2+K3)+K4)/6,y+(C1+2*(C2+C3)+C4)/6
print("Ej1 exacto:",rk(f,g,0,1,-1,0.1))
print("Ej1 trunc4:",rk(f,g,0,1,-1,0.1,T))
t=s.symbols('t');X,Y=s.Function('x'),s.Function('y')
sol=s.dsolve([s.Eq(X(t).diff(t),3*X(t)-3*Y(t)+2),s.Eq(Y(t).diff(t),-6*X(t)-t)],ics={X(0):1,Y(0):-1})
print("Ej1 analitica t=0.1:",[s.N(e.rhs.subs(t,s.Rational(1,10)),8) for e in sol])
# Ej2
f2=lambda t,y,z:z; g2=lambda t,y,z:4*z-4*y
print("Ej2 exacto:",rk(f2,g2,0,1,1,0.1)); print("Ej2 trunc4:",rk(f2,g2,0,1,1,0.1,T))
yy=s.Function('y'); e=s.dsolve(yy(t).diff(t,2)-4*yy(t).diff(t)+4*yy(t),ics={yy(0):1,yy(t).diff(t).subs(t,0):1}).rhs
print("Ej2 analitica:",e, s.N(e.subs(t,0.1),8), s.N(e.diff(t).subs(t,0.1),8))
# Ej3 diferencias finitas
h=s.Rational(1,2); c=lambda ti:2+h**2*(1-s.Rational(ti)/5)
A=s.Matrix([[-c('1.5'),1,0,0],[1,-c(2),1,0],[0,1,-c('2.5'),1],[0,0,2,-c(3)]])
B=s.Matrix([s.Rational(3,2)*h**2-2,2*h**2,s.Rational(5,2)*h**2,3*h**2+1])
Xs=A.LUsolve(B); print("Ej3 A=",A,"B=",B.T); print("Ej3 X=",Xs.T,[s.N(v,8) for v in Xs])
# Ej5 complejo
x,y=s.symbols('x y',real=True); I=s.I
TI=s.integrate(x**2,(x,1,2)); TII=s.expand(I*s.integrate((2+I*y)**2,(y,0,1)))
TIII=s.expand(s.integrate((x+I)**2,(x,2,1))); TIV=s.expand(I*s.integrate((1+I*y)**2,(y,1,0)))
print("Ej5:",TI,TII,TIII,TIV,"suma",s.simplify(TI+TII+TIII+TIV))
# Ej5-6 residuos
z=s.symbols('z'); z1=-1+2*I; z2=-1-2*I
F=(2*z**2+5)/((z+1)*(z-z1)*(z-z2))
print("den expandido:",s.expand((z+1)*(z-z1)*(z-z2)))
R=[s.simplify(s.residue(F,z,p)) for p in (z1,z2,-1)]
print("Residuos z1,z2,-1:",R,"suma",s.simplify(sum(R)),"integral",s.simplify(2*s.pi*I*sum(R)))
print("|z1|=",s.Abs(z1))
G=(z**3+2*z+1)/(z-1)**3; r=s.residue(G,z,1); print("Res z=1:",r,"integral",2*s.pi*I*r)
th=s.symbols('th',real=True); zz=2*s.exp(I*th)
print("contorno |z|=2 numerico:",s.N(s.Integral(G.subs(z,zz)*zz.diff(th),(th,0,2*s.pi))))
print("F en |z|=3 numerico:",s.N(s.Integral(F.subs(z,3*s.exp(I*th))*(3*s.exp(I*th)).diff(th),(th,0,2*s.pi))))
