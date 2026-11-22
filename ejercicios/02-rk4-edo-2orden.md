# R-K de 4º — E.D.O de 2º orden (reducida a sistema)
Pizarra: `referencias/pizarra/rk4-edo-2orden.jpg` · Verificación: `verificacion/verificar_pizarra.py`

**Resolver** $\;y'' - 4y' + 4y = 0 \qquad y(0) = y'(0) = 1 \qquad H = 0.1$

$$f:\begin{cases} y' = z \\ z' = 4z - 4y \end{cases}:g \qquad y(0) = z(0) = 1$$

Para $t=0 \quad y=1 \quad z=1$

$K_1 = 0.1f(0,1,1) = 0.1[1] = 0.1$

$C_1 = 0.1g(\;''\;) = 0.1[4(1)-4(1)] = 0$

$K_2 = 0.1f\left(0+\frac{0.1}{2},\,1+\frac{0.1}{2},\,1+\frac{0}{2}\right) = 0.1f(0.05,\,1.05,\,1) = 0.1[1] = 0.1$

$C_2 = 0.1g(0.05,\,1.05,\,1) = 0.1[4(1)-4(1.05)] = -0.02$

$K_3 = 0.1f\left(0.05,\,1+\frac{0.1}{2},\,1-\frac{0.02}{2}\right) = 0.1f(0.05,\,1.05,\,0.99) = 0.1[0.99] = 0.099$

$C_3 = 0.1g(\;''\;) = 0.1[4(0.99)-4(1.05)] = -0.024$

$K_4 = 0.1f(0+0.1,\,1+0.099,\,1-0.024) = 0.1f(0.1,\,1.099,\,0.976) = 0.1[0.976] = 0.0976$

$C_4 = 0.1g(\;''\;) = 0.1[4(0.976)-4(1.099)] = -0.0492$

**1ª iter**

$y(0.1) = 1 + \big(0.1 + 2(0.1+0.099) + 0.0976\big)/6 = 1.0992$

$z(0.1) = 1 + \big(0 + 2(-0.02-0.024) + (-0.0492)\big)/6 = 0.9771$ *(cortado en la foto; completado)*

## Observaciones
- Todos los valores de la pizarra son correctos.
- $y(0.1)=1.099266\ldots$: escribe $1.0992$ → confirma que **trunca** a 4 decimales.
- Solución analítica: $y=(1-t)e^{2t}$ → $y(0.1)=0.9e^{0.2}=1.0992625$, $y'(0.1)=0.8e^{0.2}=0.9771222$. RK4 coincide en 5 cifras.
