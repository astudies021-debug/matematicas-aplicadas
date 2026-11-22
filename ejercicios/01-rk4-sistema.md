# R-K de 4º — Sistema de E.D.O con valor inicial
Pizarra: `referencias/pizarra/rk4-sistema.jpg` · Verificación: `verificacion/rk4_sistema.m`, `verificacion/verificar_pizarra.py`

**Resolver**
$$f:\begin{cases} x' = 3x - 3y + 2 \\ y' = -6x - t\end{cases}:g \qquad x(0)=1,\; y(0)=-1$$

Para $t=0 \quad x=1 \quad y=-1 \quad H=0.1$

$K_1 = 0.1f(0,1,-1) = 0.1[3(1)-3(-1)+2] = 0.8$

$C_1 = 0.1g(0,1,-1) = 0.1[-6(1)-0] = -0.6$

$K_2 = 0.1f\left(0+\frac{0.1}{2},\,1+\frac{0.8}{2},\,-1-\frac{0.6}{2}\right) = 0.1f(0.05,\,1.4,\,-1.3) = 0.1[3(1.4)-3(-1.3)+2] = 1.01$

$C_2 = 0.1g(0.05,\,1.4,\,-1.3) = 0.1[-6(1.4)-0.05] = -0.845$

$K_3 = 0.1f\left(0.05,\,1+\frac{1.01}{2},\,-1-\frac{0.845}{2}\right) = 0.1f(0.05,\,1.505,\,-1.4225) = 0.1[3(1.505)-3(-1.4225)+2] = 1.0782$

$C_3 = 0.1g(0.05,\,1.505,\,-1.4225) = 0.1[-6(1.505)-0.05] = -0.908$

$K_4 = 0.1f(0+0.1,\,1+1.0782,\,-1-0.908) = 0.1f(0.1,\,2.0782,\,-1.908) = 0.1[3(2.0782)-3(-1.908)+2] = 1.3958$

$C_4 = 0.1g(\;''\;) = 0.1[-6(2.0782)-0.1] = -1.2569$

**1ª iter** *(no se ve en la foto; completado con sus fórmulas)*

$x(0.1) = 1 + \big(0.8 + 2(1.01+1.0782) + 1.3958\big)/6 = 2.0620$

$y(0.1) = -1 + \big(-0.6 + 2(-0.845-0.908) - 1.2569\big)/6 = -1.8938$

## Observaciones
- ⚠️ En la pizarra $C_2$ aparece como $0.1[-6(1)-0.05]$: debe ser $-6(1.4)$. El resultado $-0.845$ que escribe **sí es correcto**; es un desliz al copiar.
- Valores con 4 decimales truncados (sin truncar: $K_3=1.07825$, $K_4=1.395875$).
- Solución analítica (SymPy): $x(0.1)=2.06295$, $y(0.1)=-1.89470$. Error de RK4 con $H=0.1$ ≈ $9\times10^{-4}$; esperable con un único paso de tamaño $0.1$ y coeficientes del orden de 3–6.
