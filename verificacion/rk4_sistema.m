% RK4 para sistemas, notación del profesor (K para x, C para y).
% Uso: cambia f, g, t, x, y, H, n. trunc=1 trunca a 4 decimales como en la pizarra.
f = @(t,x,y) 3*x - 3*y + 2;      % x' = f(t,x,y)
g = @(t,x,y) -6*x - t;           % y' = g(t,x,y)
t = 0; x = 1; y = -1; H = 0.1; n = 1; trunc = 1;
r = @(v) v; if trunc, r = @(v) fix(v*1e4)/1e4; end
for it = 1:n
  K1 = r(H*f(t,x,y));            C1 = r(H*g(t,x,y));
  K2 = r(H*f(t+H/2,x+K1/2,y+C1/2)); C2 = r(H*g(t+H/2,x+K1/2,y+C1/2));
  K3 = r(H*f(t+H/2,x+K2/2,y+C2/2)); C3 = r(H*g(t+H/2,x+K2/2,y+C2/2));
  K4 = r(H*f(t+H,x+K3,y+C3));       C4 = r(H*g(t+H,x+K3,y+C3));
  x = x + (K1 + 2*(K2+K3) + K4)/6;
  y = y + (C1 + 2*(C2+C3) + C4)/6;
  t = t + H;
  fprintf('iter %d: K = [%g %g %g %g]  C = [%g %g %g %g]\n', it, K1,K2,K3,K4, C1,C2,C3,C4);
  fprintf('        t = %.1f  x = %.4f  y = %.4f\n', t, r(x), r(y));
end
