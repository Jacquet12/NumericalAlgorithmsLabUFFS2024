import numpy as np
def gauss_jordan(A, b):
    """
    Método de Gauss-Jordan para resolver sistemas lineares Ax = b.

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

        # Normaliza a linha do pivô
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]

        # Zera os elementos acima e abaixo do pivô
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    # Extraindo a solução
    x = augmented_matrix[:, -1]
    return x

# Exemplo de uso
if __name__ == "__main__":
    # Matriz de coeficientes A e vetor b
    A_jordan = np.array([[2, -1, 1],
                         [3, 3, 9],
                         [3, 3, 5]], dtype=float)
    b_jordan = np.array([2, -1, 4], dtype=float)

    # Resolvendo o sistema com Gauss-Jordan
    x_jordan = gauss_jordan(A_jordan, b_jordan)
    print(f"Solução: x = {x_jordan}")

