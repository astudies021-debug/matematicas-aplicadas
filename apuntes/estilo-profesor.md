# Estilo del profesor (extraído de la pizarra)

> Fuente: fotos en `referencias/pizarra/`. Lo marcado como **[inferido]** se deduce de los números, no está escrito.

## Notación general
- Título del tema arriba a la izquierda (p. ej. "Solución de Sistemas de E.D.O con valor inicial usando R-K de 4º").
- Enunciado: `Resolver` + ecuación(es) + condiciones + paso. **No hay enunciado en prosa.**
- E.D.O. se escribe "E.D.O"; orden con superíndice: "2º", "4º".
- Paso: **`H` mayúscula** en Runge-Kutta; **`h` minúscula** en diferencias finitas.
- Derivadas con prima: $x'$, $y'$, $y''$.
- Cálculos con **4 decimales, truncando (no redondeando)** **[inferido]**: $K_3 = 1.07825 \to 1.0782$, $K_4 = 1.39586 \to 1.3958$, $y(0.1)=1.09926\ldots \to 1.0992$.
- Usa `(  "  )` (comillas) para "mismos argumentos que la línea anterior".
- Marca con ✓ los resultados parciales comprobados.

## Método 1 — R-K de 4º para sistemas (valor inicial)
1. Escribir a la izquierda las fórmulas generales (ver abajo).
2. Nombrar cada ecuación con su función: `f:` y `g:` con llave `{`.
3. Condiciones iniciales a la derecha: $x(0)=1$, $y(0)=-1$.
4. Línea `Para t=0  x=1  y=-1  H=0.1`.
5. Calcular **intercalado**: $K_1, C_1, K_2, C_2, K_3, C_3, K_4, C_4$ ($K$ para la 1ª variable, $C$ para la 2ª).
6. Cada coeficiente en 3 pasos: $K_2 = 0.1f(\text{argumentos sin simplificar}) = 0.1f(\text{argumentos numéricos}) = 0.1[\text{sustitución}] = \text{resultado}$.
7. Cerrar con `1ª iter` y $x(0.1)$, $y(0.1)$ (o $y(0.1)$, $z(0.1)$).

Fórmulas generales (tal como las escribe):
$$
\begin{aligned}
K_1 &= Hf(t,x,y) & C_1 &= Hg(\;''\;)\\
K_2 &= Hf\!\left(t+\tfrac{H}{2},\,x+\tfrac{K_1}{2},\,y+\tfrac{C_1}{2}\right) & C_2 &= Hg(\;''\;)\\
K_3 &= Hf\!\left(t+\tfrac{H}{2},\,x+\tfrac{K_2}{2},\,y+\tfrac{C_2}{2}\right) & C_3 &= Hg(\;''\;)\\
K_4 &= Hf(t+H,\,x+K_3,\,y+C_3) & C_4 &= Hg(\;''\;)
\end{aligned}
$$
$$x_{n+1} = x_n + \big(K_1 + 2(K_2+K_3) + K_4\big)/6 \qquad y_{n+1} = y_n + \big(C_1 + 2(C_2+C_3) + C_4\big)/6$$

**EDO de 2º orden:** se reduce a sistema con $z = y'$: `f: y' = z`, `g: z' = ...`; las fórmulas pasan a $(t,y,z)$.

## Método 2 — Diferencias finitas, valores en la frontera
1. Calcular $h = \dfrac{b-a}{n}$ (escribe $h=\frac{3-1}{4}=\frac{2}{4}=\frac12$).
2. Dibujar la recta con los nodos $t$ arriba y $y_0, y_1, \dots$ abajo; punto **ficticio** $y_5$ si hay condición en la derivada.
3. Sustituir $y'' \approx \dfrac{y_{i+1}-2y_i+y_{i-1}}{h^2}$ en la EDO.
4. Multiplicar por $h^2$ → ecuación **(A)**; agrupar por $y_{i-1}, y_i, y_{i+1}$ → ecuación **(B)**.
5. Tabla por renglones: `i=1  t1=1.5  ...  (1)`, `i=2 ... (2)`, etc. **No evalúa los coeficientes**: deja $(\frac12)^2(1-\frac{1.5}{5})$.
6. Condición de derivada (**Caso 2**) con diferencia central: $y'(3)=\dfrac{y_5-y_3}{2h}$ → despejar $y_5$ y sustituir en la última ecuación.
7. Matriz $A$ (columnas $y_1\dots y_4$), vector $X$, vector $B$, con llaves debajo: $AX=B$, $X=A^{-1}B$.
   - En $A$ escribe $(1-\frac{t}{5})$ como $\frac{5-t}{5}$.
   - Los valores conocidos ($y_0$) pasan a $B$ restando: $1.5(\frac12)^2-2$.

## Método 3 — Integral de línea compleja por trayectorias
1. $z = x + iy$. Dibujo del contorno en el plano (eje `imag`, eje `x`), vértices con coordenadas y trayectorias numeradas I, II, III, IV en romanos.
2. Por cada trayectoria: `Tray I: y=0  z=x → dz=dx`.
3. Integral con límites en la variable que cambia, desarrollar el cuadrado, integrar, evaluar con barra $\Big|_a^b$.
4. Sumar todas: $\oint z^2\,dz = 0$ (función analítica, teorema de Cauchy).
