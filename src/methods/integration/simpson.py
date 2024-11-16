def simpson_rule(f, a, b, n):
    """
    Método de Simpson para integração numérica.

    Parâmetros:
    - f: função a ser integrada.
    - a: limite inferior de integração.
    - b: limite superior de integração.
    - n: número de subintervalos (deve ser par).

    Retorna:
    - Aproximação da integral de f(x) de a até b.
    """
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser par para o método de Simpson.")

    h = (b - a) / n
    result = f(a) + f(b)

    # Soma dos termos com peso 4
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)

    # Soma dos termos com peso 2
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)

    result *= h / 3
    return result

if __name__ == "__main__":
    import math

    def f(x):
        return math.sin(x)

    a, b, n = 0, math.pi, 10
    integral = simpson_rule(f, a, b, n)
    print(f"Método de Simpson: Integral = {integral:.6f}")
