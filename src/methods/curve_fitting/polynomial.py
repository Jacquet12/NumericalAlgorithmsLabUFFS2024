import numpy as np

def polynomial_regression(x, y, degree):
    """
    Realiza ajuste polinomial de grau especificado.

    Parâmetros:
    - x: array de valores de entrada (variável independente).
    - y: array de valores de saída (variável dependente).
    - degree: grau do polinômio.

    Retorna:
    - coef: coeficientes do polinômio.
    """
    coef = np.polyfit(x, y, degree)
    return coef

if __name__ == "__main__":
    # Teste do Ajuste Polinomial
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 4, 9, 16, 25])
    degree = 2
    coef = polynomial_regression(x, y, degree)
    print(f"Teste de Ajuste Polinomial (grau {degree}): Coeficientes = {coef}")
