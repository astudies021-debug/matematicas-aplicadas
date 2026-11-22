% Diferencias finitas, Caso 2: y'' - (1 - t/5) y = t, y(1) = 2, y'(3) = -1, h = 1/2
h = 1/2; t = [1.5 2 2.5 3];
c = 2 + h^2*(1 - t/5);                 % coeficiente de y_i en la ecuación (B)
A = [-c(1) 1 0 0; 1 -c(2) 1 0; 0 1 -c(3) 1; 0 0 2 -c(4)];
B = [1.5*h^2 - 2; 2*h^2; 2.5*h^2; 3*h^2 + 1];
X = A\B;                                % X = A^-1 B
disp('     t        y'); disp([t' X]);
