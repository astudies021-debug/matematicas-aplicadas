# Residuos — polos simples
Pizarra: `referencias/pizarra/residuos.jpg` (parte superior izquierda y derecha) · Verificación: `verificacion/verificar_pizarra.py`

> ⚠️ El enunciado completo (en especial el **contorno C**) no aparece en la foto. Lo reconstruido: los polos son
> $z = -1$, $z_1 = -1+2i$, $z_2 = -1-2i$, es decir $(z+1)(z^2+2z+5)$. Como suma los tres residuos, el contorno
> debe encerrar los tres polos ($|z_{1,2}| = \sqrt5 \approx 2.24$; p. ej. $|z| = 3$). **Confírmalo con tu cuaderno.**

$$\int \frac{2z^2+5}{(z+1)(z-z_1)(z-z_2)}\,dz \qquad z_1 = -1+2i \quad z_2 = -1-2i$$

$R_2 = \lim\limits_{z\to z_2}(z-z_2)F(z) = \left.\dfrac{2z^2+5}{(z+1)(z-z_1)}\right|_{z=z_2}$

$= \dfrac{2(-1-2i)^2+5}{(-1-2i+1)(-1-2i+1-2i)} = \dfrac{2(1+4i-4)+5}{(-2i)(-4i)} = \dfrac{-1+8i}{-8} = \dfrac{1-8i}{8}$

$R_1 = \left.\dfrac{2z^2+5}{(z+1)(z-z_2)}\right|_{z=z_1} = \dfrac{2(-1+2i)^2+5}{(-1+2i+1)(-1+2i+1+2i)} = \dfrac{2(1-4i-4)+5}{(2i)(4i)} = \dfrac{-1-8i}{-8} = \dfrac{1+8i}{8}$

$R_{-1} = \left.\dfrac{2z^2+5}{(z-z_1)(z-z_2)}\right|_{z=-1} = \dfrac{2(1)+5}{(-2i)(2i)} = \dfrac{7}{4}$ *(no está en la foto; completado)*

$$\int \frac{2z^2+5}{(z+1)(z-z_1)(z-z_2)}\,dz = 2\pi i\left(\frac{1+8i}{8} + \frac{1-8i}{8} + \frac74\right) = 2\pi i\left(\frac14+\frac74\right) = 2\pi i\left(\frac84\right) = 2\pi i(2) = 4\pi i$$

## Observaciones
- ⚠️ El final de la pizarra parece decir $\pi i$. El resultado correcto es **$4\pi i$**: $\frac14+\frac74 = 2$ y $2\pi i\cdot 2 = 4\pi i$. Comprobado integrando numéricamente sobre $|z|=3$: $12.566\,i = 4\pi i$.
- En la pizarra el denominador de $R_1$ se ve como $(i\cdot 4i)$; debe ser $(2i)(4i) = -8$ (su resultado $\frac{1+8i}{8}$ sí es correcto).
- Comprobación rápida: si el grado del numerador es uno menos que el del denominador, la suma de **todos** los residuos finitos = cociente de coeficientes principales $= \frac21 = 2$ ✓.
- Los residuos en polos conjugados salen conjugados ($\frac{1\pm8i}{8}$): el numerador tiene coeficientes reales.
