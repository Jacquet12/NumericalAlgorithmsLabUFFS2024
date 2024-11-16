import numpy as np

def gauss_elimination(A, b):
    """
    Método de Eliminação de Gauss para resolver sistemas lineares Ax = b.

    Parâmetros:
    - A: matriz de coeficientes (n x n).
    - b: vetor de constantes (n x 1).

    Retorna:
    - x: solução do sistema.
    """
    n = len(A)
    # Construindo a matriz aumentada
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))

    # Etapa de Eliminação
    for i in range(n):
        # Verifica se o pivô é zero
        if augmented_matrix[i, i] == 0:
            raise ValueError("Pivô zero encontrado. Reordene as linhas ou use pivotamento.")

        # Eliminação Gaussiana
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Etapa de Substituição Retroativa
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:n], x[i + 1:])) / augmented_matrix[i, i]

    return x

# Exemplo de uso
if __name__ == "__main__":
    # Matriz de coeficientes A e vetor b
    A = np.array([[3, -0.1, -0.2],
                  [0.1, 7, -0.3],
                  [0.3, -0.2, 10]], dtype=float)
    b = np.array([7.85, -19.3, 71.4], dtype=float)

    # Resolvendo o sistema com Eliminação de Gauss
    x = gauss_elimination(A, b)
    print(f"Solução: x = {x}")

