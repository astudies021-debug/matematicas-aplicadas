# Simulacro 01: calculo con 4 decimales truncados (estilo profesor) + verificacion exacta
from decimal import Decimal as D, ROUND_DOWN, getcontext
import mpmath as mp, sympy as s
getcontext().prec=40; mp.mp.dps=40
T=lambda v: D(v).quantize(D('0.0001'),rounding=ROUND_DOWN)
sen=lambda t: D(str(mp.sin(mp.mpf(str(t)))))
fmt=lambda v: format(v.normalize(),'f') if v!=0 else '0'
# ---------- Ej1 RK4 ----------
H=D('0.1')
f=lambda t,y,z: z
g=lambda t,y,z: 3*z+4*y+2*sen(t)
t,y,z=D(1),D(2),D(3); E1=[]
for it in (1,2):
    K1=T(H*f(t,y,z));C1=T(H*g(t,y,z))
    a2=(t+H/2,y+K1/2,z+C1/2);K2=T(H*f(*a2));C2=T(H*g(*a2))
    a3=(t+H/2,y+K2/2,z+C2/2);K3=T(H*f(*a3));C3=T(H*g(*a3))
    a4=(t+H,y+K3,z+C3);K4=T(H*f(*a4));C4=T(H*g(*a4))
    yn=T(y+(K1+2*(K2+K3)+K4)/6); zn=T(z+(C1+2*(C2+C3)+C4)/6)
    E1.append(dict(t=t,y=y,z=z,K=[K1,K2,K3,K4],C=[C1,C2,C3,C4],a2=a2,a3=a3,a4=a4,yn=yn,zn=zn))
    t,y,z=t+H,yn,zn
for e in E1: print('Ej1',fmt(e['t']),[fmt(k) for k in e['K']],[fmt(c) for c in e['C']],fmt(e['yn']),fmt(e['zn']))
tt=s.symbols('t'); Y=s.Function('y')
sol=s.dsolve(Y(tt).diff(tt,2)-3*Y(tt).diff(tt)-4*Y(tt)-2*s.sin(tt),ics={Y(1):2,Y(tt).diff(tt).subs(tt,1):3}).rhs
print('Ej1 analitica y(1.1),y(1.2):',s.N(sol.subs(tt,1.1),8),s.N(sol.subs(tt,1.2),8),' z:',s.N(sol.diff(tt).subs(tt,1.1),8),s.N(sol.diff(tt).subs(tt,1.2),8))
# ---------- Ej2 diferencias finitas, valor inicial ----------
h=D('0.1'); a=1+3*h; b=2-10*h*h; c=1-3*h   # a y_{i-1} - b y_i + c y_{i+1} = t_i h^2
yv={0:D(1)}; E2=[]
# i=0 con y_{-1}=y_1:  (a+c) y1 - b y0 = t0 h^2
y1=T((D(1)*h*h + b*yv[0])/(a+c)); yv[1]=y1; E2.append((0,D(1),y1))
for i in range(1,5):
    ti=1+i*h; yv[i+1]=T((ti*h*h - a*yv[i-1] + b*yv[i])/c); E2.append((i,ti,yv[i+1]))
print('Ej2 coef',a,b,c); print('Ej2',[(i,fmt(ti),fmt(v)) for i,ti,v in E2])
# exacto (sin truncar) con fracciones
from fractions import Fraction as Fr
hh=Fr(1,10);A=1+3*hh;B=2-10*hh*hh;Cc=1-3*hh;ye=[Fr(1)];ye.append((hh*hh+B)/(A+Cc))
for i in range(1,5): ye.append(((1+i*hh)*hh*hh-A*ye[i-1]+B*ye[i])/Cc)
print('Ej2 exacto',[float(v) for v in ye])
# comprobar sustitucion en ecuaciones discretas
print('Ej2 residuo i=0',(A+Cc)*ye[1]-B*ye[0]-hh*hh,[A*ye[i-1]-B*ye[i]+Cc*ye[i+1]-(1+i*hh)*hh*hh for i in range(1,5)])
sol2=s.dsolve(Y(tt).diff(tt,2)-6*Y(tt).diff(tt)+10*Y(tt)-tt,ics={Y(1):1,Y(tt).diff(tt).subs(tt,1):0}).rhs
print('Ej2 analitica',[s.N(sol2.subs(tt,1+k/10),6) for k in range(6)])
# ---------- Ej3 ----------
x,yy=s.symbols('x y',real=True);I=s.I;zz=s.symbols('z')
F=lambda Z:(Z-I*Z)**2
c1=s.expand(I*s.integrate(s.expand(F(I*yy)),(yy,0,2)))
c2=s.expand(s.integrate(s.expand(F(x+2*I)),(x,0,4)))
c3=s.expand(s.integrate(s.expand(F(x+I*x/2)*(1+I/2)),(x,0,4)))
print('Ej3 C1',c1,'C2',c2,'C1+C2',s.expand(c1+c2),'C3',c3,'directo',s.expand(s.integrate(F(zz),(zz,0,4+2*I))))
print('Ej3 integrandos C1',s.expand(F(I*yy)),' C2',s.expand(F(x+2*I)),' C3',s.expand(F(x+I*x/2)*(1+I/2)))
