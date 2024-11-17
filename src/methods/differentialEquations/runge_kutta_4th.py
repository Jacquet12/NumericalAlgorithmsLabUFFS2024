# src/methods/differentialEquations/runge_kutta.py
def runge_kutta_fourth_order(f, x0, y0, h, x_end):
    """
    Método de Runge-Kutta de quarta ordem para resolver EDOs.

    Parâmetros:
    - f: função que define a EDO (dy/dx = f(x, y)).
    - x0: valor inicial de x.
    - y0: valor inicial de y.
    - h: tamanho do passo.
    - x_end: valor final de x.

    Retorna:
    - xs: lista de valores de x.
    - ys: lista de valores de y.
    """
    xs = [x0]
    ys = [y0]
    while xs[-1] < x_end:
        x = xs[-1]
        y = ys[-1]
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        x_next = x + h
        y_next = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

        xs.append(x_next)
        ys.append(y_next)
    return xs, ys


if __name__ == "__main__":
    # Teste do Método de Runge-Kutta de Quarta Ordem
    def f(x, y):
        return y - x**2 + 1

    x0, y0 = 0, 0.5
    h = 0.2
    n = 10

    xs, ys = runge_kutta_fourth_order(f, x0, y0, h, n)
    print("Teste do Método de Runge-Kutta de Quarta Ordem:")
    for x, y in zip(xs, ys):
        print(f"x = {x:.2f}, y = {y:.4f}")
