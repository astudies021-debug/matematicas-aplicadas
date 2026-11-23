# Ej1 se toma del simulacro 01 (mismo ejercicio, mismos numeros verificados); Ej2 y Ej3 nuevos.
import io, contextlib, runpy
with contextlib.redirect_stdout(io.StringIO()):
    ns=runpy.run_path('calculo.py')
src=open('../simulacro-01/simulacro-01.tex').read().split('\n')
pre="\n".join(src[:13]).replace("{amsmath,amssymb,geometry,array,tikz}","{amsmath,amssymb,geometry,array,tikz}\n\\usetikzlibrary{babel}").replace("Simulacro 01","Simulacro 02")
ej1="\n".join(src[13:65]).replace(r"{\large\textbf{1) Solución de E.D.O de 2º con valor inicial usando R-K de 4º}}",
      r"{\large\textbf{1) Resolver por Runge-Kutta de 4º}}")
ej1=ej1.replace(r"\[ \boxed", r"\[ \boxed")+"\n"+r"{\footnotesize $^{*}$ El enunciado no da el valor de $y'(1)$; se usa $y'(1)=3$ (mismo ejercicio de la hoja anterior).}"
Xt=[format(v.normalize(),'f') for v in ns['Xt']]
ej2=r"""
{\large\textbf{2) Solución de E.D.O de 2º con valores en la frontera usando diferencias finitas}}\\[6pt]
\textbf{Resolver} \quad $y''+4y'+5y=t \qquad y'(1)=2 \quad y(3)=0 \qquad n=5$\\[4pt]
$h=\dfrac{3-1}{5}=\dfrac{2}{5}=0.4$ \hfill
\begin{tikzpicture}[baseline=-3pt,x=1.25cm]
\draw[dashed] (-1,0)--(0,0); \draw (0,0)--(5,0);
\foreach \t/\i in {0/1,1/1.4,2/1.8,3/2.2,4/2.6,5/3}{\draw (\t,0.08)--(\t,-0.08); \node[above,font=\small] at (\t,0.08){\i};}
\foreach \k in {0,...,5}{\node[below,font=\small] at (\k,-0.08){$y_{\k}$};}
\draw (-1,0.08)--(-1,-0.08); \node[below,font=\small] at (-1,-0.08){$y_{-1}$}; \node[above,font=\scriptsize] at (-1,0.08){ficticio};
\end{tikzpicture}
\begin{align*}
&\frac{(y_{i+1}-2y_i+y_{i-1})}{h^2}+4\,\frac{(y_{i+1}-y_{i-1})}{2h}+5y_i=t_i\\[4pt]
&y_{i+1}-2y_i+y_{i-1}+2h(y_{i+1}-y_{i-1})+5h^2y_i=t_ih^2 && (A)\\[4pt]
&(1-2h)\,y_{i-1}-(2-5h^2)\,y_i+(1+2h)\,y_{i+1}=t_ih^2 && (B)
\end{align*}
$y'(1)=\dfrac{y_1-y_{-1}}{2h}=2 \;\Rightarrow\; y_{-1}=y_1-2(2)(0.4)=y_1-1.6 \qquad\qquad y_5=y(3)=0$
\begin{align*}
i=0 \;\; t_0=1 &\quad (1-2(0.4))\,y_{-1}-(2-5(0.4)^2)\,y_0+(1+2(0.4))\,y_1=1(0.4)^2 && (0)\\
&\quad 0.2(y_1-1.6)-1.2\,y_0+1.8\,y_1=0.16 \;\to\; -1.2\,y_0+2\,y_1=0.48\\
i=1 \;\; t_1=1.4 &\quad (1-2(0.4))\,y_0-(2-5(0.4)^2)\,y_1+(1+2(0.4))\,y_2=1.4(0.4)^2 && (1)\\
i=2 \;\; t_2=1.8 &\quad (1-2(0.4))\,y_1-(2-5(0.4)^2)\,y_2+(1+2(0.4))\,y_3=1.8(0.4)^2 && (2)\\
i=3 \;\; t_3=2.2 &\quad (1-2(0.4))\,y_2-(2-5(0.4)^2)\,y_3+(1+2(0.4))\,y_4=2.2(0.4)^2 && (3)\\
i=4 \;\; t_4=2.6 &\quad (1-2(0.4))\,y_3-(2-5(0.4)^2)\,y_4+(1+2(0.4))\,y_5=2.6(0.4)^2 && (4)\\
&\quad 0.2\,y_3-1.2\,y_4+1.8(0)=0.416
\end{align*}
\[
\underbrace{\begin{bmatrix}
-1.2 & 2 & 0 & 0 & 0\\
0.2 & -1.2 & 1.8 & 0 & 0\\
0 & 0.2 & -1.2 & 1.8 & 0\\
0 & 0 & 0.2 & -1.2 & 1.8\\
0 & 0 & 0 & 0.2 & -1.2
\end{bmatrix}}_{A}
\underbrace{\begin{bmatrix} y_0\\ y_1\\ y_2\\ y_3\\ y_4\end{bmatrix}}_{X}
=
\underbrace{\begin{bmatrix} 0.48\\ 0.224\\ 0.288\\ 0.352\\ 0.416\end{bmatrix}}_{B}
\qquad X=A^{-1}B
\]
\[
\boxed{\begin{array}{c|cccccc}
t & 1 & 1.4 & 1.8 & 2.2 & 2.6 & 3\\\hline
y & %s & %s & %s & %s & %s & 0
\end{array}}
\]
""" % tuple(Xt)
ej3=r"""
{\large\textbf{3) Teoría de la variable compleja --- Residuos}}\\[6pt]
\[
\textbf{Evalúe}\;\int\limits_{C}\frac{2z^2+5}{(z^2+2z+1)(z+1)}\,dz=2\pi i\sum_{i=1}^{n}R_i=2\pi i(2)=4\pi i
\]
\begin{minipage}{0.55\textwidth}
$C: |z+1|=2$\\[6pt]
$z_0=-1 \qquad r=2$\\[6pt]
$z^2+2z+1=(z+1)^2 \;\to\; (z+1)^2(z+1)=(z+1)^3$\\[6pt]
$(z+1)^3=0 \;\to\; z=-1 \quad$ (polo de orden 3)
\end{minipage}\hfill
\begin{minipage}{0.4\textwidth}
\begin{tikzpicture}[scale=0.75]
\draw[->] (-3.6,0)--(1.8,0) node[right]{$x$}; \draw[->] (0,-2.5)--(0,2.6) node[above]{$i$};
\draw[thick] (-1,0) circle (2);
\draw[->] (-1,0)--({-1+2*cos(45)},{2*sin(45)}) node[midway,above left]{\small $R=2$};
\node at (-1,0){$\times$}; \node[below] at (-1,-0.1){\small $-1$};
\end{tikzpicture}
\end{minipage}\\[6pt]
$F(z)=\dfrac{2z^2+5}{(z+1)^3}$
\[
R=\frac{1}{(3-1)!}\lim_{z\to-1}\frac{d^2}{dz^2}\{(z+1)^3F(z)\}
=\frac12\,\frac{d^2}{dz^2}\left\{\begin{matrix}2z^2+5\\ 4z\\ 4\end{matrix}\right\}\Bigg|_{z=-1}=\frac12(4)=2
\]
\[
\boxed{\int\limits_{C}\frac{2z^2+5}{(z^2+2z+1)(z+1)}\,dz=2\pi i(2)=4\pi i\approx 12.5663\,i}
\]
{\footnotesize $^{*}$ Si el denominador fuera $(z^2+2z+5)(z+1)$, los polos $-1\pm2i$ caerían \emph{sobre} $C$ ($|\pm2i|=2$) y la integral no estaría definida.}
"""
doc=pre+"\n"+ej1+"\n\\newpage\n"+ej2+"\n\\newpage\n"+ej3+"\n\\end{document}\n"
open('simulacro-02.tex','w').write(doc); print('ok',Xt)
