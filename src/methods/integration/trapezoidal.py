def trapezoidal_rule(f, a, b, n):
    """
    Método dos Trapézios para integração numérica.

    Parâmetros:
    - f: função a ser integrada.
    - a: limite inferior de integração.
    - b: limite superior de integração.
    - n: número de subintervalos.

    Retorna:
    - Aproximação da integral de f(x) de a até b.
    """
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

if __name__ == "__main__":
    import math

    def f(x):
        return math.sin(x)

    a, b, n = 0, math.pi, 10
    integral = trapezoidal_rule(f, a, b, n)
    print(f"Método dos Trapézios: Integral = {integral:.6f}")
