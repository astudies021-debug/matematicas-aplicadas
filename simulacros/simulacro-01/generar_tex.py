import runpy, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    ns=runpy.run_path('calculo.py')
E1,fmt,D,T,sen,H=ns['E1'],ns['fmt'],ns['D'],ns['T'],ns['sen'],ns['H']
def p(v):  # numero con parentesis si es negativo
    s=fmt(v); return f"({s})" if v<0 else s
def sg(v): return f"+ {fmt(v)}" if v>=0 else f"- {fmt(-v)}"
L=[]
for n,e in enumerate(E1,1):
    t,y,z=e['t'],e['y'],e['z'];K,C=e['K'],e['C'];a2,a3,a4=e['a2'],e['a3'],e['a4']
    L.append(rf"\textbf{{Para}} $t={fmt(t)}\quad y={fmt(y)}\quad z={fmt(z)}\quad H=0.1$\\[-2pt]")
    L.append(r"\begin{align*}")
    gb=lambda a: rf"0.1\left[3({fmt(a[2])})+4({fmt(a[1])})+2\sen({fmt(a[0])})\right]"
    L.append(rf"K_1&=0.1f({fmt(t)},{fmt(y)},{fmt(z)})=0.1[{fmt(z)}]={fmt(K[0])}\\")
    L.append(rf"C_1&=0.1g(\,''\,)={gb((t,y,z))}={fmt(C[0])}\\")
    L.append(rf"K_2&=0.1f\left({fmt(t)}+\tfrac{{0.1}}{{2}},\,{fmt(y)}+\tfrac{{{fmt(K[0])}}}{{2}},\,{fmt(z)}+\tfrac{{{fmt(C[0])}}}{{2}}\right)=0.1f({fmt(a2[0])},\,{fmt(a2[1])},\,{fmt(a2[2])})=0.1[{fmt(a2[2])}]={fmt(K[1])}\\")
    L.append(rf"C_2&=0.1g({fmt(a2[0])},\,{fmt(a2[1])},\,{fmt(a2[2])})={gb(a2)}={fmt(C[1])}\\")
    L.append(rf"K_3&=0.1f\left({fmt(a3[0])},\,{fmt(y)}+\tfrac{{{fmt(K[1])}}}{{2}},\,{fmt(z)}+\tfrac{{{fmt(C[1])}}}{{2}}\right)=0.1f({fmt(a3[0])},\,{fmt(a3[1])},\,{fmt(a3[2])})=0.1[{fmt(a3[2])}]={fmt(K[2])}\\")
    L.append(rf"C_3&=0.1g(\,''\,)={gb(a3)}={fmt(C[2])}\\")
    L.append(rf"K_4&=0.1f({fmt(t)}+0.1,\,{fmt(y)}+{fmt(K[2])},\,{fmt(z)}+{fmt(C[2])})=0.1f({fmt(a4[0])},\,{fmt(a4[1])},\,{fmt(a4[2])})=0.1[{fmt(a4[2])}]={fmt(K[3])}\\")
    L.append(rf"C_4&=0.1g(\,''\,)={gb(a4)}={fmt(C[3])}")
    L.append(r"\end{align*}")
    tn=fmt(t+H)
    L.append(rf"\textbf{{{n}\textsuperscript{{a}} iter}}\vspace{{-4pt}}")
    L.append(r"\begin{align*}")
    L.append(rf"y({tn})&={fmt(y)}+\big({fmt(K[0])}+2({fmt(K[1])}+{fmt(K[2])})+{fmt(K[3])}\big)/6={fmt(e['yn'])}\\")
    L.append(rf"z({tn})&={fmt(z)}+\big({fmt(C[0])}+2({fmt(C[1])}+{fmt(C[2])})+{fmt(C[3])}\big)/6={fmt(e['zn'])}")
    L.append(r"\end{align*}")
ej1="\n".join(L)
last=E1[-1]
res1=rf"\boxed{{\begin{{array}}{{c|ccc}} t & 1 & 1.1 & 1.2\\\hline y & 2 & {fmt(E1[0]['yn'])} & {fmt(last['yn'])}\\ z=y' & 3 & {fmt(E1[0]['zn'])} & {fmt(last['zn'])}\end{{array}}}}"
# Ej2: solucion exacta del sistema, truncada
from fractions import Fraction as Fr
import sympy as s
A=s.Matrix([[2,0,0,0,0],[s.Rational(-19,10),s.Rational(7,10),0,0,0],[s.Rational(13,10),s.Rational(-19,10),s.Rational(7,10),0,0],[0,s.Rational(13,10),s.Rational(-19,10),s.Rational(7,10),0],[0,0,s.Rational(13,10),s.Rational(-19,10),s.Rational(7,10)]])
B=s.Matrix([s.Rational(191,100),s.Rational(11,1000)-s.Rational(13,10),s.Rational(12,1000),s.Rational(13,1000),s.Rational(14,1000)])
X=A.LUsolve(B); Xt=[T(D(str(s.N(v,30)))) for v in X]
assert all(abs(float(a)-float(b))<1e-4 for a,b in zip(Xt,ns['ye'][1:]))
xs=[fmt(v) for v in Xt]
tpl=open('simulacro-01.tpl.tex').read()
tpl=tpl.replace('%%EJ1%%',ej1).replace('%%RES1%%',res1)
for i,v in enumerate(xs,1): tpl=tpl.replace(f'%%Y{i}%%',v)
open('simulacro-01.tex','w').write(tpl); print('ok',xs)
