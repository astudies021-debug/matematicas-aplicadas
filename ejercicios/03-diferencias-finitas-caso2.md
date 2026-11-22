# Diferencias finitas — E.D.O de 2º con valores en la frontera (Caso 2)
Pizarra: `referencias/pizarra/dif-finitas-caso2.jpg` · Verificación: `verificacion/dif_finitas_caso2.m`

**Resolver** $\;y'' - (1 - t/5)\,y = t \qquad y(1) = 2 \quad y'(3) = -1$ &nbsp; **Caso 2**

$h = \dfrac{3-1}{4} = \dfrac{2}{4} = \dfrac12$

| $t$ | 1 | 1.5 | 2 | 2.5 | 3 | (ficticio) |
|---|---|---|---|---|---|---|
| | $y_0$ | $y_1$ | $y_2$ | $y_3$ | $y_4$ | $y_5$ |

$$\frac{(y_{i+1} - 2y_i + y_{i-1})}{h^2} - (1 - t_i/5)\,y_i = t_i$$

$$y_{i+1} - 2y_i + y_{i-1} - h^2(1 - t_i/5)\,y_i = t_i h^2 \qquad (A)$$

$$y_{i-1} - \left(2 + h^2\left(1 - \frac{t_i}{5}\right)\right)y_i + y_{i+1} = t_i h^2 \qquad (B)$$

$i=0 \quad t_0 = 1 \quad y_0 = 2$

$i=1 \quad t_1=1.5 \quad y_0 - \left(2 + (\tfrac12)^2(1 - \tfrac{1.5}{5})\right)y_1 + y_2 = 1.5(\tfrac12)^2 \qquad (1)$

$i=2 \quad t_2=2 \quad\;\; y_1 - \left(2 + (\tfrac12)^2(1 - \tfrac{2}{5})\right)y_2 + y_3 = 2(\tfrac12)^2 \qquad (2)$

$i=3 \quad t_3=2.5 \quad y_2 - \left(2 + (\tfrac12)^2(1 - \tfrac{2.5}{5})\right)y_3 + y_4 = 2.5(\tfrac12)^2 \qquad (3)$

$i=4 \quad t_4=3 \quad\;\; y_3 - \left(2 + (\tfrac12)^2(1 - \tfrac{3}{5})\right)y_4 + y_5 = 3(\tfrac12)^2 \qquad (4)$

**Condición en la derivada:**
$y'(3) = \dfrac{y_5 - y_3}{2h} = -1 \;\Rightarrow\; y_5 = y_3 - 2(\tfrac12) = y_3 - 1$

$(4) \to y_3 - \left(2 + (\tfrac12)^2(1 - \tfrac35)\right)y_4 + y_3 - 1 = \tfrac34 \;\Rightarrow\; 2y_3 - \left(2 + (\tfrac12)^2(1-\tfrac35)\right)y_4 = \tfrac34 + 1 \qquad (4)$

$$
\underbrace{\begin{bmatrix}
-\left(2+(\frac12)^2(\frac{5-1.5}{5})\right) & 1 & 0 & 0\\
1 & -\left(2+(\frac12)^2(\frac{5-2}{5})\right) & 1 & 0\\
0 & 1 & -\left(2+(\frac12)^2(\frac{5-2.5}{5})\right) & 1\\
0 & 0 & 2 & -\left(2+(\frac12)^2(\frac{5-3}{5})\right)
\end{bmatrix}}_{A}
\underbrace{\begin{bmatrix} y_1\\ y_2\\ y_3\\ y_4\end{bmatrix}}_{X}
=
\underbrace{\begin{bmatrix} 1.5(\frac12)^2 - 2\\ 2(\frac12)^2\\ 2.5(\frac12)^2\\ 1 + \frac34\end{bmatrix}}_{B}
$$

$X = A^{-1}B$ *(la foto se corta aquí; completado y verificado)*

Valores numéricos: $A = \begin{bmatrix}-2.175 & 1 & 0 & 0\\ 1 & -2.15 & 1 & 0\\ 0 & 1 & -2.125 & 1\\ 0 & 0 & 2 & -2.1\end{bmatrix}$, $\;B = \begin{bmatrix}-1.625\\ 0.5\\ 0.625\\ 1.75\end{bmatrix}$

| $t$ | 1 | 1.5 | 2 | 2.5 | 3 |
|---|---|---|---|---|---|
| $y$ | 2 | $y_1 = 0.2000$ | $y_2 = -1.1899$ | $y_3 = -2.2584$ | $y_4 = -2.9842$ |

(Exactos: $y_1 = \frac{57415}{287057}$, $y_2 = -\frac{341590}{287057}$, $y_3 = -\frac{648305}{287057}$, $y_4 = -\frac{1713295}{574114}$; decimales truncados a 4 cifras como el profesor.)

## Observaciones
- "Caso 2" = condición de **derivada** en un extremo → requiere nodo ficticio $y_5$ y diferencia central.
- En la foto, el exponente de $(\frac12)$ en la fila $i=3$ parece un 3; debe ser **2** ($h^2$).
- Fila 4 de $A$: el 2 viene de $y_3 + y_3$ al sustituir $y_5$.
