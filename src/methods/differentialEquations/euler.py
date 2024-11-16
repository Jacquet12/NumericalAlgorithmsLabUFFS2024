def euler_method(f, x0, y0, h, n):
    """
    Método de Euler para resolver equações diferenciais.

    Parâmetros:
    - f: função que define a EDO (dy/dx = f(x, y)).
    - x0: valor inicial de x.
    - y0: valor inicial de y.
    - h: tamanho do passo.
    - n: número de iterações.

    Retorna:
    - xs: lista de valores de x.
    - ys: lista de valores de y.
    """
    xs = [x0]
    ys = [y0]

    for _ in range(n):
        y_next = ys[-1] + h * f(xs[-1], ys[-1])
        x_next = xs[-1] + h

        xs.append(x_next)
        ys.append(y_next)

    return xs, ys

if __name__ == "__main__":
    # Teste do Método de Euler
    def f(x, y):
        return y - x**2 + 1

    x0, y0 = 0, 0.5
    h = 0.2
    n = 10

    xs, ys = euler_method(f, x0, y0, h, n)
    print("Teste do Método de Euler:")
    for x, y in zip(xs, ys):
        print(f"x = {x:.2f}, y = {y:.4f}")
