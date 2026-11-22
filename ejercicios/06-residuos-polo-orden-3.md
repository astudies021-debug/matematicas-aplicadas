# Residuos — polo de orden 3
Pizarra: `referencias/pizarra/residuos.jpg` (parte central izquierda) · Verificación: `verificacion/verificar_pizarra.py`

$$\text{Evalúe} \int\limits_{C} \frac{z^3+2z+1}{(z-1)^3}\,dz = 2\pi i\sum_{i=1}^{n}R_i = 2\pi i(3) = 6\pi i$$

$C: |z| = 2$

$z_0 = 0 \qquad\qquad (z-1)^3 = 0 \;\to\; z = 1$

*(Dibujo: circunferencia de radio $R=2$ centrada en el origen, polo $z=1$ marcado con × dentro.)*

$F(z) = \dfrac{z^3+2z+1}{(z-1)^3}$

$R = \dfrac{1}{(3-1)!}\lim\limits_{z\to1}\dfrac{d^2}{dz^2}\{(z-1)^3F(z)\}$

$= \dfrac12\left.\dfrac{d^2}{dz^2}\left\{\begin{matrix} z^3+2z+1 \\ 3z^2+2 \\ 6z \end{matrix}\right\}\right|_{z=1} = \dfrac12(6z) = 3z\Big|_{z=1} = 3$

$$\int\limits_{C} \frac{z^3+2z+1}{(z-1)^3}\,dz = 2\pi i(3) = 6\pi i$$

## Observaciones
- Todo correcto en la pizarra. Verificado con SymPy (residuo 3) e integrando numéricamente sobre $|z|=2$: $18.8496\,i = 6\pi i$.
- El subíndice del residuo en la pizarra se ve como $R_2$; con un único polo sería $R_1$. Escribe el que use tu profesor.
- El polo $z=1$ está dentro de $C$ porque $|1| < 2$. **Siempre** comprobar qué polos quedan dentro antes de sumar.
