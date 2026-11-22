# Teoría de la variable compleja — $\oint z^2\,dz$ sobre un rectángulo
Pizarra: `referencias/pizarra/variable-compleja-rectangulo.jpg` · Verificación: `verificacion/verificar_pizarra.py`

$z = x + iy$. **Ejemplo:** contorno $(1,0)\to(2,0)\to(2,1)\to(1,1)\to(1,0)$, trayectorias I, II, III, IV.
$$\oint z^2\,dz = 0$$

**soln:**

**Tray I:** $y=0 \quad z=x \;\to\; dz=dx$
$$\int z^2dz = \int_1^2 x^2dx = \frac{x^3}{3}\Big|_1^2 = \frac83 - \frac13 = \frac73$$

**Tray II:** $x=2 \quad z=2+iy \;\to\; dz = i\,dy$
$$\int z^2dz = i\int_0^1(2+iy)^2dy = i\int_0^1(4+4yi-y^2)\,dy = i\left(4y+2y^2i-\frac{y^3}{3}\right)\Big|_0^1 = i\left(4+2i-\frac13\right) = \frac{11}{3}i - 2$$

**Tray III:** $y=1 \quad z=x+i \quad dz=dx$
$$\int_2^1(x+i)^2dx = \int_2^1(x^2+2xi-1)\,dx = \frac{x^3}{3}+x^2i-x\Big|_2^1 = \left(\frac13+i-1\right)-\left(\frac83+4i-2\right) = -\frac43 - 3i$$

**Tray IV:** $x=1 \quad z=1+iy \;\to\; dz = i\,dy$
$$\int z^2dz = i\int_1^0(1+iy)^2dy = i\int_1^0(1+2yi-y^2)\,dy = i\left(y+y^2i-\frac{y^3}{3}\right)\Big|_1^0 = -i\left(1+i-\frac13\right) = 1 - \frac23 i$$

**Suma:** $\frac73 + \left(\frac{11}{3}i-2\right) + \left(-\frac43-3i\right) + \left(1-\frac23i\right) = 0 + 0i = 0 \;\checkmark$

## Observaciones
- ⚠️ **Tray III en la pizarra:** leo $-\frac43 - i$. Lo correcto es $-\frac43 - 3i$: al evaluar $x^2i$ en $x=2$ da $4i$, no $2i$. Con $-\frac43 - i$ la suma **no** daría 0. Compara con tu cuaderno; puede ser la foto o un error en la pizarra.
- Tray IV aparece cortada en la foto; está completada aquí.
- Que la suma sea 0 es el **teorema de Cauchy-Goursat**: $z^2$ es analítica en todo $\mathbb{C}$ y el contorno es cerrado. Sirve como comprobación de cada tramo.
