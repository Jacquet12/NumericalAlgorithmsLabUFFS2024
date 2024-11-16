import numpy as np

def exponential_regression(x, y):
    """
    Realiza ajuste exponencial para um conjunto de pontos.

    Parâmetros:
    - x: array de valores de entrada (variável independente).
    - y: array de valores de saída (variável dependente).

    Retorna:
    - a: coeficiente da base exponencial.
    - b: taxa de crescimento/decrescimento.
    """
    log_y = np.log(y)
    x_mean = np.mean(x)
    log_y_mean = np.mean(log_y)

    b = np.sum((x - x_mean) * (log_y - log_y_mean)) / np.sum((x - x_mean) ** 2)
    a = np.exp(log_y_mean - b * x_mean)

    return a, b

if __name__ == "__main__":
    # Teste do Ajuste Exponencial
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.7, 7.4, 20.1, 54.6, 148.4])
    a, b = exponential_regression(x, y)
    print(f"Teste de Ajuste Exponencial: y = {a:.4f}e^{b:.4f}x")
