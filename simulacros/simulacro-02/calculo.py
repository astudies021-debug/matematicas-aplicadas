# Simulacro 02 - verificacion
import sympy as s, runpy, io, contextlib
from decimal import Decimal as D, ROUND_DOWN
T=lambda v: D(str(v)).quantize(D('0.0001'),rounding=ROUND_DOWN)
# Ej1: mismo ejercicio del simulacro 01 (y'(1)=3)
with contextlib.redirect_stdout(io.StringIO()):
    ns1=runpy.run_path('../simulacro-01/calculo.py')
E1=ns1['E1']
# Ej2
t=s.symbols('t'); h=s.Rational(2,5)
a,b,c=1-2*h,2-5*h**2,1+2*h
print('Ej2 coef',a,b,c,'h^2',h**2)
A=s.Matrix([[-b,a+c,0,0,0],[a,-b,c,0,0],[0,a,-b,c,0],[0,0,a,-b,c],[0,0,0,a,-b]])
B=s.Matrix([1*h**2+a*2*(2*h), s.Rational(14,10)*h**2, s.Rational(18,10)*h**2, s.Rational(22,10)*h**2, s.Rational(26,10)*h**2])
X=A.LUsolve(B); print('Ej2 A',A,'B',B.T); print('Ej2 X',X.T,[float(v) for v in X])
yv=list(X)+[0]; ym1=yv[1]-4*h
assert a*ym1-b*yv[0]+c*yv[1]==1*h**2
for i in range(1,5): assert a*yv[i-1]-b*yv[i]+c*yv[i+1]==(1+i*h)*h**2
Y=s.Function('y'); sol=s.dsolve(Y(t).diff(t,2)+4*Y(t).diff(t)+5*Y(t)-t,ics={Y(t).diff(t).subs(t,1):2,Y(3):0}).rhs
print('Ej2 analitica',[round(float(sol.subs(t,1+k*h)),6) for k in range(6)])
Xt=[T(s.N(v,30)) for v in X]; print('Ej2 trunc',Xt)
# Ej3
z=s.symbols('z'); F=(2*z**2+5)/((z**2+2*z+1)*(z+1))
r=s.residue(F,z,-1); print('Ej3 residuo',r,'integral',2*s.pi*s.I*r)
th=s.symbols('th',real=True); zz=-1+2*s.exp(s.I*th)
print('Ej3 numerico',s.N(s.Integral(F.subs(z,zz)*zz.diff(th),(th,0,2*s.pi))))
print('Ej3 derivadas',s.diff(2*z**2+5,z),s.diff(2*z**2+5,z,2))
