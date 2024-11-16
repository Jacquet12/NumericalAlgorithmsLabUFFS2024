import numpy as np

def simpson_rule(f, a, b, epsilon=1e-3):
    """
    Calcula a integral de f(x) no intervalo [a, b] usando a regra de Simpson,
    ajustando automaticamente o número de subintervalos para atingir a precisão desejada.
    
    Parâmetros:
    - f: função a ser integrada.
    - a: limite inferior de integração.
    - b: limite superior de integração.
    - epsilon: tolerância para o erro.

    Retorna:
    - Aproximação da integral.
    - Tabela de pontos (x_i, y_i).
    """
    n = 2  # Começamos com um número par de subintervalos
    integral_prev = 0
    while True:
        x = np.linspace(a, b, n + 1)
        y = f(x)
        h = (b - a) / n
        integral = h / 3 * (y[0] + 2 * np.sum(y[2:-1:2]) + 4 * np.sum(y[1::2]) + y[-1])
        if abs(integral - integral_prev) < epsilon:
            break
        integral_prev = integral
        n *= 2

    points = np.column_stack((x, y))  # Tabela de pontos (x_i, y_i)
    return integral, points
