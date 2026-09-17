def bisseccao(f, a, b, eps=1e-4, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) e f(b) precisam ter sinais opostos")

    historico = []
    for k in range(1, max_iter + 1):
        m = (a + b) / 2
        fm = f(m)
        historico.append((k, m, fm))

        if abs(fm) < eps or (b - a) / 2 < eps:
            return m, historico

        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    return m, historico


def posicao_falsa(f, a, b, eps=1e-4, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) e f(b) precisam ter sinais opostos")

    historico = []
    x_anterior = None
    for k in range(1, max_iter + 1):
        x = a - fa * (b - a) / (fb - fa)
        fx = f(x)
        historico.append((k, x, fx))

        if abs(fx) < eps or (x_anterior is not None and abs(x - x_anterior) < eps):
            return x, historico

        if fa * fx < 0:
            b, fb = x, fx
        else:
            a, fa = x, fx
        x_anterior = x

    return x, historico


def ponto_fixo(phi, f, x0, eps1=1e-4, eps2=1e-4, max_iter=100):
    x = x0
    historico = []
    for k in range(1, max_iter + 1):
        x_novo = phi(x)
        f_novo = f(x_novo)
        historico.append((k, x_novo, f_novo))

        if abs(f_novo) < eps1 or abs(x_novo - x) < eps2:
            return x_novo, historico
        x = x_novo

    return x_novo, historico


def newton_raphson(f, fdev, x0, eps1=1e-4, eps2=1e-4, max_iter=100):
    x = x0
    historico = []
    for k in range(1, max_iter + 1):
        fx, dfx = f(x), fdev(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivada nula")
        x_novo = x - fx / dfx
        f_novo = f(x_novo)
        historico.append((k, x_novo, f_novo))

        if abs(f_novo) < eps1 or abs(x_novo - x) < eps2:
            return x_novo, historico
        x = x_novo

    return x_novo, historico


def secante(f, x0, x1, eps1=1e-4, eps2=1e-4, max_iter=100):
    f0, f1 = f(x0), f(x1)
    historico = []

    for k in range(1, max_iter + 1):
        if f1 - f0 == 0:
            raise ZeroDivisionError("f(x1) - f(x0) = 0, método falhou")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)
        historico.append((k, x2, f2))

        if abs(f2) < eps1 or abs(x2 - x1) < eps2:
            return x2, historico

        x0, f0 = x1, f1
        x1, f1 = x2, f2

    return x2, historico