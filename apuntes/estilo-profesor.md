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

Fórmulas generales (tal como las escribe; en sistemas de 2º orden usa $(t,y,z)$ y $y_{n+1}$, $z_{n+1}$; título "R-K de 4º Sistemas:"):
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

## Método 4 — Integrales por residuos
1. `Evalúe` $\displaystyle\int \frac{\dots}{\dots}dz = 2\pi i\sum_{i=1}^{n} R_i$ — escribe la fórmula **en la misma línea del enunciado** y luego pone el resultado a la derecha ($=2\pi i(3) = 6\pi i$).
2. Debajo: el contorno `C: |z| = 2` y el centro `z₀ = 0`.
3. Polos: iguala el denominador a cero, $(z-1)^3 = 0 \to z = 1$.
4. Dibujo: plano con eje `i` y eje `x`, circunferencia con radio marcado ($R=2$) y el polo marcado con ×.
5. Define $F(z) = \dots$
6. Residuo — **nombres del profesor:** $R_1$ = fórmula de polo simple, $R_2$ = fórmula de polo de orden $k$ (no son "primer/segundo residuo"):
   $$R_1=\lim_{z\to z_0}(z-z_0)F(z) \qquad R_2=\frac{1}{(k-1)!}\lim_{z\to z_0}\frac{d^{k-1}}{dz^{k-1}}\{(z-z_0)^kF(z)\}$$
   - Polo de orden $m$: $R = \dfrac{1}{(m-1)!}\lim\limits_{z\to z_0}\dfrac{d^{m-1}}{dz^{m-1}}\{(z-z_0)^m F(z)\}$. Escribe $(3-1)!$ sin simplificar y las derivadas sucesivas **en columna** debajo del polinomio ($z^3+2z+1$, $3z^2+2$, $6z$).
   - Polo simple: $R = \lim\limits_{z\to z_k}(z-z_k)F(z) = \left.\dfrac{\dots}{\dots}\right|_{z=z_k}$, con barra vertical de evaluación. Al sustituir, tacha los términos que se cancelan.
7. Suma de residuos dentro de $2\pi i(\;\cdot\;)$, cada residuo como fracción ($\frac{1+8i}{8}$), luego agrupa.

## Formato de entrega en PDF (aprobado por el usuario)
Referencia exacta: `simulacros/simulacro-01/simulacro-01.pdf` · Plantilla: `plantillas/plantilla-pdf.tex`
- LaTeX (`pdflatex`), carta, márgenes 1.5 cm, 11 pt, **punto decimal** (`es-nodecimaldot`), `\sen`.
- Encabezado: "Simulacro NN — Matemáticas Aplicadas" centrado + línea horizontal.
- **Un ejercicio por página.** Título numerado en negrita con el nombre del tema como lo escribe el profesor.
- `Resolver` / `Evalúe` / `Calcule` en negrita + ecuación + condiciones en la misma línea.
- Procedimiento completo en el orden del profesor, sin explicaciones en prosa.
- Fórmulas generales del método antes de sustituir (R-K), recta de nodos con TikZ (diferencias finitas), dibujo del contorno con TikZ (variable compleja).
- 4 decimales **truncados**; en R-K los valores truncados se propagan a los pasos siguientes; en sistemas $AX=B$ se resuelve exacto y se trunca el resultado.
- **Resultado final en recuadro** (`\boxed`), en tabla cuando hay varios valores.
- Solo notas al pie en `\footnotesize` con $^{*}$ para supuestos o errores del enunciado.
- Los números se generan por script desde el cálculo verificado (`calculo.py` → `generar_tex.py`), nunca a mano.
