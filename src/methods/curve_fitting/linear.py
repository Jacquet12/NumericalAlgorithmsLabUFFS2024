import numpy as np

def linear_regression(x, y):
    """
    Realiza ajuste linear (regressão linear simples) para um conjunto de pontos.

    Parâmetros:
    - x: array de valores de entrada (variável independente).
    - y: array de valores de saída (variável dependente).

    Retorna:
    - m: coeficiente angular da reta.
    - b: coeficiente linear da reta.
    """
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    b = y_mean - m * x_mean

    return m, b

if __name__ == "__main__":
    # Teste do Ajuste Linear
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.2, 2.8, 4.5, 3.7, 5.5])
    m, b = linear_regression(x, y)
    print(f"Teste de Ajuste Linear: y = {m:.4f}x + {b:.4f}")
