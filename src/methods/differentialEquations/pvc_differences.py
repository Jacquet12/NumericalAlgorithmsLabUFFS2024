def pvc_differences(g, a, b, ya, yb, n):
    """
    Resolução de PVC por diferenças finitas.

    Parâmetros:
    - g: função que define a segunda derivada (d²y/dx² = g(x)).
    - a: limite inferior de x.
    - b: limite superior de x.
    - ya: condição de contorno em x = a.
    - yb: condição de contorno em x = b.
    - n: número de subintervalos.

    Retorna:
    - xs: lista de valores de x.
    - ys: lista de valores de y.
    """
    h = (b - a) / (n + 1)
    xs = [a + i * h for i in range(n + 2)]
    A = [[0] * n for _ in range(n)]
    b_vec = [g(xs[i + 1]) for i in range(n)]

    b_vec[0] -= ya / h**2
    b_vec[-1] -= yb / h**2

    for i in range(n):
        A[i][i] = -2 / h**2
        if i > 0:
            A[i][i - 1] = 1 / h**2
        if i < n - 1:
            A[i][i + 1] = 1 / h**2

    from numpy.linalg import solve
    ys_internal = solve(A, b_vec)
    ys = [ya] + list(ys_internal) + [yb]

    return xs, ys

if __name__ == "__main__":
    # Teste da Resolução de PVC por Diferenças Finitas
    def g(x):
        return -2  # Exemplo para y'' = g(x)

    a, b = 0, 1
    ya, yb = 1, 0
    n = 5

    xs, ys = pvc_differences(g, a, b, ya, yb, n)
    print("Teste da Resolução de PVC por Diferenças Finitas:")
    for x, y in zip(xs, ys):
        print(f"x = {x:.2f}, y = {y:.4f}")
